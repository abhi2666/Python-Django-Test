# hello/test_views.py
from django.urls import reverse
from django.test import TestCase

class HelloWorldViewTests(TestCase):
    def test_hello_world_view(self):
        response = self.client.get(reverse('hello_world'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, World!")
