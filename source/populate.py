import json, requests, argparse
from datetime import datetime

from mongoengine import connect, Document, EmbeddedDocument	
from mongoengine.fields import Document, StringField, ListField, IntField, DateTimeField, URLField
from datetime import datetime


# Define book class
class Book(Document):
    id = IntField(required=True,primary_key=True)
    title = StringField(required=True)
    author = StringField(required=True)
    genre = StringField(required=True)
    description = StringField(required=True)
    isbn = StringField(required=True)
    image = URLField(required=True)
    published = DateTimeField(required=True)
    publisher = StringField(required=True)

    meta = {'collection': 'books'}


if __name__ == "__main__":
    # Connect to mongodb repo
    print('Connecting to mongodb repo...')
    connect('library', host='mongo')


    # Get data from fakerapi and save it to mongodb
    print('Retrieving data from fakerapi.it...')
    response = requests.get('https://fakerapi.it/api/v1/books?_quantity=50')
    data = response.json()
    books = []
    for libro in data['data']:
        newBook = Book(
            title=libro['title'],
            author=libro['author'],
            genre=libro['genre'],
            description=libro['description'],
            isbn=libro['isbn'],
            published=libro['published'],
            publisher=libro['publisher']
        )
        books.append(newBook)

    print('Saving data to mongodb...')
    Book.objects.insert(books, load_bulk=True)