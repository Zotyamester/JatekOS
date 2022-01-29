from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', views.comment, name='post-comment'),
    path('comment/<int:pk>/update/',
         views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/',
         views.CommentDeleteView.as_view(), name='comment-delete'),
]
