import datetime
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from Posts.models import Category, Author, Post

User = get_user_model()

def createUserWithToken(self):
    self.username = 'adminTest'
    self.password = 'admin'
    self.data = {
        'username': self.username,
        'password': self.password
    }
    url = reverse('token_obtain_pair')

    # Create a user
    user = User.objects.create_user(username='adminTest', password='admin')

    # Post to get token
    response = self.client.post(url, self.data, format='json')
    self.access_token = response.data["access"]
    self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

def createPostSetUp(self):
    # give access
        createUserWithToken(self)
        # Create author
        self.author = Author.objects.create(name='Author')
        self.author.save()

        # Create categories
        self.category0 = Category.objects.create(name='First Category')
        self.category1 = Category.objects.create(name='Second Category')
        self.category0.save()
        self.category1.save()

        # Create post
        self.post = Post.objects.create(title="New title"
                                        , sub_title="test sub title"
                                        , image_URL="https://pixabay.com/photos/corgi-dog-pet-canine-rain-animal-4415649/"
                                        , body="This is body content test"
                                        , author=self.author)
        
        self.post.categories.set([self.category0, self.category1])
        self.post.save()
class CreateAccessTokenTestCase(APITestCase):
    def setUp(self):
        self.username = 'adminTest'
        self.password = 'admin'
        self.data = {
            'username': self.username,
            'password': self.password
        }

    def test_details(self):
        url = reverse('token_obtain_pair')

        # Create a user
        user = User.objects.create_user(username='adminTest', password='admin')
        self.assertEqual(user.is_active, 1, 'Active User')

        # Post to get token
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)

# Posts
class PostListTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("listPosts")

    def test_details(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)
        self.assertEqual(response.data["results"], [])

class PostGetTestCase(APITestCase):
    def setUp(self):
        # Create author
        self.author = Author.objects.create(name='Author')
        self.author.save()

        # Create categories
        self.category0 = Category.objects.create(name='First Category')
        self.category1 = Category.objects.create(name='Second Category')
        self.category0.save()
        self.category1.save()

        # Create post
        self.post = Post.objects.create(title="New title"
                                        , sub_title="test sub title"
                                        , image_URL="https://pixabay.com/photos/corgi-dog-pet-canine-rain-animal-4415649/"
                                        , body="This is body content test"
                                        , author=self.author)
        
        self.post.categories.set([self.category0, self.category1])
        self.post.save()
        self.url = reverse("getPost", args=[self.post.id])

    def test_details(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        if status.is_success(response.status_code):
            response_data = response.data
             # Check if the response data matches the expected data
            fields_to_check = ['title', 'sub_title', 'image_URL', 'body']
            for field in fields_to_check:
                self.assertEqual(response_data[field], getattr(self.post, field))

            self.assertEqual(response_data['author'], self.post.author.id)
            expected_categories = [category.id for category in self.post.categories.all()]
            self.assertEqual(expected_categories, response_data['categories'])

class PostCreateTestCase(APITestCase):
    def setUp(self):
        createUserWithToken(self)

        # Create categories
        self.category0 = Category.objects.create(name='First Category')
        self.category1 = Category.objects.create(name='Second Category')
        self.category0.save()
        self.category1.save()

        # Create author
        self.author = Author.objects.create(name='Author')
        self.author.save()

    # Create post
    def test_details(self):
        payload = {
                "title": "New title",
                "sub_title": "test sub title",
                "image_URL": "https://pixabay.com/photos/corgi-dog-pet-canine-rain-animal-4415649/",
                "body": "This is body content test",
                "author": self.author.pk,
                "categories": [
                            self.category0.pk,
                            self.category1.pk
                        ]
            }
        response = self.client.post(reverse("createPost"), payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        if status.is_success(response.status_code):
            response_data = response.data
            for key, value in payload.items():
                assert response_data[key] == value

class PostUpdateTestCase(APITestCase):
    def setUp(self):
        createPostSetUp(self)
        self.url = reverse("updatePost", args=[self.post.id])

    def test_details(self):
        payload = {
                "title": "New title updated",
                "sub_title": "test sub title updated",
                "image_URL": "https://pixabay.com/photos/corgi-dog-pet-canine-rain-animal-4415649/",
                "body": "This is body content test updated",
                "author": self.author.pk,
                "categories": [
                            self.category0.pk,
                            self.category1.pk
                        ]
            }
        response = self.client.put(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if status.is_success(response.status_code):
            response_data = response.data
            for key, value in payload.items():
                assert response_data[key] == value
class PostDeleteTestCase(APITestCase):
    def setUp(self):
        createPostSetUp(self)
        self.url = reverse("deletePost", args=[self.post.id])
    
    def test_details(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

# Authors  
class AuthorListTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("listAuthors")

    def test_details(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)
        self.assertEqual(response.data["results"], [])

        # addind author
        self.author = Author.objects.create(name='Author')
        self.author.save()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

class AuthorGetTestCase(APITestCase):
    def setUp(self):
        # Create author
        self.author = Author.objects.create(name='Author')
        self.author.save()
        self.url = reverse("getAuthor", args=[self.author.id])

    def test_details(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if status.is_success(response.status_code):
            response_data = response.data
            self.assertEqual(response_data["id"], self.author.id)
            self.assertEqual(response_data["name"], self.author.name)

class AuthorCreateTestCase(APITestCase):
    def setUp(self):
        createUserWithToken(self)
    
    def test_details(self):
        payload = {
                        "name": "New Author",
                        "age": 30
                    }
        response = self.client.post(reverse("createAuthor"), payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], payload["name"])
        self.assertEqual(response.data["age"], payload["age"])

class AuthorUpdateTestCase(APITestCase):
    def setUp(self):
        # give access
        createUserWithToken(self)
        # Create author
        self.author = Author.objects.create(name='Author')
        self.author.save() 
        self.url = reverse("updateAuthor", args=[self.author.id])
    def test_details(self):
        payload = {
                "name": "Author updated"
            }
        response = self.client.put(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if status.is_success(response.status_code):
            self.assertEqual(response.data["name"], payload["name"])

class AuthorDeleteTestCase(APITestCase):
    def setUp(self):
        # give access
        createUserWithToken(self)
        # Create author
        self.author = Author.objects.create(name='Author')
        self.author.save()
        self.url = reverse("deleteAuthor", args=[self.author.id])

    def test_details(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class CategoriesListTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("listCategories")

    def test_details(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)
        self.assertEqual(response.data["results"], [])

        # addind categories
        self.category0 = Category.objects.create(name='First Category')
        self.category1 = Category.objects.create(name='Second Category')
        self.category0.save()
        self.category1.save()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)

class CategoryGetTestCase(APITestCase):
    def setUp(self):
        # Create category
        self.category = Category.objects.create(name='Category')
        self.category.save()
        self.url = reverse("getCategory", args=[self.category.id])

    def test_details(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if status.is_success(response.status_code):
            response_data = response.data
            self.assertEqual(response_data["id"], self.category.id)
            self.assertEqual(response_data["name"], self.category.name)

class CategoriesCreateTestCase(APITestCase):
    def setUp(self):
        createUserWithToken(self)
        
    def test_details(self):
        category0 = {
                        "name": "First Category"
                    }
        response = self.client.post(reverse("createCategory"), category0)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], category0["name"])

        category1 = {
                        "name": "Second Category"
                    }
        response = self.client.post(reverse("createCategory"), category1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], category1["name"])

class CategoryUpdateTestCase(APITestCase):
    def setUp(self):
        # give access
        createUserWithToken(self)
        # Create category
        self.category = Category.objects.create(name='Category')
        self.category.save() 
        self.url = reverse("updateCategory", args=[self.category.id])
    def test_details(self):
        payload = {
                "name": "Category updated"
            }
        response = self.client.put(self.url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if status.is_success(response.status_code):
            self.assertEqual(response.data["name"], payload["name"])

class CategoryDeleteTestCase(APITestCase):
    def setUp(self):
        # give access
        createUserWithToken(self)
        # Create category
        self.category = Category.objects.create(name='Category')
        self.category.save()
        self.url = reverse("deleteCategory", args=[self.category.id])

    def test_details(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)