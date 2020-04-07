from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(),name="blog-home"),
    path('about/', views.about,name="blog-about"),
    path('post/<int:pk>/', views.PostDetailView.as_view(),name="post-detail"),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(),name="post-update"),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(),name="post-delete"),
    path('post/new/', views.PostCreatView.as_view(),name="post-create"),
]
