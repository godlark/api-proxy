from django.db import models


class ContentType(models.Model):
    slug = models.CharField(max_length=100, unique=True)
    format = models.CharField(max_length=100, unique=True)


class Method(models.Model):
    name = models.CharField(max_length=10, unique=True)


class Proxy(models.Model):
    slug = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=100)
    methods = models.ManyToManyField(Method)
    content_types = models.ManyToManyField(ContentType)
