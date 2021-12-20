from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="Green Blog 17")
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
      #  return reverse('article-detail', args=(str(self.id)))
      return reverse('home')
        # Siempre que algo es creado en nustro modelo, se le crea una id, y con eso referenciamos a donde tiene que ir la pagina luego de postear el post.