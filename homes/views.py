from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post
# Create your views here.
def home(request): 
     return render(request, "home/home.html")




