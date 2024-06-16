from django.db import models

from open_library.utility import generate_isbn


class Library(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class Member(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_of_membership = models.DateTimeField(auto_now=True)
    number_of_books_borrowed = models.IntegerField(default=0)
    max_book_limit = models.IntegerField(default=3)
    address = models.CharField(max_length=255)
    is_signed_up = models.BooleanField(default=False)
    library = models.ForeignKey(Library, related_name='members', on_delete=models.CASCADE)


class Author(Member):
    biograph = models.TextField()


class Book(models.Model):
    STATUS = [("B", "BORROW"), ("NOT_AV", "NOT_AVAILABLE")]
    title = models.CharField(max_length=255)
    year_published = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=6, choices=STATUS, default="B")
    ISBN = models.CharField(max_length=13, unique=True, default=generate_isbn)
    date_borrowed = models.DateTimeField(null=True, blank=True)
    borrower = models.ForeignKey(Member, null=True, blank=True, related_name='borrowed_books',
                                 on_delete=models.SET_NULL)
    library = models.ForeignKey(Library, related_name='books', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Librarian(Member):
    pass
