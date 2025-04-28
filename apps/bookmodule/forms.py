from django import forms
from .models import Book, Student, Address

class BookForm(forms.ModelForm):  
    class Meta:
        model = Book
        fields = ['title', 'author']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'  

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
