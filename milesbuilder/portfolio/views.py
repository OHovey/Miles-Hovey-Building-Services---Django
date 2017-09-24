from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Project, Image
from braces.views import SuperuserRequiredMixin
from .forms import ProjectForm, ImageForm
from django.urls import reverse_lazy

# Create your views here.

class ProjectList(ListView):

    model = Project

class ProjectDetail(DetailView):

    model = Project

class ProjectCreate(SuperuserRequiredMixin, CreateView):

    form_class = ProjectForm
    model = Project

    success_url = reverse_lazy('portfolio:all')

class ImageCreate(SuperuserRequiredMixin, CreateView):

    form_class = ImageForm
    model = Image

    success_url = reverse_lazy('portfolio:all')

class ProjectDelete(SuperuserRequiredMixin, DeleteView):

    model = Project
    success_url = reverse_lazy('portfolio:all')