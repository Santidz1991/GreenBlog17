from django.urls import path
from .views import AddPostView, HomeView, ArticleDetailView, UpdatePostView, DeletePostView, AddCategoryView , CategoryView, CategoryListView, LikeView
from . import views


urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'), 
    path('add_post/', AddPostView.as_view(), name='addpost'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='updatepost'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name='deletepost'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'), 
    path('objetivos/', views.ObjetivosView, name='objetivos'),
    
    ]
 
# pk = primary key Asi podemos identificar el numero unico del post