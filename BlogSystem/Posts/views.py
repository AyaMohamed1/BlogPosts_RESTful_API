from Posts.models import Post, Author, Category
from Posts.serializers import PostSerializer, AuthorSerializer, CategorySerializer, AuthorPostsSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AuthorPosts(APIView):
    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        author = self.get_object(pk)
        author_posts_serializer = AuthorPostsSerializer(author)
        return Response(author_posts_serializer.data)

class AuthorsPosts(APIView):
    def get(self, request, format=None):
        authors_posts = Author.objects.all()
        authors_posts_serializer = AuthorPostsSerializer(authors_posts, many = True)
        return Response(authors_posts_serializer.data)
        
