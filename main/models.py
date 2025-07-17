from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
