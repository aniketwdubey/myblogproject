from django.db import models

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    author = models.CharField(max_length=100)