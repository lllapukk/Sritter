from django.urls import path

from .views import (
    post_list,
    by_author,
    add_post
)


urlpatterns = [
    path('posts/', post_list, name='post_list'),
    path('posts/author/<int:user_id>/', by_author, name='by_author'),
    path('posts/add/', add_post, name='add_post')
]
