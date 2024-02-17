from django.contrib import admin
# from .models import Department, StudentLevel, School, Semester, Course, ExamVenue, Exam
from .models import *

# Register your models here.

admin.site.register(School)
admin.site.register(Department)
admin.site.register(StudentLevel)
admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(ExamVenue)
admin.site.register(Exam)
admin.site.register(ExamTimetable)
admin.site.register(ExamRoom)
