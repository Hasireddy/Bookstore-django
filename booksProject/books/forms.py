from django.forms import ModelForm

from django import forms

from .models import Book


class EditBookForm(ModelForm):
    
    model = Book
    fields = '__all__'
    
    widgets = {
             'title': forms.TextInput(attrs={'class': 'form-control'}),
             'author': forms.TextInput(attrs={'class': 'form-control'}),
             'price': forms.TextInput(attrs={'class': 'form-control'}),
             'isbn': forms.TextInput(attrs={'class': 'form-control'}),
             'image': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
