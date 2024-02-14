import strawberry
from .models import Post, Comment, Vote
from typing import List

    
@strawberry.django.type(Vote)
class VoteType:
    vote_id: int
    vote_type: str
    voter: str

@strawberry.django.type(Post)
class PostType:
    post_id: int
    title: str
    content: str
    author: str
    comments:List['CommentType']
    votes: List['VoteType']

    # @strawberry.field
    # def comments(self) -> List['CommentType']:
    #     return Comment.objects.filter(post_id=self.post_id)
    
    # @strawberry.field
    # def votes(self) -> List['VoteType']:
    #     # votes = Vote.objects.filter(object_id=self.post_id)
    #     # return [VoteType(vote_id=vote.vote_id, vote_type=vote.vote_type, voter=vote.voter) for vote in votes]
    #     return Vote.objects.filter(object_id=self.post_id)
    
@strawberry.django.type(Comment)
class CommentType:
    comment_id: int
    post:PostType
    content: str
    author: str
    votes: List['VoteType']

    # @strawberry.field
    # def votes(self) -> List['VoteType']:
    #     votes = Vote.objects.filter(object_id=self.comment_id)
    #     return [VoteType(vote_id=vote.vote_id, vote_type=vote.vote_type, voter=vote.voter) for vote in votes]
