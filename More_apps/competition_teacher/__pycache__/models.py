from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from myapp.authen.models import StudentInfo, TeacherInfo
from myapp.competition_student.models import Competition, StudentInformation

class TeacherInformation(models.Model):

    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    teacher_id = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name



class CompetitionApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', '审核中'),
        ('approved', '进行中'),
        ('rejected', '已拒绝'),
    ]
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentInformation, on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherInformation, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f'{self.competition.name} - {self.student.name} ({self.status})'
