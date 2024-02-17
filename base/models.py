from django.db import models

# Create your models here.


class StudentLevel(models.Model):
    name = models.CharField(max_length=5)
    
    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Semester(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=7, unique=True)
    description = models.TextField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    level = models.ForeignKey(StudentLevel, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['course_code']
        
    def __str__(self):
        return self.course_code + ' -> ' + self.course_name


class ExamVenue(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return self.name


class ExamRoom(models.Model):
    name = models.CharField(max_length=20)
    venue = models.ForeignKey(ExamVenue, on_delete=models.CASCADE)
    no_of_seats = models.IntegerField(null=True, blank=True)


class ExamTimetable(models.Model):
    student_level = models.ForeignKey(StudentLevel, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True)
    
    @property
    def get_name(self):
        return self.student_level.name + " " + self.semester.name + " Semester Time Table"
      
    
    def __str__(self) :
        return self.student_level.name + " " + self.department.name + " " + self.semester.name + " Semester Time Table"


class Exam(models.Model):
    course = models.OneToOneField(Course, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=[('paper', 'Paper Exam'), ('cbt', 'CBT Exam')], default='paper')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue = models.ForeignKey('ExamVenue', on_delete=models.SET_NULL, null=True, blank=True)
    timetable = models.ForeignKey(ExamTimetable, on_delete=models.CASCADE)
    
    @property
    def get_day(self):
        days = [
          'monday',
          'tuesday',
          'wednesday',
          'thursday',
          'friday',
          'saturday',
          'sunday',
        ]
        return days[self.date.weekday()]
    
    def __str__(self):
        return self.course.course_code + ' Exam'

