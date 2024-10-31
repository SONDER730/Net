from rest_framework import serializers
from .models import StudentInformation

class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInformation
        fields = ['name', 'student_id', 'gender', 'phone', 'email', 'school', 'major', 'grade']
