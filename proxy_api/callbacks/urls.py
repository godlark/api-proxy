from django.urls import path

from . import views

app_name = 'callbacks'
urlpatterns = [
    path('forward/<slug:callback_slug>/<path:callback_path>',
         views.forward, name='forward_path'),
    path('forward/<slug:callback_slug>/',
         views.forward, name='forward'),
    path('replay/<int:id>/',
         views.replay, name='replay'),
]
