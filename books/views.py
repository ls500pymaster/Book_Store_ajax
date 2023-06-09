from django.core.exceptions import ValidationError
from django.core.mail import send_mail, BadHeaderError
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import FormView

from books.models import Book, Author
from books.forms import BookForm, ContactForm, AuthorForm


def home(request):
    return render(request, "books/home.html")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send email
            return JsonResponse({'success': True})
        else:
            return render(request, 'books/contact.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'books/contact.html', {'form': form})


def contact_success(request):
    return render(request, "books/success.html")


def author_list(request):
    authors = Author.objects.all()
    return render(request, "books/author_list.html", {"authors": authors})


def author_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
    else:
        form = AuthorForm()
    return save_author_form(request, form, "books/partial_author_create.html")


def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
    else:
        form = AuthorForm(instance=author)
    return save_author_form(request, form, "books/partial_author_update.html")


def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    data = dict()
    if request.method == 'POST':
        author.delete()
        data['form_is_valid'] = True
        authors = Author.objects.all()
        data['html_author_list'] = render_to_string('books/partial_author_list.html', {
            'authors': authors
        })
    else:
        context = {'author': author}
        data['html_form'] = render_to_string('books/partial_author_delete.html', context, request=request)
    return JsonResponse(data)


def save_author_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            authors = Author.objects.all()
            data['html_author_list'] = render_to_string('books/partial_author_list.html', {
                'authors': authors
            })
            context = {'form': form}
            data['html_form'] = render_to_string(template_name, context, request=request)
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


############ books ################

# def contact_main(request):
#     return render(request, 'books/contact.html')


def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()
    return save_contact_form(request, form, "books/partial_contact_form.html")


def save_contact_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = Book.objects.all()
            data['html_book_list'] = render_to_string('books/contact.html', {
                'books': books
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def save_book_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = Book.objects.all()
            data['html_book_list'] = render_to_string('books/partial_book_list.html', {
                'books': books
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
    else:
        form = BookForm()
    return save_book_form(request, form, 'books/partial_book_create.html')


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
    else:
        form = BookForm(instance=book)
    return save_book_form(request, form, 'books/partial_book_update.html')


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    data = dict()
    if request.method == 'POST':
        book.delete()
        data['form_is_valid'] = True
        books = Book.objects.all()
        data['html_book_list'] = render_to_string('books/partial_book_list.html', {
            'books': books
        })
    else:
        context = {'book': book}
        data['html_form'] = render_to_string('books/partial_book_delete.html', context, request=request)
    return JsonResponse(data)
