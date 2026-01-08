from django.urls import path, include
from .views import PostApi,PostDetail
from graphene_django.views import GraphQLView
from .schema import schema
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('posts/', PostApi.as_view(), name='posts_api'),
    path('posts/<int:pk>',PostDetail.as_view(),name='postsDetail_api'),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    

]
    
