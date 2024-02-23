# this only is for instance

from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime

from accounts.models import User, Profile
from blog.models import Post


class TestBlogview(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email="test70@test.com", password="a/@1234567"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="first_name_test",
            last_name="last_name_test",
            description="description_test",
        )
        self.post = Post.objects.create(
            author=self.profile,
            title="test75",
            content="description",
            status=True,
            category=None,
            published_date=datetime.now(),
        )

    def test_blog_index_url_successful_response(self):
        url = reverse("blog:post-list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        # self.assertTrue(str(response.content).find("something"))
        # self.assertTemplateUsed(response, template_name="a template name")

    def test_blog_post_detail_logged_in_response(self):
        self.client.force_login(self.user)
        url = reverse("blog:post-detail", kwargs={"pk": self.post.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_blog_post_detail_anonymouse_response(self):
        url = reverse("blog:post-detail", kwargs={"pk": self.post.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)
