from pyexpat import model
from django.views.generic import ListView
from .models import Student


# Create your views here.
class StudentListView(ListView):
    print("Student List View")
    model = Student
