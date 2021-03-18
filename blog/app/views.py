from django.shortcuts import render
from app.models import Post, Category
from app.serializers import PostSerializer, PostSerializerWrite, \
        CategorySerializer, AuthorSerializer
from django.contrib.auth.models import User
from rest_framework import generics


# Create your views here.
class MethodSerializerView(object):
  
    method_serializer_classes = None

    def get_serializer_class(self):
        assert self.method_serializer_classes is not None, (
            'Expected view %s should contain method_serializer_classes '
            'to get right serializer class.' %
            (self.__class__.__name__, )
        )
        for methods, serializer_cls in self.method_serializer_classes.items():
            if self.request.method in methods:
                return serializer_cls

        raise exceptions.MethodNotAllowed(self.request.method)


class PostList(MethodSerializerView, generics.ListCreateAPIView):  
  
    queryset = Post.objects.all()
    method_serializer_classes = {
            ('GET', ): PostSerializer,
            ('POST'): PostSerializerWrite,
    }
    

class PostDetail(MethodSerializerView, generics.RetrieveUpdateDestroyAPIView):  
    
    queryset = Post.objects.all()  
    method_serializer_classes = {
            ('GET', ): PostSerializer,
            ('PUT', 'PATCH'): PostSerializerWrite,
    }
    

class CategoryList(generics.ListCreateAPIView):
   
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):  
  
    queryset = Category.objects.all()  
    serializer_class = CategorySerializer


class AuthorList(generics.ListAPIView):
   
    queryset = User.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveAPIView):  
  
    queryset = User.objects.all()  
    serializer_class = AuthorSerializer