from django.shortcuts import render
from django.views.generic import ListView, DetailView
import models

class NewsListView(ListView):
    model = models.News

class NewsDetailView(DetailView):
    model = models.News

# Create your views here.
