from rest_framework import serializers
from .models import TeacherInformation

class TeacherInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherInformation
        fields = ['name', 'department', 'teacher_id', 'email', 'contact']
