from django.urls import path
from Posts.views import PostList, PostCreate, PostDetail, PostUpdate, PostDelete,\
    AuthorList, AuthorDetail, AuthorCreate, AuthorUpdate, AuthorDelete, AuthorPosts, AuthorsPosts, \
        CategoryList, CategoryCreate, CategoryDetail, CategoryUpdate, CategoryDelete

urlpatterns = [
    path('', PostList.as_view(), name="listPosts"),
    path('create/', PostCreate.as_view(), name="createPost"),
    path('<int:pk>/', PostDetail.as_view(), name="getPost"),
    path('<int:pk>/update/', PostUpdate.as_view(), name="updatePost"),
    path('<int:pk>/delete/', PostDelete.as_view(), name="deletePost"),

    path('authors/', AuthorList.as_view(), name="listAuthors"),
    path('authors/create/', AuthorCreate.as_view(), name="createAuthor"),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name="getAuthor"),
    path('authors/<int:pk>/update/', AuthorUpdate.as_view(), name="updateAuthor"),
    path('authors/<int:pk>/delete/', AuthorDelete.as_view(), name="deleteAuthor"),
    path('authors/<int:pk>/posts/', AuthorPosts.as_view(), name="getAuthorPosts"),
    path('authors/posts/', AuthorsPosts.as_view(), name="getAuthorsPosts"),

    path('categories/', CategoryList.as_view(), name="listCategories"),
    path('categories/create/', CategoryCreate.as_view(), name="createCategory"),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name="getCategory"),
    path('categories/<int:pk>/update/', CategoryUpdate.as_view(), name="updateCategory"),
    path('categories/<int:pk>/delete/', CategoryDelete.as_view(), name="deleteCategory"),
    

]