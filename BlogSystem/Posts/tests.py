from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from Posts.models import Category, Author

User = get_user_model()
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

class PostListTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("listPosts")

    def test_details(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)
        self.assertEqual(response.data["results"], [])


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

class AuthorCreateTestCase(APITestCase):
    def setUp(self):
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
    
    def test_details(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        payload = {
                        "name": "New Author",
                        "age": 30
                    }
        response = self.client.post(reverse("createAuthor"), payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], payload["name"])
        self.assertEqual(response.data["age"], payload["age"])

    


class CategoriesCreateTestCase(APITestCase):
    def setUp(self):
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
        
    def test_details(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
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


class PostCreateTestCase(APITestCase):
    def setUp(self):
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
