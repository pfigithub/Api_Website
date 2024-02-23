from website.views import *
from django.urls import path

app_name = "web"

urlpatterns = [
    path("fbvi/", FunctionBaseViewIndex, name="fbv-index"),
    # manual templateview
    path("cbvi/", C1assBaseViewIndex.as_view(), name="cbv-index"),
    # auto templateview
    path(
        "cbtv/",
        TemplateView.as_view(
            template_name="web/index.html",
            extra_context={"whatever": "hello template view"},
        ),
    ),
    # cbv for contact page
    path("contact/", ContactFormView.as_view(), name="contact"),
    # fbv for contact page
    # path('contact/', contact, name = 'contact'),
    # url for cbv
    path("about/", AboutView.as_view(), name="about"),
    # url for fbv
    # path("about/", about, name = 'about'),
    path("newsletter/", newsletter_view, name="newsletter"),
    path("redirect/", RedirectToEveryWhere.as_view(), name="redirect"),
]
