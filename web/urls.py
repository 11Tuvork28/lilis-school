from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('blog/<int:blog_id>', views.blog, name='blog'),
]
