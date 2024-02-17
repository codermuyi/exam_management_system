from django.urls import path
from . import views

urlpatterns = [
    path('student-login/', views.loginStudent, name='student-login'),
    path('student-signup/', views.signupStudent, name='student-signup'),
    path('logout/', views.logoutUser, name='logout'),
    path('account/', views.studentDashboard, name='student-dashboard'),
    path('account/profile/', views.studentProfile, name='student-profile'),
    path('account/schedule/', views.studentSchedule, name='student-schedule'),
    path('account/timetable/', views.studentTimetable, name='student-timetable'),
    path('account/notification', views.studentNotification, name='student-notification'),
    path('account/map', views.studentMap, name='student-map'),
]
