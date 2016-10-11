from django.shortcuts import render
from django.views.generic import ListView
from .models import Film
# Create your views here.

class HomeView(ListView):

    model=Film
    queryset=Film.objects.order_by('-created_date')[:9]
    template_name= 'index.html'

    def get_context_data(self,**kwargs):
        context=super(HomeView,self).get_context_data(**kwargs)
        return context
