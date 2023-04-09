from django.urls import path
from Posts.views import PostList, PostDetail, AuthorList, AuthorDetail, CategoryList, CategoryDetail

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('authors/',AuthorList.as_view()),
    path('authors/<int:pk>/',AuthorDetail.as_view()),
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),

]