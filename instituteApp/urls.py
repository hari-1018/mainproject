from django.urls import path
from . import views

urlpatterns = [
    path('acy/',views.academicyear,name = 'academicyear'),
    path('acyedit/<int:id>/',views.acyedit,name='acyedit'),
    path('course/',views.course, name='course'),
    path('courseedit/<int:id>/',views.courseedit,name='courseedit'),
    path('batch/',views.batch,name='batch'),
    path('subject/',views.subject,name='subject'),
    path('subedit/<int:id>/',views.subedit,name='subedit'),
    path('quata/',views.quata,name='quata'),
    #--------------------------------------------------------
    path('admission/', views.student, name='student'),
    path('studentlist/', views.studentlist, name='studentlist'),
    path('teacherdetails/', views.addteacher, name='addt'),
    path('teacherlist/', views.teacherlist, name='list'),
]