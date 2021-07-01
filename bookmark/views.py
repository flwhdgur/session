from typing import List
from django.shortcuts import render
from .models import bookmark
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy


class bookmarkListView(ListView):
    model = bookmark

class bookmarkCreateView(CreateView):
    model = bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = "_create"

class bookmarkDetailView(DetailView):
    model = bookmark