import strawberry
from .models import Post, Comment
from typing import List

@strawberry.type
class PostType:
    post_id: int
    title: str
    content: str
    author: str
    comments:List['CommentType']
    
    @strawberry.field
    def comments(self) -> List['CommentType']:
        return Comment.objects.filter(post_id=self.post_id)
    
@strawberry.type
class CommentType:
    comment_id: int
    post:PostType
    content: str
    author: str

