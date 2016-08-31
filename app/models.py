from django.db import models

"""
The task is to therefore create a three model Django project that contains school objects,
classroom objects, and student objects.
A student can belong only to one classroom and a classroom only relates to a single school.

We do not need to know subjects that pupils might be taking, or any results, grades, or exams they might be associated with, so these should not be included within the above models.

MODELS
------------
SCHOOL =
CLASSROOM = can only belong to one school
STUDENT = can only belong to one classroom
"""


class School(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def classes(self):
        return self.class_set.count()


class Class(models.Model):
    name = models.CharField(max_length=30, unique=True)
    school = models.ForeignKey(School)

    class Meta:
        verbose_name_plural = 'Classes'

    def __str__(self):
        return self.name

    def enrolled_students(self):
        return self.student_set.count()


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    student_id = models.CharField(max_length=8, unique=True)
    student_class = models.ForeignKey ('Class', Class)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


