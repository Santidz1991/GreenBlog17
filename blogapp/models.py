from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="Agenda 2030 Blog")
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=80, default='general')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
      #  return reverse('article-detail', args=(str(self.id)))
      return reverse('home')
        # Siempre que algo es creado en nustro modelo, se le crea una id, y con eso referenciamos a donde tiene que ir la pagina luego de postear el post.