from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve  # useful for testing urls
from .views import HomePageView,AboutPageView


class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get('/')

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there i should not be on the page')

    # resolve url
    def test_homepage_url_resolve_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AboutPagetest(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get('/')

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there i should not be on the page')

    # resolve url
    def test_aboutpage_url_resolve_aboutpageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )
