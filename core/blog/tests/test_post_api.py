from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from datetime import datetime
from accounts.models import User
from ..models import Category


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email="test100@test.com", password="a/@1234567", is_verified=True
    )
    return user


@pytest.fixture
def common_category():
    category_obj = Category.objects.create(name = 'cat1')
    return category_obj


@pytest.mark.django_db
class TestPostApi:
    def test_get_post_response_200_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test95",
            "content": "description",
            "status": True,
            "published_date": datetime.now(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_post_response_201_status(self, api_client, common_user, common_category):
        url = reverse("blog:api-v1:post-list")
        user = common_user
        category = common_category
        data = {
            "title": "test96",
            "content": "description",
            "category":category,
            "status": True,
            "published_date": datetime.now()
        }
        # no difference between force_login and force_authenticate here
        # api_client.force_authenticate(user=user)
        api_client.force_login(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_post_invalid_data_response_400_status(
        self, api_client, common_user,
    ):
        url = reverse("blog:api-v1:post-list")
        data = {"title": "test97", "content": "description"}
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400
