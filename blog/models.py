from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

from django.db import models

class Vote(models.Model):
    UP_VOTE = 1
    DOWN_VOTE = -1
    VOTE_CHOICES = (
        (UP_VOTE, 'Upvote'),
        (DOWN_VOTE, 'Downvote'),
    )

    vote_id = models.AutoField(primary_key=True)
    vote_type = models.IntegerField(choices=VOTE_CHOICES)

    voter = models.CharField(max_length=100)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    votes = GenericRelation(Vote)


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    author = models.CharField(max_length=100)
    votes = GenericRelation(Vote)


