from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone


class PostPublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            published_date__lte=timezone.now())