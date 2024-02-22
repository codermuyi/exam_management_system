from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.db import transaction

# from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import StudentForm, StudentUserForm, UpdateUserForm
from .models import Student
from base.models import Course, ExamTimetable, Exam

# Create your views here.


def logoutUser(request):
    logout(request)
    return redirect("home")


def loginStudent(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect("student-dashboard")

    if request.method == "POST":
        username = request.POST.get("username").upper()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("student-dashboard")
        else:
            messages.error(request, "Username or password does not exist")

    context = {"page": page}
    return render(request, "student/student_auth.html", context)


def signupStudent(request):
    if request.user.is_authenticated:
        return redirect("student-dashboard")

    page = "signup"
    userForm = StudentUserForm()
    studentForm = StudentForm()

    if request.method == "POST":
        userForm = StudentUserForm(request.POST)
        studentForm = StudentForm(request.POST, request.FILES)

        if userForm.is_valid() and studentForm.is_valid():
            user = userForm.save(commit=False)
            user.username = user.username.upper()
            user.save()

            student = studentForm.save(commit=False)
            student.user = user
            student.save()

            my_student_group = Group.objects.get_or_create(name="STUDENT")
            my_student_group[0].user_set.add(user)
            login(request, user)
            return redirect("student-dashboard")

    context = {"page": page, "userForm": userForm, "studentForm": studentForm}
    return render(request, "student/student_auth.html", context)


@login_required(login_url="student-login")
def studentDashboard(request):
    student = Student.objects.get(user=request.user)

    if student.department:
        courses = Course.objects.filter(
            department=student.department, level=student.level
        ).values()
    else:
        courses = []

    context = {"courses": courses, "student": student}
    return render(request, "student/student_dashboard.html", context)


@login_required(login_url="student-login")
def studentProfile(request):
    student = Student.objects.get(user=request.user)

    studentForm = StudentForm(instance=student)
    userForm = UpdateUserForm(instance=request.user)

    if request.method == "POST":
        userForm = UpdateUserForm(request.POST, instance=request.user)
        studentForm = StudentForm(request.POST, instance=student)

        if userForm.is_valid() and studentForm.is_valid():
            print("Something")
            userForm.save()
            studentForm.save()

            messages.success(request, "Your profile is updated successfully")
            return redirect("student-profile")
        else:
            print("An error occurred.")
            messages.error(request, "Something went wrong")

    context = {
        "student": student,
        "matric_no": student.user.username.replace(".", "/"),
        "studentForm": studentForm,
        "userForm": userForm,
        "userForm_errors": userForm.errors,
    }
    return render(request, "student/pages/student-profile.html", context)


@login_required(login_url='student-login')
def studentTimetable(request):
    student = Student.objects.get(user=request.user)
    timetable = ExamTimetable.objects.get(
        department=student.department, student_level=student.level
    )

    context = {"timetable": timetable}
    return render(request, "student/pages/timetable.html", context)


@login_required(login_url="student-login")
def studentSchedule(request):
    student = Student.objects.get(user=request.user)
    exams = Exam.objects.filter(course__department__id=student.department.id)

    context = {"exams": exams}
    return render(request, "student/pages/student-schedule.html", context)


@login_required(login_url="student-login")
def studentNotification(request):
    context = {}
    return render(request, "student/pages/notifications.html")


@login_required(login_url="student-login")
def studentMap(request):
    context = {}
    return render(request, "student/pages/maps.html")

