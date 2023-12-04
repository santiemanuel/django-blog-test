from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from django.utils.text import slugify
# Create your models here.

# vamos ir cargando uno por uno los models para ver donde se encuentrar mi error

COLOR_CHOICES = (
    ('1', 'celeste'),
    ('2', 'beige'),
    ('3', 'salmon')
)

NAME_CHOICES = (
    ('1', 'nacional'),
    ('2', 'provincial'),
    ('3', 'municipal')
)

class Category(models.Model):
    name = models.CharField(max_length= 50)
    description = models.TextField()
    slug = models.SlugField(null=False, blank=False, unique=True)
    color = models.CharField(max_length=20, choices= COLOR_CHOICES, default= 'celeste')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

# create inline for postcategory in Post to select many categories


class Post(models.Model):
    STATUS_CHOICES = (
        ('1', "DRAFT"),
        ('2', "PUBLISHED"),
        ('3', "REMOVED"),
    )  

    title = models.CharField(max_length= 20, null=False)
    content = models.TextField(max_length= 100, null=False)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now = True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    status = models.CharField(choices=STATUS_CHOICES , default='DRAFT', max_length= 20)
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to="image", null = True, blank = True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'category')

    def __str__(self):
        return self.post.title + " - " + self.category.name

class Comment(models.Model):
    author = models.CharField(max_length= 20, null = False)
    content = models.TextField(null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add= True)
    comment_post = models.ForeignKey(Post, on_delete= models.CASCADE)

    def __str__(self):
        return self.author

