from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from .managers import PostPublishedManager


class Post(models.Model):
    published = PostPublishedManager()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def is_publish(self):
        return True if self.published_date else False

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Blog post'
        verbose_name_plural = 'Blog posts'

    def __str__(self):
        return self.title