from mongoengine import connect

connect('library', host='mongo')
print('Connected to book database')