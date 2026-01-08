from django.shortcuts import render

# Create your views here.
from .serializer import PostSerializer
from posts .models import Post
from rest_framework import mixins, generics


class PostApi(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request):
        return self.list(request)
    

    def post(self, request):
        return self.create(request)
    
class PostDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin  ,generics.GenericAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

    def get(self,request,pk):
       return self.retrieve(request,pk)
    
    def put(self,request,pk):
       return self.update(request,pk) 

    def delete(self,request,pk):
       return self.destroy(request,pk)