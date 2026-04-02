import graphene
from posts.models import Post
from graphene import ObjectType, String, List, ID, DateTime

class PostType(ObjectType):
    id = ID()
    title = String()
    body = String()
    created_at = DateTime()

class Query(ObjectType):
    posts = List(PostType)

    def resolve_posts(self, info):
        return Post.objects.all()

class CreatePost(graphene.Mutation):
    class Arguments:
        title = String()
        body = String()

    post = graphene.Field(PostType)

    def mutate(self, info, title, body):
        post = Post(title=title, body=body)
        post.save()
        return CreatePost(post=post)

class Mutation(ObjectType):
    create_post = CreatePost.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
