"""readit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from books.views import (AuthorDetail, AuthorList, list_books, BookDetail, review_book, review_books)
import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # empty URL
    url(r'^$', list_books, name='books'),
    url(r'^authors/$', AuthorList.as_view(), name='authors'),
    url(r'^book/(?P<pk>[-\w]+)/$', BookDetail.as_view(), name='book-detail'),
    url(r'^authors/(?P<pk>[-\w]+)/$', AuthorDetail.as_view(), name='author-detail'),
    url(r'^review/$', review_books, name='review-books'),
    url(r'^review/(?P<pk>[-\w]+)/$', review_book, name='review-book'),
]

# if settings.DEBUG:
#     import debug_toolbar
#
#     urlpatterns += [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     ]
