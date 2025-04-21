from django.shortcuts import render
from django.db.models import Count, Sum, Avg, Max, Min

from .models import Book ,Address ,Student 
# Create your views here.
from django.db.models import Q 

from django.http import HttpResponse
def index(request):
    name = request.GET.get("name") or "world!"  #add this line
    return render(request, "bookmodule/index.html"  , {"name": name})  

def index2(request, val1 = 0):   #add the view function (index2)
    return HttpResponse("value1 = "+str(val1))

def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)

def index(request):
 return render(request, "bookmodule/index.html")
 


def list_books(request):
    return render(request, 'bookmodule/list_books.html') 

def viewbook(request, bookId):
 return render(request, 'bookmodule/one_book.html')  


def aboutus(request):
 return render(request, 'bookmodule/aboutus.html')

def search (request):
  if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
 

  return render(request, 'bookmodule/search.html')


def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]
 
def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='a') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')

def task1(request):
   books = Book.objects.filter(Q(price__lte=50))
   return render(request, 'bookmodule/bookList.html', {'books':books})


def task2(request):
   books = Book.objects.filter(Q(edition__lte=50))
   return render(request, 'bookmodule/bookList.html', {'books':books})

def task2(request):
   books = Book.objects.filter(Q(edition__lte=50))
   return render(request, 'bookmodule/bookList.html', {'books':books})

def task3(request):
    # Query books with editions no higher than 3 and do not contain 'co' in title or author
    books = Book.objects.filter(
        Q(edition__lte=3) & ~(Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task4(request):
    # Query books and order by title
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books': books})

def task5(request):
    # Perform aggregation on the Book model
 query = Book.objects.aggregate(
        num_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
 return render(request, 'bookmodule/task5.html', {'books': query})

def task7(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task7.html', {'cities': cities})