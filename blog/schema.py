import strawberry
from typing import List

from django.contrib.contenttypes.models import ContentType

from .types import PostType, CommentType, VoteType
from .models import Post, Comment, Vote

@strawberry.type
class Query:
    @strawberry.field
    def posts(self, author: str = None) -> List[PostType]:
        if author:
            return Post.objects.filter(author=author)
    
        return Post.objects.all()
    
    @strawberry.field
    def post(self, post_id: int) -> PostType:
        return Post.objects.get(post_id=post_id)
    
    @strawberry.field
    def comments(self, author: str = None) -> List[CommentType]:
        if author:
            return Comment.objects.filter(author=author)
        else:
            return Comment.objects.all()
        
    @strawberry.field
    def votes(self) -> List[VoteType]:
        return Vote.objects.all()
    
    @strawberry.field
    def vote(self, vote_id: int) -> VoteType:
        return Vote.objects.get(vote_id=vote_id)
        
@strawberry.type
class Mutation:
    @strawberry.field 
    def create_post(self, title: str, content: str, author: str) -> PostType:
        post = Post(title=title, content=content, author=author)
        post.save()
        return post

    @strawberry.field
    def update_post(self, post_id: int, title: str, content: str, author: str) -> PostType:
        post = Post.objects.get(post_id=post_id)
        post.title = title
        post.content = content
        post.author = author
        post.save()
        return post

    @strawberry.field
    def delete_post(self, post_id: int) -> bool:
        post = Post.objects.get(post_id=post_id)
        post.delete()
        return True
    
    @strawberry.field 
    def create_comment(self, post_id: int, content: str, author: str) -> CommentType:
        post = Post.objects.get(post_id=post_id)
        comment = Comment(post=post, content=content, author=author)
        comment.save()
        return comment

    @strawberry.field
    def update_comment(self, comment_id: int, content: str, author: str) -> CommentType:
        comment = Comment.objects.get(comment_id=comment_id)
        comment.content = content
        comment.author = author
        comment.save()
        return comment
    
    @strawberry.field
    def create_vote(self, vote_type: int, content_type: str, object_id: int, voter: str) -> VoteType:
        content_type = ContentType.objects.get(model=content_type)
        vote = Vote(content_type=content_type, object_id=object_id, vote_type=vote_type, voter=voter)
        vote.save()
        return vote
    
    @strawberry.field
    def update_vote(self, vote_id:int, vote_type: str) -> VoteType:
        vote = Vote.objects.get(vote_id=vote_id)
        vote_type = vote_type
        vote.save()
        return vote
    
    @strawberry.field
    def delete_vote(self, vote_id: int) -> bool:
        vote = Vote.objects.get(vote_id=vote_id)
        vote.delete()
        return True

schema = strawberry.Schema(query=Query, mutation=Mutation)


