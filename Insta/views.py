from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from Insta.models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

class HelloWorld(TemplateView):
    template_name = 'test.html'

class PostsView(ListView):
    model = Post
    template_name = 'post_all.html'

class PostsDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = "post_create.html"
    #当你去create一个view的时候，你希望用户提供什么field
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ['title']

class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    #不能一边执行delete，一边又开始跳转了，所以要使用reverse_lazy
    success_url = reverse_lazy('posts')