from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView



app_name = "blog"


urlpatterns = [
    #path("api/v1", include("blog.api.v1.urls")),
    path("fbvi", views.FunctionBaseViewIndex, name="fbv-index"),
    # manual templateview
    path("cbvi", views.C1assBaseViewIndex.as_view(), name="cbv-index"),
    # auto templateview
    path("cbtv", TemplateView.as_view(template_name="index.html", extra_context ={'whatever':'hello template view'})),
    path("redirect", views.RedirectToEveryWhere.as_view(), name="redirect"),
    path("post/", views.PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post/create/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/edit/", views.PostEditView.as_view(), name="post-edit"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),
]