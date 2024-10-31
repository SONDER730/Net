from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from More_apps.authen.models import StudentInfo, TeacherInfo
from More_apps.competition_student.models import  StudentInformation

class TeacherInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    teacher_id = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name



