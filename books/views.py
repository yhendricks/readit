from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


# Create your views here.
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
    #return HttpResponse(request.user.username)
    return render(request, 'list.html', context)
