from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book, Author
from django.views.generic import DetailView, View
from django.db.models import Count
from .forms import ReviewForm


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


def review_books(request):
    """
    List all of the books that we want to review.
    """
    books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')

    context = {
        'books': books,
    }

    return render(request, "list-to-review.html", context)


def review_book(request, pk):
    """
    Review an individual book
    """
    book = get_object_or_404(Book, pk=pk)
    form = ReviewForm

    context = {
        'book': book,
        'form': form,
    }

    return render(request, "review-book.html", context)

