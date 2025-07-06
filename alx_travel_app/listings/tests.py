from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Listing

# Create your tests here.

class ListingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testhost',
            email='test@example.com',
            password='testpass123'
        )
        
    def test_listing_creation(self):
        listing = Listing.objects.create(
            title='Test Listing',
            description='A test listing',
            price_per_night=100.00,
            location='Test City',
            host=self.user
        )
        self.assertEqual(listing.title, 'Test Listing')
        self.assertEqual(listing.host, self.user)
        self.assertEqual(str(listing), 'Test Listing')

class HealthCheckAPITest(APITestCase):
    def test_health_check_endpoint(self):
        url = reverse('health_check')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'healthy')
        self.assertIn('message', response.data)
