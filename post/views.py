from django.http.response import Http404
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

class PostList(APIView):
    def get(self,request):
        postList = Post.objects.all()
        serializer = PostSerializer(postList,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
class PostDetail(APIView):
    def get_post(self,id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request,id):
        post = self.get_post(id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, id):
        post = self.get_post(id)
        serializer = PostSerializer(Post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self, request, id):
        article = self.get_post(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)