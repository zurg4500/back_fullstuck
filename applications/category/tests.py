from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse

from .models import Category
from django.contrib.auth import get_user_model

from utils.utils import get_tokens_for_user


User = get_user_model()

class CategoryTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        user = User.objects.create(
            username='testuser',
            password='testpassword123',
            email='test@test.com',
            is_active=True
        )
        admin = User.objects.create_superuser(
            username='testadmin',
            password='testpassword123',
            email='admin@test.com',
        )

        Category.objects.create(title='testcategory')

        self.user_token = get_tokens_for_user(user)
        self.admin_token = get_tokens_for_user(admin)

        self.url = reverse('category-list')
        self.detail_url = reverse('category-detail', ['testcategory'])
        "category/testcategory"
    
    def test_get_categories(self): # "/category/"
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_category_as_anon(self):
        response = self.client.post(self.url, {"title": "Игрушки"})
        self.assertEqual(response.status_code, 401)

    def test_create_category_as_user(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.user_token['access'])
        response = self.client.post(self.url, {'title': 'Mashinki'})
        self.assertEqual(response.status_code, 403)

    def test_create_category_as_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.admin_token['access'])
        response = self.client.post(self.url, {'title': 'Mashinki'})
        self.assertEqual(response.status_code, 201)
    
    def test_admin_can_update(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.admin_token['access'])
        response = self.client.patch(self.detail_url, {"title": "New title"}) 
        self.assertEqual(response.status_code, 200)
