from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name  

class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=150)
    image_URL = models.CharField(max_length=300)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                                 null=True, related_name="book_authors")
    categories = models.ManyToManyField(Category, related_name="book_categories")

    def __str__(self):
        return self.title
