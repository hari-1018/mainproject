from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Academicyear)
admin.site.register(models.Course)
admin.site.register(models.Batch)
admin.site.register(models.Subject)
admin.site.register(models.Quata)
admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.AssignTeacher)
admin.site.register(models.Timetable)