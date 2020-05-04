from rest_framework import serializers
from blog.models import Category,Post


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id','name']

   


class PostSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id','title','content','category','status','category_name']


    def get_category_name(self,obj):
        return obj.category.name



