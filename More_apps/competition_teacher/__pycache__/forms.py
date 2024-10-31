from django import forms

from myapp.competition_teacher.models import TeacherInformation


class TeacherInfoForm(forms.ModelForm):
    class Meta:
        model = TeacherInformation
        fields = ['name', 'department',  'teacher_id',  'email', 'contact']
