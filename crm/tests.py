from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Client

class ClientTests(APITestCase):
    def test_create_client(self):
        url = reverse('client-list')
        data = {'first_name': 'John', 'last_name': 'Doe', 'phone_number': '1234567890', 'email': 'john.doe@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.get().first_name, 'John')