
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Post
from django.urls import reverse_lazy


class IndexView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'


class PostCreateView(CreateView):
    model = Post
    template_name = "post/post_create.html"
    fields = ['title', 'content']
    success_url = reverse_lazy('post:index')


class PostDetailView(DetailView):
    model = Post
    template_name = "post/post_detail.html"


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post/post_delete.html"
    success_url = reverse_lazy('post:index')


class PostUpdateView(UpdateView):
    model = Post
    template_name = "post/post_update.html"
    fields = ['title', 'content']
    success_url = reverse_lazy('post:index')
