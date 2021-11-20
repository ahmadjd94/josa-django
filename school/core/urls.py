
from django.contrib import admin
from django.urls import path

from .views import StudentListView, StudentsDetailView, create_student, delete_student

urlpatterns = [
    path("students", StudentListView.as_view()),
    path("students/<int:pk>", StudentsDetailView.as_view()),
    path("students/create", create_student),
    path("students/delete/<int:pk>", delete_student),

]
