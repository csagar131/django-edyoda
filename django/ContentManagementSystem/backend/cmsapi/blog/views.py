from django.shortcuts import render
from blog.models import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.serializers import PostSerializer
# Create your views here.

class PostAPIView(APIView):
    def get(self,request,*args,**kwargs):
        posts = Post.objects.all()
        ser_obj = PostSerializer(posts,many=True)
        return Response(ser_obj.data)


