from django import forms

from app.models import Contact


class NumberForm(forms.Form):
    username = forms.CharField(label="username", required=True, max_length=10)
    number = forms.IntegerField(label="number", required=True)


class CarForm(forms.Form):
    style = forms.CharField(label="style", required=False, max_length=10)
    manufacturer = forms.CharField(label="manufacturer", required=False, max_length=10)
    model = forms.CharField(label="model", required=False, max_length=20)
    engine_cc = forms.IntegerField(label="engine_cc", required=False)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }