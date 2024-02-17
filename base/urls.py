from django.urls import path
from . import views

urlpatterns = [
    path('admin-login/', views.loginAdmin, name='admin-login'),
    path('dashboard/', views.dashboard, name='admin-dashboard'),
    path('dashboard/profile', views.adminProfile, name='admin-profile'),
    path('dashboard/schedule', views.adminProfile, name='admin-schedule'),
    # path('student-signup/', views.signupStudent, name='student-signup'),
    # path('account/', views.studentDashboard, name='student-dashboard'),
    # path('account/profile/', views.studentProfile, name='student-profile'),
    # path('account/schedule/', views.studentSchedule, name='student-schedule'),
    # path('account/timetable/', views.studentTimetable, name='student-timetable'),
    # path('account/notification', views.studentNotification, name='student-notification'),
    # path('account/map', views.studentMap, name='student-map'),
]
