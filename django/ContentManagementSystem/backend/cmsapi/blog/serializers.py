from rest_framework import serializers
from blog.models import Category,Post


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id','name']

   


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ['id','title','content','category','status']

    def create(self,validated_data):
        return Post.objects.create(**validated_data)



