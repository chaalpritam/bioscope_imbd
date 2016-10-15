from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import flim

class HomeView(ListView):
     model = flim
     queryset = flim.objects.order_by('-created_by')[:9]
     template_name = 'index.html'

def get_context_data(self, **kwargs):
    context = super(homeview,self).get_context_data(**kwargs)
    return context
