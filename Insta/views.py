from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from Insta.models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from Insta.forms import CustomUserCreationForm

class HelloWorld(TemplateView):
    template_name = 'test.html'

class PostsView(ListView):
    model = Post
    template_name = 'post_all.html'

class PostsDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Post
    template_name = 'post_detail.html'

#继承类前后顺序有关系
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_create.html"
    #当你去create一个view的时候，你希望用户提供什么field
    fields = '__all__'
    #如果点击createView时候没有login的话，跳转到login的url
    login_url = 'login'

class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ['title']

class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Post
    template_name = "post_delete.html"
    #不能一边执行delete，一边又开始跳转了，所以要使用reverse_lazy
    success_url = reverse_lazy('posts')

class SignUp(CreateView):
    #我应该用一个什么样的表格？这里用UserCreationForm
    #form_class = UserCreationForm
    #Customize自己的user model后就使用自己的user model
    form_class = CustomUserCreationForm
    template_name = "sign_up.html"
    success_url = reverse_lazy('login')