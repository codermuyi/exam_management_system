from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group

# from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import StudentForm, StudentUserForm
from .models import Student
from base.models import Course, ExamTimetable

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
        )
    else:
        courses = []

    context = {"courses": courses, "student": student}
    return render(request, "student/student_dashboard.html", context)


@login_required(login_url="student-login")
def studentProfile(request):
    student = Student.objects.get(user=request.user)

    studentForm = StudentForm(instance=student)
    userForm = StudentUserForm(instance=request.user)

    context = {
        "student": student,
        "matric_no": student.user.username.replace(".", "/"),
        "studentForm": studentForm,
        "userForm": userForm,
    }
    return render(request, "student/pages/student-profile.html", context)


def studentTimetable(request):
    student = Student.objects.get(user=request.user)
    timetable = ExamTimetable.objects.get(
        department=student.department, student_level=student.level
    )

    context = {"timetable": timetable}
    return render(request, "student/pages/timetable.html", context)


def studentSchedule(request):
    context = {}
    return render(request, 'student/pages/student-schedule.html')

def studentNotification(request):
    context = {}
    return render(request, 'student/pages/notifications.html')


def studentMap(request):
    context = {}
    return render(request, 'student/pages/maps.html')
  
