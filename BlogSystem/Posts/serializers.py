from rest_framework import serializers
from Posts.models import Post, Author, Category

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = ('created_at', 'updated_at')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('created_at', 'updated_at')