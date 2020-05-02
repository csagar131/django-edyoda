from rest_framework import serializers
from blog.models import Category


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()

    def create(self,validated_data):
        print(validated_data)
        return Category.objects.create(**validated_data)


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=30)
    content = serializers.CharField()
    status = serializers.CharField()
    category = serializers.PrimaryKeyRelatedField(read_only = True)




