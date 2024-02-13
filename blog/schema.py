import strawberry
from typing import List

from sympy import Q
from .types import PostType, CommentType
from .models import Post, Comment

@strawberry.type
class Query:
    @strawberry.field
    def posts(self, author: str = None) -> List[PostType]:
        if author:
            return Post.objects.filter(author=author)
        else:
            return Post.objects.all()

    @strawberry.field
    def post(self, post_id: int) -> PostType:
        return Post.objects.get(post_id=post_id)
    
    # @strawberry.field
    # def comments(self, author: str = None) -> List[CommentType]:
    #     if author:
    #         return Comment.objects.filter(author=author)
    #     else:
    #         return Comment.objects.all()
    
    
    @strawberry.field
    def paginated_posts(self, first: int, after: str = None) -> List[PostType]:
        queryset = Post.objects.order_by('post_id')
        if after:
            queryset = queryset.filter(post_id__gt=after)
        return queryset[:first]
        
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
    def delete_comment(self, comment_id: int) -> bool:
        comment = Comment.objects.get(comment_id=comment_id)
        comment.delete()
        return True

schema = strawberry.Schema(query=Query, mutation=Mutation)





