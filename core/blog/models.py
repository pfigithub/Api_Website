from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    """this is a class to define posts for blog app"""

    author = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.id})


class Category(models.Model):
    """class for category"""

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
