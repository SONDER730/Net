from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models

class StudentInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20)  # 保留 student_id
    email = models.EmailField(max_length=100)  # 添加 email 字段
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.student_id



class TeacherInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length=20)  # 保留 teacher_id
    email = models.EmailField(max_length=100)  # 添加 email 字段
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.teacher_id