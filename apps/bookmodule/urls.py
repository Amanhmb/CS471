
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
 path('search/', views.search),
  path('simple/query', views.simple_query),
  path('complex/query', views.complex_query),
  
 ]