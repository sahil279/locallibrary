from django.shortcuts import render
from django.views import generic

# Create your views here.
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(Status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    name_genre= Genre.objects.count()

    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'name_genre': name_genre,
        'num_visits':num_visits,
    }


    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)

class BookListView(generic.ListView):
    model = Book
class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
class AuthorDetailView(generic.DetailView):
    model = Author
























# sessions code
