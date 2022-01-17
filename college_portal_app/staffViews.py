#code written and modified
#date :19-06-21
#author:neetya

from college_portal_app.models import SessionYearModel, Subjects
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from college_portal_app.forms import EventForm
from college_portal_app.models import CustomUser, Teachers,Semisters,Students,Calendar,LeaveReportTeacher,LeaveReportStudent,Attendance,AttendanceReport


def staff_home(request):
    return render(request, "staff_Templates/home_content.html")

def staff_attendance(request):
    subject=Subjects.objects.filter(subject_id=request.user.id)
    session_year=SessionYearModel.objects.all()
    return render(request,"staff_Templates/staff_attendance.html",{"subject":subject,"session_year":session_year})

def staff_apply_lv_rq(request):
    return render(request, "staff_Templates/staff_apply_lv_rq.html")

def staff_stud_lv_rq(request):
    return render(request,"staff_Templates/staff_stud_lv_rq.html")

def chk_stud_attendance(request):
    return render(request, "staffTemplates/chk_stud_attendance.html") 




def staff_add_student(request):
    semisters=Semisters.objects.all()
    return render(request,'staffTemplates/add_student.html',{"semisters":semisters})

def add_student_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method ")
        return redirect('add_student')
        
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        session_start=request.POST.get('session_start')
        session_end=request.POST.get('session_end')
        semister_id=request.POST.get('semister')
        sex=request.POST.get("sex")

        try:

            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=3)
            user.students.address = address
            semister_obj=Semisters.objects.get(id=semister_id)
            user.students.semister_id=semister_obj
            user.students.session_start_year=session_start
            user.students.session_end_year=session_end
            user.students.gender=sex
            user.students.profile_pics=""
            user.save()
            messages.success(request, "Student Added Successfully!")
            return redirect('add_student')
        except:
            messages.error(request, "Failed to Add Student!")
            return redirect('add_student')


def manage_student(request):
    students = Students.objects.all()
    context = {
        "students": students
    }
    # print(context.admin)
    return render(request, 'staffTemplates/manage_student.html', context)


# def leave_req(request):
#     students = LeaveReportStudent.objects.all()
#     context = {
#         "students": students
#     }
#     # print(context.admin)
#     return render(request, 'hod_template/leave_req.html', context)
    
# def leave_req_faculty(request):
#     Teachers = LeaveReportTeacher.objects.all()
#     context = {
#         "teachers": Teachers
#     }
#     # print(context.admin)
#     return render(request, 'hod_template/leave_req_faculty.html', context)

# def attendance_faculty(request):
#     Teachers = Attendance.objects.all()
#     context = {
#         "teachers": Teachers
#     }
#     # print(context.admin)
#     return render(request, 'hod_template/attendance_faculty.html', context)

# def attendance_student(request):
#     Students = AttendanceReport.objects.all()
#     context = {
#         "students": Students
#     }
#     # print(context.admin)
#     return render(request, 'hod_template/attendance_student.html', context)