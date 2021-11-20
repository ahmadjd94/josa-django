from django.contrib import admin

from .models import Student


class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fields = (
        "id",
        "name",
        "age",
        "grade"
    )


admin.site.register(Student, StudentAdmin)
