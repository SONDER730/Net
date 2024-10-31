from django import forms

from .models import StudentInformation, StudentFileUpload
from ..competition_teacher.models import CompetitionApplication, TeacherInformation


class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInformation
        fields = ['name', 'school', 'major', 'student_id', 'grade', 'gender', 'email']
        widgets = {
            'gender': forms.RadioSelect(choices=[('M', 'Male'), ('F', 'Female')]),
        }
from django import forms


class CompetitionApplicationForm(forms.ModelForm):
    class Meta:
        model = CompetitionApplication
        fields = ['teacher']

    teacher = forms.ModelChoiceField(queryset=TeacherInformation.objects.all(), label="选择指导老师")


class StudentFileUploadForm(forms.ModelForm):
    class Meta:
        model = StudentFileUpload
        fields = ['file']