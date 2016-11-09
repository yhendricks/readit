from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author
from django.views.generic import DetailView, View
from django.db.models import Count


class AuthorList(View):
    def get(self, request):
        #authors = Author.objects.all()
        authors = Author.objects.annotate(
            published_books=Count('books')
        ).filter (
            published_books__gt=0
        )
        context = {
            'authors': authors
        }
        return render(request, "authors.html", context)


def list_books(request):
    """
    List the books that have reviews
    :param request:
    :return HttpResponse:
    """
    books = Book.objects.exclude(date_reviewed__isnull=True).prefetch_related('authors')
    context = {
        'books': books,
    }
    # return HttpResponse(request.user.username)
    return render(request, 'list.html', context)


class BookDetail(DetailView):
    model = Book
    template_name = "book.html"


class AuthorDetail(DetailView):
    model = Author
    template_name = "author.html"
