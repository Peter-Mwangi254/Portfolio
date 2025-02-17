from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('projects/', views.projects, name="projects"),
    path('contact/', views.contact, name="contact"),
    path('resume/', views.resume, name="resume"),

    path('posts/', views.posts, name="posts"),
    path('posts/<slug:slug>/', views.post_detail, name="post_detail"),

]