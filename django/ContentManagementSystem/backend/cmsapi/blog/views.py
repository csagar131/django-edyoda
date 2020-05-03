from django.shortcuts import render
from blog.models import Post,Category
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from blog.serializers import PostSerializer,CategorySerializer
# Create your views here.

class PostAPIView(APIView):
    def get(self,request,*args,**kwargs):
        posts = Post.objects.all()
        ser_obj = PostSerializer(posts,many=True)
        return Response(ser_obj.data)

    def post(self,request,*args,**kwargs):
        ser_obj = PostSerializer(data = request.data)

        try:
            cat_obj = Category.objects.get(name = request.data.get('category').get('name'))
        except:
            return Response({'error':'Invalid Category'},status = status.HTTP_400_BAD_REQUEST)

        if ser_obj.is_valid():
            ser_obj.validated_data['category'] = cat_obj
            post_obj = ser_obj.save()
            post_ser = PostSerializer(post_obj)
            return Response(post_ser.data,status = status.HTTP_201_CREATED)
        return Response(ser_obj.errors,status = status.HTTP_400_BAD_REQUEST)

