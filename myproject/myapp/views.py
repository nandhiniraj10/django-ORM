from django.http import HttpResponse
from myapp.models import Author, Book
from django.db.models import Count, Avg, Q

def create_data(request):
    author1 = Author.objects.create(name='George Orwell', age=46)
    author2 = Author.objects.create(name='J.K. Rowling', age=54)
    Book.objects.create(title='1984', author=author1, published_date='1949-06-08')
    Book.objects.create(title='Harry Potter and the Philosopher\'s Stone', author=author2, published_date='1997-06-26')
    Book.objects.create(title='Harry Potter and the Chamber of Secrets', author=author2, published_date='1998-07-02')
    return HttpResponse("Data created")

def show_authors(request):
    authors = Author.objects.all()
    output = ', '.join([author.name for author in authors])
    return HttpResponse(output)

def filter_books(request):
    books = Book.objects.filter(title__icontains='Harry Potter')
    output = ', '.join([book.title for book in books])
    return HttpResponse(output)

def aggregate_data(request):
    avg_age = Author.objects.aggregate(Avg('age'))
    return HttpResponse(f"Average age of authors: {avg_age['age__avg']}")

def annotate_data(request):
    authors = Author.objects.annotate(book_count=Count('book'))
    output = ', '.join([f"{author.name} ({author.book_count} books)" for author in authors])
    return HttpResponse(output)

def complex_query(request):
    authors = Author.objects.filter(Q(name__icontains='George') | Q(age__gt=50))
    output = ', '.join([author.name for author in authors])
    return HttpResponse(output)

