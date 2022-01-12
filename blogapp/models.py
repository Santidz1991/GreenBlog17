from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField 


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255, default="Agenda 2030 Blog")
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=80, default='general')
    snippet = models.CharField(max_length=80)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
      #  return reverse('article-detail', args=(str(self.id)))
      return reverse('home')
        # Siempre que algo es creado en nustro modelo, se le crea una id, y con eso referenciamos a donde tiene que ir la pagina luego de postear el post.