from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
'''
def home(request):
    return render(request, 'home.html', {})
'''

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'addpost.html'
    fields = '__all__'
    # fields = ('title', 'body')

def objetivos1(request):
    return render(request,'inicio.html',{})

def objetivosfull(request):
    return render(request,'objetivosfull.html',{})

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
    else:
        form=UserCreationForm()
    context={'form':form}       
    
    return render(request,'singIn.html',context)