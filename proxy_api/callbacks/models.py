from django.contrib.postgres.fields import JSONField
from django.db import models


class Method(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Callback(models.Model):
    slug = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=100)
    methods = models.ManyToManyField(Method)

    def __str__(self):
        return "{} - {}".format(self.slug, self.url)


class CallbackCallLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    callback = models.ForeignKey(Callback, on_delete=models.CASCADE)

    request_path = models.CharField(max_length=1000, blank=True)
    request_body = models.TextField(blank=True)
    request_body_binary = models.BinaryField(blank=True)
    request_headers = JSONField()

    content = models.TextField()
    status = models.IntegerField()
    reason = models.TextField()
    charset = models.CharField(blank=True, max_length=100)
    content_type = models.CharField(blank=True, max_length=100)
