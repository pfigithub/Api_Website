from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from .forms import PostForm


# Create your views here.


# simple showing function base view
def FunctionBaseViewIndex(request):
    """a function based view to show index page"""

    whatever = "hello function base"
    context = {"whatever": whatever}
    return render(request, "index.html", context)


# cbv simple show for templateview
class C1assBaseViewIndex(TemplateView):
    """a class based view to show index page"""

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["whatever"] = "hello class base"
        return context


# cbv for redirect
class RedirectToEveryWhere(RedirectView):
    """redirection view sample for varzesh3"""

    url = "https://varzesh3.com"

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)


# cbv post list
class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 2
    ordering = "-published_date"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["now"] = timezone.now()
    #     return context


# cbv post detail
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    # context_object_name = "post"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["now"] = timezone.now()
    #     return context


# create post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields list or form class
    # form_class = PostForm
    fields = ["title", "content", "status", "category", "published_date"]

    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# edit post
class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "image", "content", "status", "category", "published_date"]
    # or like next line if we have forms and model form
    # form_class = model form name
    success_url = "/blog/post/"


# delete post
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/post/"
