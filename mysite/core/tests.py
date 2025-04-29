from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class LoginPageTests(TestCase):
    
    def test_login_page_status(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
    
    def test_login_template_used(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login.html')