from django.test import TestCase
from django.contrib.auth.models import User

class InventoryTestCase(TestCase):
    
    def setUp(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_inventory_view(self):
        response = self.client.get('/inventory')
        self.assertEqual(response.status_code, 200)

    def test_inventory_api(self):
        response = self.client.get('/api/inventory')
        self.assertEqual(response.status_code, 200)

    def test_inventory_api_id(self):
        response = self.client.get('/inventory/7')
        self.assertEqual(response.status_code, 200)
