from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.urls import reverse


class CustomUser(AbstractUser):
    followers = models.ManyToManyField("self", through='Contact', related_name="following_set", symmetrical=False)

    def get_absolute_url(self):
        return reverse('account:user_detail', args=[self.username])

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="profile_pictures/", null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

class Contact(models.Model):
    user_from = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following', on_delete=models.CASCADE)
    user_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following_by_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_from', 'user_to')
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']
    
    def __str__(self):
        return f"{self.user_from} follows {self.user_to}"