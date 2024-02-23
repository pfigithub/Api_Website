from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        # cbv-index means class base view index page
        return ["web:cbv-index", "web:about", "web:contact"]

    def location(self, item):
        return reverse(item)
