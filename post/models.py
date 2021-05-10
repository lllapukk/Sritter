from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    header = models.CharField(max_length=50, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    published_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    image = models.ImageField()
