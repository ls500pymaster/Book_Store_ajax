from django import forms

from books.models import Book, Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'bio', 'age', 'website')



class BookForm(forms.ModelForm):
    publication_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    book_type = forms.ChoiceField(
        required=False,
        choices=[('', '----'), ] + Book.BookTypes.choices,
        widget=forms.Select(attrs={'class': "custom-select"}),
    )

    class Meta:
        model = Book
        fields = ('title', 'publication_date', 'author', 'price', 'pages', 'book_type', )


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
