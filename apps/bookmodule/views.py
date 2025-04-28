from django.shortcuts import render
from django.db.models import Count, Sum, Avg, Max, Min
from django.shortcuts import get_object_or_404
from django.shortcuts import get_object_or_404, redirect
from .forms import BookForm
from .forms import StudentForm

from .models import Book ,Address ,Student , Department , Course
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

def task22(request):
    departments = Department.objects.annotate(student_count=Count('students'))
    return render(request, 'bookmodule/task22.html', {'departments':departments})


def task33(request):
    courses = Course.objects.annotate(student_count=Count('students'))
    return render(request, 'bookmodule/task33.html', {'courses':courses})


def task44(request):
    departments = Department.objects.annotate(oldest_student_id=Min('students__id'))
    
    department_data = []

    for department in departments:
        if department.oldest_student_id is not None:
            oldest_student = department.students_set.get(id=department.oldest_student_id)
            department_data.append(
                {
                    'department_name': department.name,
                    'oldest_student_name': oldest_student.name
                }
            )

    return render(request, 'bookmodule/task44.html', {'department_data': department_data})


def task55(request):
    departments = Department.objects.annotate(student_count=Count('students')).filter(student_count__gt=2).order_by("-student_count")
    return render(request, 'bookmodule/task55.html', {'departments':departments})


def listbooks(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/listbooks.html', {'books':books})

def addbook(request):
    if request.method =="POST":
        Book.objects.create(
            title= request.POST['title'],
            author= request.POST['author']
            )
        return redirect('list_books')
    return render(request, 'bookmodule/addbook.html')


def editbook(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.save()
        return redirect('list_books')
    return render(request, 'bookmodule/editbook.html', {'book':book})


def deletebook(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('list_books')

def listbooks2(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/listbooks2.html', {'books':books})


def addbook2(request):
    if request.method =="POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books2')
    else:
        form = BookForm()
    return render(request, 'bookmodule/addbook2.html', {'form':form})


def editbook2(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        form = BookForm(request.POST, instance = book)
        if form.is_valid():
            form.save()
            return redirect('list_books2')
    else:
        form = BookForm(instance = book)
    return render(request, 'bookmodule/editbook2.html', {'form':form})


def deletebook2(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('list_books2')

############

def list_students(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/list_students.html', {'students':students})

def addstudent(request):
    if request.method =="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'bookmodule/addstudent.html', {'form':form})


def editstudent(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance = student)
    return render(request, 'bookmodule/editstudent.html', {'form':form})


def deletestudent(request, id):
    Students = get_object_or_404(Student, id=id)
    Students.delete()
    return redirect('list_students')