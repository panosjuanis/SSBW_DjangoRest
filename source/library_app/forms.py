from django import forms


class SearchTitleForm(forms.Form):
    book_name = forms.CharField(label='Book title', max_length=100)


class BookDetailsForm(forms.Form):
    isbn = forms.CharField(label='ISBN', max_length=100)
    title = forms.CharField(label='Title', max_length=100)
    author = forms.CharField(label='Author', max_length=100)
    genre = forms.CharField(label='Genre', max_length=100)
    image = forms.URLField(label='Image', max_length=100)
    description = forms.CharField(label='Description', max_length=1000)
    published = forms.DateField(label='Published')
    publisher = forms.CharField(label='Publisher', max_length=100)
