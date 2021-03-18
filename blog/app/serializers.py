from app.models import Post, Category
from rest_framework import serializers
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class CategorySerializer(serializers.ModelSerializer):
    
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'


class CategorySerializerNoPosts(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
  
    author = AuthorSerializer()
    category = CategorySerializerNoPosts()
    class Meta:
        model = Post
        fields = '__all__'


class PostSerializerWrite(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'