from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication


def student_home(request):
    return render(request, 'student_home.html')
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import StudentInformation, UploadedFile
from .serializers import StudentInfoSerializer
from django.http import JsonResponse
from functools import wraps
@api_view(['GET', 'POST'])
def student_info_api(request):
    if request.method == 'GET':
        try:
            # 获取当前登录用户的学生信息
            print(request.user)
            student_info = StudentInformation.objects.get(user=request.user)
            serializer = StudentInfoSerializer(student_info)
            return Response(serializer.data)
        except StudentInformation.DoesNotExist:
            return Response({'error': 'Student information not found.'}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        # 创建或更新当前登录用户的学生信息
        print(request.user)
        serializer = StudentInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # 将登录用户与学生信息关联
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileUploadView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.FILES.get('file'):
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage(location='C:/Users/23991/Desktop/upload')  # 文件存储路径
            filename = fs.save(uploaded_file.name, uploaded_file)  # 保存文件
            file_url = fs.url(filename)

            # 保存文件信息到数据库
            UploadedFile.objects.create(user=request.user, file=filename)

            return JsonResponse({'message': '文件上传成功', 'file_url': file_url}, status=200)
        return JsonResponse({'error': '无效的请求'}, status=400)