from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from .managers import PostPublishedManager, PostManager
from rest_framework import serializers


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=200, verbose_name='Title')
    text = models.TextField(verbose_name='Post text')
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Created date")

    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Published date')
    is_published = models.BooleanField(default=False, verbose_name='Is published?')

    objects = PostManager()
    published = PostPublishedManager()

    def is_publish(self):
        return True if self.published_date else False

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[str(self.id)])

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Blog post'
        verbose_name_plural = 'Blog posts'

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey('blog.post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField(verbose_name='comment')
    created_date = models.DateTimeField(default=timezone.now(), verbose_name='Date of creation')
    approved_comment = models.BooleanField(default=False, verbose_name='Approved?')

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('created_date', 'text')