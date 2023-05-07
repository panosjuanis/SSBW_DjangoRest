from django.utils import timezone

from mongoengine import connect, Document, EmbeddedDocument	
from mongoengine.fields import Document, StringField, ListField, IntField, DateTimeField, URLField

    
# Define book class
class Book(Document):
    title = StringField(required=True)
    author = StringField(required=True)
    genre = StringField(required=True)
    description = StringField(required=True)
    isbn = StringField(required=True)
    image = URLField(required=True)
    published = DateTimeField(required=True)
    publisher = StringField(required=True)

    meta = {'collection': 'books'}