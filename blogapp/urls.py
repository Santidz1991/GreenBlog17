from django.urls import path
from django.views.generic.base import TemplateView
# from . import views
from .views import AddPostView, HomeView, ArticleDetailView, UpdatePostView, DeletePostView, objetivosfull


urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'), 
    path('addpost/', AddPostView.as_view(), name='addpost'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='updatepost'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name='deletepost'),
    path('objetivos/full', objetivosfull.as_view(), name='objetivosFull'),
    ]
 
# pk = primary key Asi podemos identificar el numero unico del post