from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import ExpenseIncome

class ExpenseTrackerTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='pass123')
        self.user2 = User.objects.create_user(username='user2', password='pass123')
        self.admin = User.objects.create_superuser(username='admin', password='admin123')
        
        self.expense1 = ExpenseIncome.objects.create(
            user=self.user1,
            title="Lunch",
            amount=15.00,
            transaction_type="debit",
            tax=2.00,
            tax_type="flat"
        )
        
    def test_user_registration(self):
        url = reverse('register')
        data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'newpass123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        
    def test_expense_creation(self):
        self.client.force_authenticate(user=self.user1)
        url = reverse('expenses-list')
        data = {
            'title': 'Dinner',
            'amount': '25.00',
            'transaction_type': 'debit',
            'tax': '3.00',
            'tax_type': 'flat'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        
    def test_tax_calculation_flat(self):
        self.assertEqual(self.expense1.total, 17.0)
        
    def test_user_cant_see_others_expenses(self):
        self.client.force_authenticate(user=self.user2)
        url = reverse('expenses-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 0)