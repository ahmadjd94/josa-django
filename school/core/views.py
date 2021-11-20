from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .form import StudentForm
from .models import Student


class StudentListView(ListView):
    model = Student


class StudentsDetailView(DetailView):
    model = Student

def delete_student(request,pk):
    student = Student.objects.get(id=pk)
    print(student)
    student.delete()
    return HttpResponse(render(request, template_name="core/student_delete.html"))


def create_student(request):
    print(request)
    if request.method =="GET":
        form = StudentForm()
        return HttpResponse(render(request, template_name="core/student_create.html",
                                   context={"form": form}))
    elif request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(render(request, template_name="core/student_success.html"))
        return HttpResponse(render(request, template_name="core/student_errors.html",
                                   context={"errors": "this is an error"}))

