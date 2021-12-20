from django.urls import path
# from . import views
from .views import AddPostView, HomeView, ArticleDetailView,objetivos1,objetivosfull,register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'), 
    path('addpost/', AddPostView.as_view(), name='addpost'),
    path('objetivos1/',objetivos1),
    path('objetivosFull/',objetivosfull),
    path('registro/',register,name='register'),
    path('ingresar/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='logout.html'),name='logout'),
]
# pk = primary key Asi podemos identificar el numero unico del post
