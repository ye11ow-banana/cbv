from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='main_page'),
    path('blogs/', views.Blogs.as_view(), name='blogs'),
    path('<slug:slug>/', views.Blog.as_view(), name='blog'),
]