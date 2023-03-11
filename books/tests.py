from django.test import TestCase
from django.urls import reverse

from books.models import Book


# Create your tests here.

class BooksTestCase(TestCase):
    def test_no_books(self):
        response=self.client.get(reverse('books:Listview'))

        self.assertContains(response,'No books found.')

    def test_bookd_list(self):
        Book.objects.create(title='test1',description='test1',isbn='123456789')
        Book.objects.create(title='test2',description='test2',isbn='223456789')
        Book.objects.create(title='test3',description='test3',isbn='323456789')

        response=self.client.get(reverse('books:Listview'))

        books=Book.objects.all()

        for book in books:
            self.assertContains(response,book.title)

    def test_details_book(self):
        book=Book.objects.create(title='test1', description='test1', isbn='123456789')
        respone=self.client.get(reverse('books:DetailView',kwargs={'pk':book.id}))

        self.assertContains(respone,book.title)





