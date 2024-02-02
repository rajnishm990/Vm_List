from django.shortcuts import render
from .models import Appliances 
from django.views.generic import ListView

# Create your views here.
class Index(ListView):
    model = Appliances
    template_name = 'home/index.html'
    context_object_name = 'appliances'
    ordering = ['name']
    

