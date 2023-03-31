from django.test import TestCase

class TestPageStatus(TestCase):

    def test_home_status_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_aboutus_status_page(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)

    def test_login_status_page(self):
        response = self.client.get('/auth/login')
        self.assertEqual(response.status_code, 200)

    def test_registration_status_page(self):
        response = self.client.get('/auth/registration')
        self.assertEqual(response.status_code, 200)
