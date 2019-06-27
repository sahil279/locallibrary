from django.db import models
from django.urls import reverse
import uuid




# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length = 200,help_text = 'enter a book genre (for eg a science fiction)')


    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)





    author = models.ForeignKey('AUTHOR', on_delete=models.SET_NULL,null=True)
    summary = models.TextField(max_length=1000,help_text="write a brief discussion of the book")
    genre = models.ManyToManyField(Genre,help_text='select a genre of this book')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail',args = [str(self.id)])
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Unique ID for this particular book across whole library ')
    book = models.ForeignKey('Book',on_delete=models.SET_NULL,null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True,blank=True)
    LOAN_STATUS = (
    ('m','Maintainance'),
    ('o','On Loan'),
    ('r','Reserved'),
    ('a','available'),
    )

    Status = models.CharField(
    max_length=1,
    choices= LOAN_STATUS,
    blank=True,
    default='m',
    help_text = "Book availabilty",

    )

    class Meta:
        ordering = ['due_back']
    def __str__(self):
        return f'{self.id}({self.book.title})'
class Language(models.Model):


    name = models.CharField(max_length=200,help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True,blank = True)
    date_of_death = models.DateField(null=True,blank=True)

    class Meta:
        ordering = ['last_name','first_name']


    def get_absolute_url(self):
        return reverse('author-detail',args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name},{self.first_name}'
