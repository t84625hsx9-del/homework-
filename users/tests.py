from django.test import TestCase

class RegistrationTest(TestCase):
    def test_registration_page_status_code(self):
        # Просто заходим на корень сайта
        response = self.client.get('/') 
        self.assertEqual(response.status_code, 200)
