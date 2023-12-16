from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('post/add/', views.post_add, name='post_add')
]