from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from blog.models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User


def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context)


class Home(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_created"]
    paginate_by = 5


class Postdetailview(DetailView):
    model = Post


class Postcreateview(LoginRequiredMixin, CreateView):
    model = Post
    feilds = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "blog_home"
    template_name = "blog/post_delete_confirm.html"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class Postupdateview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_post.html"
    context_object_name = "posts"

    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_created")


def about(request):
    return render(request, "blog/about.html")
# Create your views here.
