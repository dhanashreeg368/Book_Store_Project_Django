from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import Permission

from .models import Book, Review


class BookTests(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title='Oka_book',
            author='sharif',
            price='25.00',
        )
        self.special_permission = Permission.objects.get(codename='special_status')
        self.book = Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='25.00',
        )
        self.review = Review.objects.create(
            book=self.book,
            author=self.user,
            review='An excellent review',
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Oka_book')
        self.assertEqual(f'{self.book.author}', 'sharif')
        self.assertEqual(f'{self.book.price}', '25.00')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Oka book')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_resonse = self.client.get('/book/1234/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_resonse.status_code, 400)
        self.assertNotContains(response, 'Oka book')
        self.assertContains(response, 'I enjoed')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_list_view_for_logged_in_user(self):
        self.client.login(email='sharif@email.com', password='1')
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_list_view_for_logged_out_user(self):  # new
        self.client.logout()

        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '%s?next=/books/' % (reverse('account_login')))
        response = self.client.get(
            '%s?next=/books/' % (reverse('account_login')))
        self.assertContains(response, 'Log In')
