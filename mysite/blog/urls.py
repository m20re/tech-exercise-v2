from  django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
]