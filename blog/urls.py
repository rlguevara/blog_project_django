from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('article/create/', views.article_create, name='article_create'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
] 