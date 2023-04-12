# BlogPosts_RESTful_API using django and postgres
# Deployed on "render" with link: https://myblogpost-hrfs.onrender.com


Models
    A Post contains the following properties:
        •	Author: One to Many
        •	Title
        •	Subtitle
        •	ImageUrl: useing external links
        •	Body
        •	Categories: Many to Many
        •	Created_at
        •	Updated_at
        
    An Author contains the following properties:
        •	Name
        •	Age
        •	Created_at
        •	Updated_at
        
    A Category contains the following properties:
        •	Name
        •	Created_at
        •	Updated_at
  
  
APIs:
RESTful API to perform the following actions:
    Tokens
        •	Get auth token.
        •	Refresh auth token.
        
    Posts
        •	Listing blog posts (public api)
        •	Getting a single blog post (public api)
        •	Adding a blog post (protected)
        •	Deleting a blog post (protected)
        •	Updating a blog post (protected)
        
    Authors
        •	Listing authors (public api)
        •	Listing authors blogs (public api)
        •	Getting an author (public api)
        •	Getting an author blogs (public api)
        •	Adding an author (protected)
        •	Updating an author (protected)
        •	Deleting an author (protected)
        
    Categories
        •	Listing categories (public api)
        •	Getting a category (public api)
        •	Adding a category (protected)
        •	Updating a category (protected)
        •	Deleting a category (protected)
        
Unit tests:
Added unit tests for:
    • Create Access Token Test Case
    • Post List Test Case
    • Author List Test Case
    • Categories List Test Case
    • Author Create Test Case
    • Categories Create Test Case
    • Post Create Test Case


