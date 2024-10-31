from django.views.decorators.csrf import csrf_exempt

from .forms import StudentInfoForm, StudentFileUploadForm
from .models import StudentInformation, StudentFileUpload
from ..competition_teacher.models import CompetitionApplication
from django.contrib.auth.decorators import login_required

def student_home(request):
    return render(request, 'student_home.html')
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import StudentInformation
from .serializers import StudentInfoSerializer
@csrf_exempt
@api_view(['GET', 'POST'])
def student_info_api(request):
    if request.method == 'GET':
        # 获取所有学生信息
        student_info = StudentInformation.objects.all()
        serializer = StudentInfoSerializer(student_info, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # 创建或更新学生信息
        serializer = StudentInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render, redirect

from .models import Competition,  StudentInfo
from .forms import CompetitionApplicationForm

@login_required
def competition_list(request):
    competitions = Competition.objects.all()
    return render(request, 'competition_list.html', {'competitions': competitions})

@login_required
def apply_for_competition(request, competition_id):
    competition = Competition.objects.get(id=competition_id)
    student = StudentInformation.objects.get(user=request.user)

    if request.method == 'POST':
        form = CompetitionApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.competition = competition
            application.student = student
            application.status = 'pending'
            application.save()
            return redirect('my_competitions')
    else:
        form = CompetitionApplicationForm()

    return render(request, 'apply_for_competition.html', {'form': form, 'competition': competition})

@login_required
def my_competitions(request):
    student = StudentInformation.objects.get(user=request.user)
    applications = CompetitionApplication.objects.filter(student=student)
    return render(request, 'my_competitions.html', {'applications': applications})

@login_required
def student_upload_file(request):
    if request.method == 'POST':
        form = StudentFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_upload = form.save(commit=False)
            file_upload.student = request.user  # 关联上传者为当前用户
            file_upload.save()
            return redirect('student_uploaded_files')  # 上传成功后重定向到文件列表页
    else:
        form = StudentFileUploadForm()
    return render(request, 'upload_file.html', {'form': form})

@login_required
def student_uploaded_files(request):
    files = StudentFileUpload.objects.filter(student=request.user)  # 仅显示当前学生上传的文件
    return render(request, 'uploaded_files.html', {'files': files})