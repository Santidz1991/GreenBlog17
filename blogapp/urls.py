from django.urls import path
# from . import views
from .views import AddPostView, HomeView, ArticleDetailView


urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'), 
    path('addpost/', AddPostView.as_view(), name='addpost'),
]
# pk = primary key Asi podemos identificar el numero unico del post