import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.conf import settings


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def user_data():
    return {
        "username": "testuser",
        "password": "test12345",
        "email": "test@test.com"
    }


@pytest.fixture
def user(db, user_data):
    return User.objects.create_user(
        username=user_data["username"],
        password=user_data["password"],
        email=user_data["email"]
    )
