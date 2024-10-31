# Create your views here.
from django.http import HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import TeacherInfoForm
from .serializers import TeacherInformationSerializer
from ..authen.models import TeacherInfo
from ..competition_student.models import StudentFileUpload


def teacher_home(request):
    return render(request, 'teacher_home.html')
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import CompetitionApplication, TeacherInformation


@csrf_exempt  # 取消CSRF验证（如果需要，但建议谨慎使用）
@api_view(['GET', 'POST'])  # 支持 GET 和 POST 请求
def teacher_info(request):
    if request.method == 'GET':
        # 获取与当前用户相关联的教师信息
        teacher_info = TeacherInformation.objects.all()  # 您可能需要根据需求过滤
        serializer = TeacherInformationSerializer(teacher_info, many=isinstance(request.data, list))
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TeacherInformationSerializer(data=request.data,many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@login_required
def manage_applications(request):
    teacher = TeacherInformation.objects.get(user=request.user)
    applications = CompetitionApplication.objects.filter(teacher=teacher)

    return render(request, 'manage_applications.html', {'applications': applications})

@login_required
def approve_application(request, application_id):
    application = CompetitionApplication.objects.get(id=application_id)
    application.status = 'approved'
    application.save()
    return redirect('manage_applications')

@login_required
def reject_application(request, application_id):
    application = CompetitionApplication.objects.get(id=application_id)
    application.status = 'rejected'
    application.save()
    return redirect('manage_applications')


@login_required
def teacher_view_files(request):
    if not request.user:  # 确保教师是staff用户
        return HttpResponseForbidden("You are not allowed to view this page")
    files = StudentFileUpload.objects.all()  # 显示所有学生上传的文件
    return render(request, 'view_files.html', {'files': files})
