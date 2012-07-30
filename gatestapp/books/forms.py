
from django.forms import ModelForm
from models import Author, Book, Publisher

class AuthorForm(ModelForm):
    class Meta:
        model = Author

class BookForm(ModelForm):
    class Meta:
        model = Book

class PublisherForm(ModelForm):
    class Meta:
        model = Publisher

