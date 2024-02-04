from django.shortcuts import render
from .models import Appliances 
from django.views.generic import ListView , DetailView

# Create your views here.
class Index(ListView):
    model = Appliances
    template_name = 'home/index.html'
    context_object_name = 'appliances'
    ordering = ['name']
    
class applianceDetail(DetailView):
    model = Appliances
    template_name = 'home/appliance_detail.html'
    context_object_name = 'appliance'
    
