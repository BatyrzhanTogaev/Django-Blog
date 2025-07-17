from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='images_post/')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} -> {self.author}'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')

    def __str__(self):
        return f'{self.text[:20]}'
