from django.shortcuts import render

from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from studentapp import models

class CourseList(APIView):
    def get(self, request,id=None):
        if id == None:
            course=models.Course.objects.all()
            serializer=serializers.CourseSerializer(course, many=True)

        else:
            course = models.Batch.objects.get(id=id)
            serializer=serializers.CourseSerializer(course)
        return Response(serializer.data)

class BatchList(APIView):
    def get(self, request):
        batch=models.Batch.objects.filter(academicid__isactive =True)
        serializer=serializers.BatchSerializer(batch, many=True)
        return Response(serializer.data)


class SubjectList(APIView):
    def get(self, request,id):
        subject=models.Subject.objects.filter(academicid__isactive =True,semester=id)
        serializer=serializers.SubjectSerializer(subject, many=True)
        return Response(serializer.data)

class TeacherList(APIView):
    def get(self, request):
        teacher=models.AssignTeacher.objects.all()
        serializer=serializers.AssignTeacherSerializer(teacher,many=True)
        return Response(serializer.data)

class StudentList(APIView):
    def get(self, request):
        student=models.Student.objects.all()
        serializer=serializers.StudentSerializer(student,many=True)
        return Response(serializer.data)

class SemesterList(APIView):
    def get(self, request):
        semester=models.Semester.objects.filter(academicid__isactive =True)
        serializer=serializers.SemesterSerializer(semester, many=True)
        return Response(serializer.data)

class PdfList(APIView):
    def get(self, request, subject_id):
        syllabus = models.Subject.objects.filter(academicid__isactive=True,id=subject_id)
        serializer = serializers.PDFSerializer(syllabus, many=True)
        return Response(serializer.data)

class SubjectList1(APIView):
    def get(self, request,id):
        subject=models.Subject.objects.filter(academicid__isactive =True)
        serializer=serializers.SubjectSerializer(subject, many=True)
        return Response(serializer.data)
