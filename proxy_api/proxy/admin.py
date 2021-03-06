from django.contrib import admin
from .models import API, Method, ContentType, APICallLog


@admin.register(ContentType)
class ContentTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Method)
class MethodAdmin(admin.ModelAdmin):
    pass


@admin.register(API)
class APIAdmin(admin.ModelAdmin):
    pass


@admin.register(APICallLog)
class APICallLogAdmin(admin.ModelAdmin):
    pass
