from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('search/', views.search),
    path('simple/query', views.simple_query),
    path('complex/query', views.complex_query),
    path('lab8/task1/', views.task1),
    path('lab8/task2/', views.task2),
    path('lab8/task3/', views.task3),
    path('lab8/task4/', views.task4),
    path('lab8/task5/', views.task5),
    path('lab8/task7/', views.task7),
    path('lab9_part1/listbooks', views.listbooks, name="list_books"),
    path('lab9_part1/addbook', views.addbook, name="add_book"),
    path('lab9_part1/editbook/<int:id>', views.editbook, name="edit_book"),
    path('lab9_part1/deletebook/<int:id>', views.deletebook, name="delete_book"),
    path('lab9_part2/listbooks2', views.listbooks, name="list_books2"),
    path('lab9_part2/addbook2', views.addbook2, name="add_book2"),
    path('lab9_part2/editbook2/<int:id>', views.editbook, name="edit_book2"),
    path('lab9_part2/deletebook2/<int:id>', views.deletebook, name="delete_book2"),
    path('lab9/task22', views.task22),
    path('lab9/task33', views.task33),
    path('lab9/task44', views.task44),
    path('lab9/task55', views.task55),
]
