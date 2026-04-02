from django.shortcuts import render

# Create your views here.
from .serializer import PostSerializer
from posts .models import Post
from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import status


class PostApi(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

    def get(self, request):

        if not request.user.is_staff:
            return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
        return self.list(request)
    

    def post(self, request):
        if not request.user.is_staff:
            return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
        return self.create(request)
    
class PostDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, pk):
        if not request.user.is_staff:
            return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
        return self.retrieve(request, pk)

    def put(self, request, pk):
        if not request.user.is_staff:
            return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
        return self.update(request, pk)

    def delete(self, request, pk):
        if not request.user.is_staff:
            return Response({"detail": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
        return self.destroy(request, pk)