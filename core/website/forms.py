from django import forms
from website.models import Contact, Newsletter
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = "__all__"

    # def send_email(self):
    #     # send email using the self.cleaned_data dictionary
    #     pass


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = "__all__"
