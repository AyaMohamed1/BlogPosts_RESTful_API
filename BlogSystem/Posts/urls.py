from django.urls import path
from Posts.views import PostList, PostCreate, PostDetail, PostUpdate, PostDelete,\
    AuthorList, AuthorDetail, AuthorCreate, AuthorUpdate, AuthorDelete, AuthorPosts, AuthorsPosts, \
        CategoryList, CategoryCreate, CategoryDetail, CategoryUpdate, CategoryDelete

urlpatterns = [
    path('', PostList.as_view()),
    path('create/', PostCreate.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('<int:pk>/update/', PostUpdate.as_view()),
    path('<int:pk>/delete/', PostDelete.as_view()),
    path('authors/', AuthorList.as_view()),
    path('authors/create/', AuthorCreate.as_view()),
    path('authors/<int:pk>/', AuthorDetail.as_view()),
    path('authors/<int:pk>/update/', AuthorUpdate.as_view()),
    path('authors/<int:pk>/delete/', AuthorDelete.as_view()),
    path('authors/<int:pk>/posts/', AuthorPosts.as_view()),
    path('authors/posts/', AuthorsPosts.as_view()),
    path('categories/', CategoryList.as_view()),
    path('categories/create/', CategoryCreate.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),
    path('categories/<int:pk>/update/', CategoryUpdate.as_view()),
    path('categories/<int:pk>/delete/', CategoryDelete.as_view()),
    

]