from django.db import models


class BlogModel(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=30)
    owner = models.CharField(max_length=30)
