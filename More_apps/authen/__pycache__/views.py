import json

from django.contrib.auth import login
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.http import JsonResponse
# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import StudentRegistrationForm, TeacherRegistrationForm
from .models import StudentInfo, TeacherInfo


def home(request):
    return render(request, 'home.html')

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # 从请求体中获取 JSON 数据
            user_id = data.get('user_id')
            password = data.get('password')
            user_type = data.get('role')  # 前端传递的 'role' 字段 (student 或 teacher)

            if user_type == 'student':
                user = StudentInfo.objects.get(student_id=user_id)
            elif user_type == 'teacher':
                user = TeacherInfo.objects.get(teacher_id=user_id)
            else:
                return JsonResponse({'error': 'Invalid user type.'}, status=400)

            # 验证密码
            if check_password(password, user.password):
                # 登录成功
                request.session['user_type'] = user_type

                # 获取或创建 Django 用户
                user_instance, created = User.objects.get_or_create(username=user_id)

                # 使用 Django 的登录功能
                login(request, user_instance)

                # 返回成功响应
                return JsonResponse({'message': '登录成功', 'role': user_type}, status=200)
            else:
                return JsonResponse({'error': 'Invalid credentials.'}, status=400)

        except (StudentInfo.DoesNotExist, TeacherInfo.DoesNotExist):
            return JsonResponse({'error': 'User not found.'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data.'}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)
def competition(request):
    return render(request, 'competition.html')

def lab(request):
    return render(request, 'lab.html')

def guide(request):
    return render(request, 'guide.html')

@csrf_exempt  # 生产环境中应正确处理 CSRF
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            role = data.get('role')
            if role == 'student':
                form = StudentRegistrationForm(data)
            elif role == 'teacher':
                form = TeacherRegistrationForm(data)
            else:
                return JsonResponse({'error': 'Invalid role type'}, status=400)

            if form.is_valid():
                user = form.save(commit=False)
                user.password = make_password(form.cleaned_data['password'])
                user.save()
                return JsonResponse({'message': f'{role} registered successfully!'}, status=201)
            else:
                return JsonResponse({'error': form.errors}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
def success(request):
    return render(request, 'success.html')
