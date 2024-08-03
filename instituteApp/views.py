from django.shortcuts import render,redirect
from instituteApp import models
# Create your views here.
def academicyear(request):
    print(request.POST,'--------')
    data=models.Academicyear.objects.all()
    if request.method=='POST' and 'submit' in request.POST:
        academic = request.POST.get('academicyear')
        startson = request.POST.get('startson')
        endson = request.POST.get('endson')
        obj = models.Academicyear()
        obj.academicyearname = academic
        obj.startson = startson
        obj.endson = endson
        obj.save()
        print("succesfully printed")
    if request.method == "POST" and "delete" in request.POST:
        idd = request.POST.get("delete")
        obj = models.Academicyear.objects.get(id=idd)
        obj.delete()
    if request.method == "POST" and "active" in request.POST:
        idd = request.POST.get("active")
        obj = models.Academicyear.objects.get(id=idd)
        ob = models.Academicyear.objects.exclude(id=idd)

        if obj.isactive==False:
            obj.isactive=True
            obj.save()
            for i in ob:
                i.isactive=False
                i.save()
        else:
            obj.isactive=False
            obj.save()
    return render(request,'academicyear.html',{'academic':data})

def acyedit(request,id):
    ob=models.Academicyear.objects.get(id=id)
    if request.method=='POST':
        academic = request.POST.get('academicyear')
        startson = request.POST.get('startson')
        endson = request.POST.get('endson')
        obj = models.Academicyear.objects.get(id=id)
        obj.academicyearname = academic
        obj.startson = startson
        obj.endson = endson
        obj.save()
        return redirect('academicyear')
    return render(request,'editacademicyear.html',{'obj':ob})

def course(request):
    academic = models.Academicyear.objects.get(isactive=True)
    data = models.Course.objects.all()
    if request.method == 'POST' and 'submit' in request.POST:
        course = request.POST.get('course')
        # code = request.POST.get('code')
        # description = request.POST.get('description')
        # academicyear = request.POST.get('academicyear')
        # academi = models.Academicyear.objects.get(academicyearname=academicyear)
        obj = models.Course()
        obj.coursename = course
        # obj.code = code
        # obj.description = description
        obj.academicid = academic
        obj.save()
        print("succesfully printed")
    if request.method == "POST" and "delete" in request.POST:
        idd = request.POST.get("delete")
        obj = models.Course.objects.get(id=idd)
        obj.delete()
    return render(request, 'course.html', {'key2': data, 'acad': academic})


def courseedit(request, id):
    # academic = models.Academicyear.objects.get(id=id)
    course = models.Course.objects.get(id=id)
    if request.method == 'POST':
        course = request.POST.get('course')
        academicyear = request.POST.get('academicyear')
        obj = models.Course.objects.get(id=id)
        obj.coursename = course
        obj.academicid = academicyear
        obj.save()
        return redirect('course')
    return render(request, 'editcourse.html', {'course': course }) #,'academic':academic


def batch(request):
    academic=models.Academicyear.objects.get(isactive=True)
    course=models.Course.objects.all()
    batch = models.Batch.objects.all()
    if request.method == 'POST' and 'submit' in request.POST:
        batchname = request.POST.get('batch')
        #academicyear = request.POST.get('academicyear')
        course = request.POST.get('course')
        ob = models.Batch()
        ob.batchname = batchname
        print(academicyear)
        ob.academicid = academic #models.Academicyear.objects.get(id=academicyear)
        ob.courseid = models.Course.objects.get(id=course)
        ob.save()
        print("succesfully printed")
    if request.method == "POST" and "delete" in request.POST:
        idd = request.POST.get("delete")
        obj = models.Batch.objects.get(id=idd)
        obj.delete()
    return render(request,'batch.html',{'academic': academic, 'course': course,'batch':batch})

def batchedit(request,id):
    batch = models.Batch.objects.get(id=id)
    # academic = models.Academicyear.objects.get(id=id)
    # course = models.Batch.objects.get(id=id)
    if request.method == 'POST':
        batchname = request.POST.get('batch')
        academicyear = request.POST.get('academicyear')
        coursename = request.POST.get('course')
        obj = models.Batch.objects.get(id=batch)
        obj.batchname = batchname
        obj.coursename = coursename
        obj.academicid = academicyear
        obj.save()
        return redirect('batch')
    return render(request, 'editbatch.html',{'batch':batch})   # ,'academic':academic,'course': course


# def batchedit(request,id,academicid):
#     course = models.Course.objects.get(id=id)
#     academic = models.Academicyear.objects.get(id=academicid)
#     batch = models.Batch.objects.get(id=id)
#     if request.method == 'POST':
#         batchname = request.POST.get('batch')
#         # academic = request.POST.get('academicyear')
#         course = request.POST.get('course')
#         obj = models.Batch.objects.get(id=batch)
#         obj.batchname = batchname
#         obj.coursename = course
#         obj.academicid = academic
#         obj.save()
#         return redirect('batch')
#     return render(request, 'editbatch.html',{'course':course,'batch':batch,'academic':academic})
def subject(request):
    academic = models.Academicyear.objects.get(isactive=True)
    course = models.Course.objects.all()
    batch = models.Batch.objects.all()
    subject = models.Subject.objects.all()
    if request.method == "POST" and "submit" in request.POST:
        subject = request.POST.get('subject')
        # academicyear = request.POST.get('academicyear')
        course = request.POST.get('course')
        # syllabus = request.POST.get('')
        batchname = request.POST.get('batch')
        obj = models.Subject()
        obj.subject = subject
        obj.academicid = academic # models.Academicyear.objects.get(id=academicyear)
        obj.courseid = models.Course.objects.get(id=course)
        obj.batch = models.Batch.objects.get(id=batch)
        # obj.syllabus = syllabus
        obj.save()
    return render(request, 'subject.html', {'academic': academic, 'course': course, 'batch': batch,'subject':subject})


def subedit(request,id):
    course = models.Course.objects.get(id=id)
    academic = models.Academicyear.objects.get(id=id)
    batch = models.Batch.objects.get(id=id)
    subject = models.Subject.objects.get(id=id)
    if request.method == 'POST':
        batchname = request.POST.get('batch')
        academicyear = request.POST.get('academicyear')
        course = request.POST.get('course')
        subject = request.POST.get('subject')
        obj = models.Subject.objects.get(id=subject)
        obj.batchname = batchname
        obj.coursename = course
        obj.academicid = academicyear
        obj.subject = subject
        obj.save()
        return redirect('subject')
    return render(request, 'editsubject.html',{'subject':subject,'course':course,'academic':academic,'batch':batch})


def quata(request):
    data = models.Quata.objects.all()
    if request.method == "POST" and "submit" in request.POST:
        admittedquata = request.POST.get('quata')
        obj = models.Quata()
        obj.AdmittedQuata = admittedquata
        obj.save()
    if request.method == "POST" and "delete" in request.POST:
        idd = request.POST.get("delete")
        obj = models.Quata.objects.get(id=idd)
        obj.delete()
    return render(request, 'quata.html',{'quata':data})

def quataedit(request,id):
    quata = models.Quata.objects.get(id=id)
    if request.method == 'POST':
        adquata = request.POST.get('quata')
        obj = models.Quata.objects.get(id=quata)
        obj.admittedquata = adquata
        obj.save()
        return redirect('quata')
    return render(request, 'editquata.html',{'quata':quata})
# --------------------------------------------------------

def student(request):
    data = models.Student.objects.all()

    course=models.Course.objects.all()
    batch = models.Batch.objects.all()
    quata = models.Quata.objects.all()

    if request.method == "POST" and "submit" in request.POST:
        admissionnumber = request.POST.get('admissionnumber')
        admissionyear = request.POST.get('admissionyear')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        bloodgroup = request.POST.get('bloodgroup')
        phonenumber = request.POST.get('phonenumber')
        contactdetails = request.POST.get('contactdetails')
        gender = request.POST.get('gender')
        rollno = request.POST.get('rollno')
        course = request.POST.get('course')
        batch = request.POST.get('batch')
        academicyear = request.POST.get('academicyear')
        attend = request.POST.get('attend')
        admittedquota = request.POST.get('admittedquota')
        regno = request.POST.get('regno')
        obj = models.Student()
        obj.admissionnumber = admissionnumber
        obj.admissionyear = admissionyear
        obj.firstname = firstname
        obj.lastname = lastname
        obj.email = email
        obj.dob = dob
        obj.bloodgroup = bloodgroup
        obj.phonenumber = phonenumber
        obj.contactdetails = contactdetails
        obj.gender = gender
        obj.rollno = rollno
        obj.course = course
        obj.batch = batch
        obj.academicyear = academicyear
        obj.attend = attend
        obj.admittedquota = admittedquota
        obj.regno = regno
        obj.save()
    if request.method == "POST" and "delete" in request.POST:
        idd = request.POST.get("delete")
        obj = models.Student.objects.get(id=idd)
        obj.delete()
    return render(request, 'admission.html',{'stud':data})

def studentlist(request):
    data = models.Student.objects.all()
    if request.method == "POST" and "submit" in request.POST:
        admissionnumber = request.POST.get('admissionnumber')
        admissionyear = request.POST.get('admissionyear')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        dob = request.POST.get('dob')
        contactdetails = request.POST.get('contactdetails')
        gender = request.POST.get('gender')
        course = request.POST.get('course')
        batch = request.POST.get('batch')
        obj = models.Student()
        obj.admissionnumber = admissionnumber
        obj.admissionyear = admissionyear
        obj.firstname = firstname
        obj.lastname = lastname
        obj.dob = dob
        obj.contactdetails = contactdetails
        obj.gender = gender
        obj.course = course
        obj.batch = batch
        obj.save()
    if request.method == "POST" and "delete" in request.POST:
        idd = request.POST.get("delete")
        obj = models.Student.objects.get(id=idd)
        obj.delete()
    return render(request, 'studentlist.html',{'studlist':data})

def addteacher(request):
    data = models.Teacher.objects.all()
    if request.method == "POST" and "submit" in request.POST:
        Name = request.POST.get('name')
        Designation = request.POST.get('designation')
        Education = request.POST.get('education')
        Experiance = request.POST.get('experience')
        Gender = request.POST.get('gender')
        Subject = request.POST.get('subject')
        obj = models.Teacher()
        obj.Name = name
        obj.Designation = designation
        obj.Education = education
        obj.Experiance = experiance
        obj.Gender = gender
        obj.Subject = subject
        obj.save()
    if request.method == "POST" and "delete" in request.POST:
        idd = request.POST.get("delete")
        obj = models.Teacher.objects.get(id=idd)
        obj.delete()
    return render(request, 'teacherdetails.html',{'teacher':data})

def teacherlist(request):
    data = models.Teacher.objects.all()
    if request.method == "POST" and "delete" in request.POST:
        idd = request.POST.get("delete")
        obj = models.Teacher.objects.get(id=idd)
        obj.delete()
    return render(request, 'teacherlist.html',{'data':data})
#
# def student-list edit(request,id):
#        admissionnumber = models.Sudent.objects.get(id=id)
#         admissionyear = request.POST.get('admissionyear')
#         firstname = request.POST.get('firstname')
#         lastname = request.POST.get('lastname')
#         dob = request.POST.get('dob')
#         contactdetails = request.POST.get('contactdetails')
#         gender = request.POST.get('gender')
#         course = request.POST.get('course')
#         batch = request.POST.get('batch')
#     quata = models.Quata.objects.get(id=id)
#     if request.method == 'POST':
#         adquata = request.POST.get('quata')
#         obj = models.Quata.objects.get(id=quata)
#         obj.admittedquata = adquata
#         obj.save()
#         return redirect('quata')
#     return render(request, 'editquata.html',{'quata':quata})


def login(request):
    return render(request,'login.html')