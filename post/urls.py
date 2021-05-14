from django.urls import path

from .views import (
    post_list,
    post_list_by_author,
    add_post
)


urlpatterns = [
    path('posts/', post_list, name='post_list'),
    path('posts/author/<int:user_id>/', post_list_by_author, name='post_list_by_author'),
    path('posts/add/', add_post, name='add_post')
]
