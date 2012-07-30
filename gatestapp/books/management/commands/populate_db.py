
from django.core.management.base import BaseCommand, CommandError

from gatestapp.books.models import Publisher, Author, Book

from datetime import datetime
import random
from random import choice, sample

import pdb

class Command(BaseCommand):
    args = '< none >'
    help = """
        Populates the database with a bunch of foo data
        for demonstrative purposes
    """
    
    domains = ('example.com', 'domain.com', 'myemail.com',
               'good.net', 'about.me', 'testing.app', 'zone.it',
               'business.biz', 'gman.gov',)
    
    def getrnd(self, rmin=0, rmax=500):
        return random.randint(rmin, rmax)
    
    def delete_all(self):
        Book.objects.all().delete()
        Author.objects.all().delete()
        Publisher.objects.all().delete()
    
    
    def generate_publishers(self, num=20):
        publishers = []
        
        for i in range(0, num):
            if i > 0 and i % 10 == 0:
                print 'Generated %d publishers so far...' % i
            
            p = Publisher.objects.create(name = 'Publisher %d' % self.getrnd(),
                                     address= '%d main street' % self.getrnd(),
                                     city='Anytown',
                                     state_province='AA',
                                     country='C',
                                     website='website.com')
            
            publishers.append(p)
            
        return publishers
    
    def generate_authors(self, num=20):
        authors = []
        
        for i in range(0, num):
            if i > 0 and i % 10 == 0:
                print 'Generated %d authors so far...' % i
            
            rnd = self.getrnd()
            if rnd % 2 == 0:
                fname = 'Guy'
            else:
                fname = 'Girl'
            
            lname = str(rnd)
            a = Author.objects.create(first_name=fname,
                                      last_name=lname,
                                      email=fname + lname + '@' + choice(self.domains))
            authors.append(a)
            
            
        return authors
    
    def generate_books(self, theauthors, publishers, num=20, authormin=1, authormax=4):
        books = []
        for i in range(0, num):
            if i > 0 and i % 10 == 0:
                print 'Generated %d authors so far...' % i
            
            title = 'Book title %d' % self.getrnd()
            
            publisher = choice(publishers)
            book_authors = sample(theauthors, random.randint(authormin, authormax))
            
            book = Book.objects.create(title=title,
                                       publisher=publisher,
                                       publication_date=datetime.now().today())
            book.authors = book_authors
            book.save()
            
            books.append(book)
            
        return books
    
    def handle(self, *args, **options):
        rmin = 0
        rmax = 500
        
        num_publishers = 25
        num_authors = 50
        num_books = 10
        
        print 'deleting all model instances...'
        self.delete_all()
        
        print 'generating %d publishers...' % num_publishers
        publishers = self.generate_publishers(num_publishers)
        
        print 'generating %d authors...' % num_authors
        authors = self.generate_authors(num_authors)
        
        print 'generating %d books...' % num_books
        books = self.generate_books(authors, publishers, num=num_authors)
        
        
        print 'finsihed - added %d publishers, %d books and %d authors' % (len(publishers), len(books), len(authors),)


