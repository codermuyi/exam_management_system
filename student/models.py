from django.db import models
from django.contrib.auth.models import User
from base.models import Department, StudentLevel

# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.ForeignKey(StudentLevel, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    profile_pic = models.ImageField(upload_to='static/profile_pic/Student/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
   
    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name
      
    def __str__(self):
        return self.get_name + " : " + self.user.username.replace(".", "/")

