from django.shortcuts import render, redirect

from .models import Post
from .forms import PostForm


def post_list(request):
    post_list = Post.objects.all().order_by('-pk')

    return render(request, 'post/list.html', {'post_list': post_list})


def by_author(request, user_id):
    post_list = Post.objects.filter(author=user_id).order_by('-pk')

    return render(request, 'post/list.html', {'post_list': post_list})


def add_post(request):
    if request.method != 'POST':
        form = PostForm()
        return render(request, 'post/add.html', {'form': form})

    form = PostForm(request.POST or None, request.FILES or None)

    if not form.is_valid():
        return render(request, 'post.add.html', {'form': form})

    post = form.save(commit=False)
    post.author = request.user
    post.save()

    return redirect('post_list')
