from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    class BookTypes(models.IntegerChoices):
        HARDCOVER = 1, _('Hardcover')
        PAPERBACK = 2, _('Paperback')
        EBOOK = 3, _("E-book")

    title = models.CharField(max_length=50)
    publication_date = models.DateField(blank=True, null=True)
    author = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.PositiveSmallIntegerField(choices=BookTypes.choices, blank=True, null=True)


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    bio = models.TextField()
    website = models.URLField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField()
    borrower = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a', help_text='Book availability')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.book.title} ({self.id})'