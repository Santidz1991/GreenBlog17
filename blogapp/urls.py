from django.urls import path
from django.views.generic.base import TemplateView
from .views import AddPostView, HomeView, ArticleDetailView, UpdatePostView, DeletePostView, AddCategoryView , TemplateView
from blogapp.views import MyView


urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'), 
    path('add_post/', AddPostView.as_view(), name='addpost'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='updatepost'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name='deletepost'),
    path('objetivos/', MyView.as_view(), name='objetivosfull'),
    ]
 
# pk = primary key Asi podemos identificar el numero unico del post