from django.urls import path

from . import views

app_name = 'proxy'
urlpatterns = [
    path('<slug:api_slug>/<path:api_path>',
         views.forward, name='forward_path'),
    path('<slug:api_slug>/',
         views.forward, name='forward'),
]
