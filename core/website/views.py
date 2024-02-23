from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from website.forms import ContactForm, NewsletterForm
from .models import Contact, Newsletter
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView, CreateView


# simple showing function base view
def FunctionBaseViewIndex(request):
    """a function based view to show index page"""

    whatever = "hello function base"
    context = {"whatever": whatever}
    return render(request, "web/index.html", context)


# cbv simple show for templateview
class C1assBaseViewIndex(TemplateView):
    """a class based view to show index page"""

    template_name = "web/index.html"

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


# fbv for maintenance page
def maintenance_view(request):
    return render(request, "web/maintenance.html")


# fbv for about page
# def about(req):
#     return render(req, 'web/about.html')


# cbv for about page
class AboutView(TemplateView):
    template_name = "web/about.html"


# fbv for contact
# def contact(req):
#     if req.method == 'POST':
#         form = ContactForm(req.POST)
#         if form.is_valid():
#             form.save()
#             messages.add_message(req, messages.SUCCESS, 'your ticket submitted successfully')
#         else:
#             messages.add_message(req, messages.ERROR, 'your ticket did not submitted')
#     form = ContactForm()
#     return render(req, 'web/contact.html', {'form':form})


# cbv for contact
class ContactFormView(FormView):
    model = Contact
    template_name = "web/contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        return super().form_valid(form)


# fbv newsletter
def newsletter_view(req):
    if req.method == "POST":
        form = NewsletterForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")
