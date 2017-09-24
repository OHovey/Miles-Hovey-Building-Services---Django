from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy, reverse
from django.utils import timezone

from braces.views import SuperuserRequiredMixin

# Create your views here.


class PostCreate(SuperuserRequiredMixin, CreateView):

    
    

    form_class = PostForm
    model = Post

    success_url = reverse_lazy('blog:drafts')

class PostList(ListView):

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published__lte=timezone.now()).order_by('-published')

class DraftList(SuperuserRequiredMixin, ListView):

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published__isnull=True).order_by('-created')

class PostDetail(DetailView):

    model = Post

class PostUpdate(SuperuserRequiredMixin, UpdateView):

    model = Post
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    

class PostDelete(SuperuserRequiredMixin, DeleteView):

    model = Post
    success_url = reverse_lazy('blog:all')

def publish(request, pk):

    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:all')
