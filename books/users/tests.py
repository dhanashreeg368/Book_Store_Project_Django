from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
# from .views import SignupPageView


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        # creating user
        user = User.objects.create_user(
            username='will',
            email='will@gmail.com',
            password='testpass123'
        )
        # verifying user
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@gmail.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        # creating user
        admin_user = User.objects.create_superuser(
            username='forhad',
            email='forhad@gmail.com',
            password='forhard123'
        )
        # verifying user
        self.assertEqual(admin_user.username, 'forhad')
        self.assertEqual(admin_user.email, 'forhad@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

#
# class SignupPagetests(TestCase):
#     def setUp(self):
#         url = reverse('signup')
#         self.response = self.client.get(url)
#
#     def test_signup_template(self):
#         self.assertEqual(self.response.status_code, 200)
#         self.assertTemplateUsed(self.response, 'signup.html')
#         self.assertContains(self.response, 'Sign Up')
#         self.assertNotContains(self.response, 'Hi there i should not be on the page')
#
#     def test_signup_form(self):
#         form = self.response.context.get('form')
#         self.assertIsInstance(form, CustomUserCreationForm)
#         self.assertContains(self.response, 'csrfmiddlewaretoken')
#
#     def test_signup_view(self):
#         view = resolve('/accounts/signup/')
#         self.assertEqual(
#             view.func.__name__,
#             SignupPageView.as_view().__name__
#         )


class SignupTests(TestCase):
    username = 'sharif'
    email = 'sharif@gmail.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)

        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email)

        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
                         [0].email, self.email)