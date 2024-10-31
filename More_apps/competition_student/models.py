from django.contrib.auth.models import User
from django.db import models

from More_apps.authen.models import StudentInfo, TeacherInfo


class StudentInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    school = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)


    def __str__(self):
        return self.name

class UploadedFile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')  # 文件字段，存储文件
    uploaded_at = models.DateTimeField(auto_now_add=True)  # 上传时间

    def __str__(self):
        return self.file.name

