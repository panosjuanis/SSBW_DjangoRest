from mongoengine import connect
import logging

connect('library', host='mongo')
print('Connected to book database')


logger = logging.getLogger(__name__)