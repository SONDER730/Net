# Create your views here.
from django.http import HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import TeacherInfoForm
from .serializers import TeacherInformationSerializer
from ..authen.models import TeacherInfo



def teacher_home(request):
    return render(request, 'teacher_home.html')
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import  TeacherInformation


@csrf_exempt  # 取消CSRF验证（如果需要，但建议谨慎使用）
@api_view(['GET', 'POST'])  # 支持 GET 和 POST 请求
@login_required
def teacher_info(request):
    if request.method == 'GET':
     try:
        # 获取与当前用户相关联的教师信息
        teacher_info = TeacherInformation.objects.get(user=request.user)  # 您可能需要根据需求过滤
        serializer = TeacherInformationSerializer(teacher_info)
        return Response(serializer.data)
     except TeacherInformation.DoesNotExist:
        return Response({'error': 'Student information not found.'}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        serializer = TeacherInformationSerializer(data=request.data,many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

