from django.test import TestCase
from views import home_page

from django.urls import resolve
from django.http import HttpRequest


class HomePageTest(TestCase):

    def test_url_resolve(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_view(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
