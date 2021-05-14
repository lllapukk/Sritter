from django.shortcuts import render

from .models import Post


def post_list(request):
    post_list = Post.objects.all().order_by('-pk')

    return render(request, 'post/list.html', {'post_list': post_list})


def post_list_by_author(request, user_id):
    post_list = Post.objects.filter(author=user_id).order_by('-pk')

    return render(request, 'post/list.html', {'post_list': post_list})


def add_post(request):
    if request.method != 'POST':
        return render(request, 'post/add.html')

    header = request.POST.get('header')
    text = request.POST.get('text')
    image = request.FILES.get('image')

    Post.objects.create(header=header, text=text, image=image, author=request.user)

    return render(request, 'post/add.html', {
        'header': header, 'text': text, 'image': image
    })
