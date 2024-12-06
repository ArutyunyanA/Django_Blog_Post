from django.db.models import Count
from django.shortcuts import render, redirect
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.utils.text import slugify
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity
from .forms import EmailPostForm, CommentForm, SearchForm, PostForm
from taggit.models import Tag
from .models import Post, Comment




def post_list(request, tag_slug=None):
    post_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])
    # pagination list for 3 posts on a page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # Если page_number не целое число, то 
        # выдать первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        # Если page_number находится вне диапазона, то 
        # выдать последнюю страницу
        posts = paginator.page(paginator.num_pages)
    return render(
        request, 
        'blog/post/list.html',
        {'posts': posts, 'tag': tag}
    )


def post_share(request, post_id):
    # Извлечь пост по идентификатору id
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
    # Форма была передана на обработку
        form = EmailPostForm(request.POST)
        if form.is_valid():
        # Поля формы успешно прошли валидацию
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recomends you to read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n{cd['name']}'s commments: {cd['comments']}"
            send_mail(subject, message, 'your@accountmail.com', [cd['to']])
            sent = True
    # ... отправить электронное письмо
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})
 

def post_details(request, year, month, day, post):
    post = get_object_or_404(
        Post, 
        status=Post.Status.PUBLISHED, 
        # Убираем id=id вместо этого добавляем year, month, day и post
        # чтобы использовать аргументы и извлекать опубликованный пост с заданным 
        # слагом и датой публикации.
        slug=post, 
        publish__year=year, 
        publish__month=month, 
        publish__day=day)
    # Список активных комментариев к этому посту
    comments = post.comments.filter(active=True)
    # Форма для комментирования пользователями
    form = CommentForm()
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', 'publish')[:4]
    return render(request, 'blog/post/details.html', {'post': post, 'comments': comments, 'form': form, 'similar_posts': similar_posts})

def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.published.annotate(
                similarity=TrigramSimilarity('title', query),).filter(similarity__gt=0.1).order_by('-similarity')
    return render(request, 'blog/post/search.html', {'form': form, 'query': query, 'results': results})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if not post.slug:
                post.slug = slugify(post.title)
            post.save()
            return redirect(post.get_absolute_url())
    else:
        form = PostForm()
    return render(request, 'blog/post/post_create.html', {'form': form})

@login_required
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    # Комментарий был отправлен
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            # Создать объект класса Comment, не сохраняя его в базе данных
            comment = form.save(commit=False)
            # Назначить пост комментарию
            comment.post = post
            # Привязываем автора комментария
            comment.author = request.user
            # Сохранить комментарий в базе данных
            comment.save()
            return redirect(post.get_absolute_url())
    else:
        #Создаем пустую форму при запросе GET
        form = CommentForm()
    return render(request, 'blog/post/comment.html', {'post': post, 'form': form, 'comment': comment})
