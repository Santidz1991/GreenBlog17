from django.urls import path
# from . import views
from .views import AddPostView, HomeView, ArticleDetailView, UpdatePostView, DeletePostView


urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'), 
    path('addpost/', AddPostView.as_view(), name='addpost'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='updatepost'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name='deletepost'),
]
# pk = primary key Asi podemos identificar el numero unico del post