from django.contrib.postgres.fields import JSONField
from django.db import models


class ContentType(models.Model):
    slug = models.CharField(max_length=100, unique=True)
    format = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return "{} : {}".format(self.slug, self.format)


class Method(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class API(models.Model):
    slug = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=100)
    methods = models.ManyToManyField(Method)
    accepted_content_types = models.ManyToManyField(ContentType)

    def __str__(self):
        return "{} - {}".format(self.slug, self.url)


class APICallLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    api = models.ForeignKey(API, on_delete=models.CASCADE)

    request_body = models.TextField()
    request_headers = JSONField()

    content = models.TextField()
    status = models.IntegerField()
    reason = models.TextField()
    charset = models.CharField(blank=True, max_length=100)
    content_type = models.CharField(blank=True, max_length=100)
