from django.test import TestCase
from datetime import datetime

from accounts.models import User, Profile
from ..models import Post


class TestPostModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="test60@test.com", password="a/@1234567"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="first_name_test",
            last_name="last_name_test",
            description="description_test",
        )

    def test_create_post_with_valid_data(self):
        post = Post.objects.create(
            author=self.profile,
            title="another test",
            content="description",
            status=True,
            category=None,
            published_date=datetime.now(),
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertEquals(post.title, "another test")
