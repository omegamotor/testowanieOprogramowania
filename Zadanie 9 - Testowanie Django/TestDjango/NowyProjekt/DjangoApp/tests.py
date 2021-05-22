from django.template.loader import render_to_string
from django.test import TestCase
from DjangoApp.views import home_page
from django.urls import resolve





class HomePageTest(TestCase):

    def test_url_resolve(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_view(self):
        response = self.client.get('http://localhost:8000')
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Lista rzeczy do zrobienia</title>', html)
        self.assertTrue(html.endswith('</html>'))
        self.assertTemplateUsed(response, 'DjangoApp/home.html')

    def test_post(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())