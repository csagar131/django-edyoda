from rest_framework import serializers
from blog.models import Category,Post
from rest_framework.validators import UniqueValidator 

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id','name']

   
class PostSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    title = serializers.CharField(max_length=30,validators =[UniqueValidator(queryset = Post.objects.all())])

    class Meta:
        model = Post
        fields = ['id','title','content','category','status','category_name','image']


    def get_category_name(self,obj):
        return obj.category.name



