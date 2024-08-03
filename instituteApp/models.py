from django.db import models

# Create your models here.
class Academicyear(models.Model):
    academicyearname=models.CharField(max_length=255, null=True, blank=True)
    startson=models.DateField(null=True,blank=True)
    endson=models.DateField(null=True,blank=True)
    addondate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)
    isactive = models.BooleanField(default=False, null=True, blank=True)

class Course(models.Model):
    coursename=models.CharField(max_length=255)
    code=models.CharField(max_length=255, null=True,blank=True)
    Description=models.TextField(null=True,blank=True)
    academicid = models.ForeignKey(Academicyear, on_delete=models.CASCADE)
    isactive=models.BooleanField(default=True, null=True,blank=True)
    addondate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)

class Batch(models.Model):
    batchname = models.CharField(max_length=255)
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    addondate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)
    academicid = models.ForeignKey(Academicyear,null=True,blank=True ,on_delete=models.CASCADE)

class Subject(models.Model):
    subject = models.CharField(max_length=255)
    academicid = models.ForeignKey(Academicyear, on_delete=models.CASCADE, null=True, blank=True, )
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, )
    syllabus = models.FileField(upload_to='syllabus/', null=True, blank=True)
    # semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True, blank=True, )
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True, blank=True)

class Quata(models.Model):
    AdmittedQuata = models.CharField(max_length=255)

class Student(models.Model):
    admissionnumber = models.CharField(max_length=220, null=True, blank=True)
    admissionyear = models.CharField(max_length=220, null=True, blank=True)
    firstname = models.CharField(max_length=220, null=True, blank=True)
    lastname = models.CharField(max_length=220, null=True, blank=True)
    email = models.CharField(max_length=220, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    bloodgroup = models.CharField(max_length=220, null=True, blank=True)
    phonenumber = models.IntegerField(null=True, blank=True)
    contactdetails = models.CharField(max_length=220, null=True, blank=True)
    gender = models.CharField(max_length=220, null=True, blank=True)
    rollno = models.IntegerField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True, blank=True)
    batch = models.ForeignKey(Batch,on_delete=models.CASCADE, null=True, blank=True)
    academicyear = models.ForeignKey(Academicyear,on_delete=models.CASCADE, null=True, blank=True)
    attend = models.CharField(max_length=255, null=True,blank=True)
    admittedquota = models.ForeignKey(Quata,on_delete=models.CASCADE, null=True, blank=True)
    regno = models.IntegerField(null=True, blank=True)

class Teacher(models.Model):
    Name=models.CharField(max_length=255)
    Designation=models.CharField(max_length=255)
    Education=models.CharField(max_length=255)
    Experience=models.IntegerField()
    Gender=models.CharField(max_length=255)
    Subject=models.CharField(max_length=255, null=True, blank=True)

class AssignTeacher(models.Model):
    academicyearname = models.ForeignKey(Academicyear, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Name = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    coursename = models.ForeignKey(Course, on_delete=models.CASCADE)
    batchname = models.ForeignKey(Batch, on_delete=models.CASCADE)

class Timetable(models.Model):
    day = models.CharField(max_length=255)
    starttime = models.CharField(max_length=255)
    endtime = models.CharField(max_length=255)
    isbreak = models.BooleanField(default=False, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    batchname = models.ForeignKey(Batch, on_delete=models.CASCADE)
    coursename = models.ForeignKey(Course, on_delete=models.CASCADE)
