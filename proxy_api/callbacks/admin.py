from django.contrib import admin
from .models import Callback, Method, CallbackCallLog


@admin.register(Method)
class MethodAdmin(admin.ModelAdmin):
    pass


@admin.register(Callback)
class CallbackAdmin(admin.ModelAdmin):
    pass


@admin.register(CallbackCallLog)
class CallbackCallLogAdmin(admin.ModelAdmin):
    pass
