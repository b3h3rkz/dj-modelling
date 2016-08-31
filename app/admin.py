from django.contrib import admin
from .models import School, Class, Student


class SchoolModelAdmin(admin.ModelAdmin):
    model = School
    list_display = ['name', 'classes']


class ClassModelAdmin(admin.ModelAdmin):
    model = Class
    list_display = ['name', 'school', 'enrolled_students']


class StudentModelAdmin(admin.ModelAdmin):
    model = Student
    list_display = ['first_name', 'last_name', 'student_id', 'student_class']


admin.site.register(Class, ClassModelAdmin)
admin.site.register(School, SchoolModelAdmin)
admin.site.register(Student, StudentModelAdmin)