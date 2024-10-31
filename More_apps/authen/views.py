import json
from functools import wraps

from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken

from .forms import StudentRegistrationForm, TeacherRegistrationForm
from .models import StudentInfo, TeacherInfo
# 关于验证码的相关导入
import random
import string
from captcha.image import ImageCaptcha
import redis

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
            captcha = data.get('captcha') # 前端传递验证码
            # 获取 Redis 中存储的验证码
            captcha_key = f"captcha_{request.session.session_key}"
            correct_captcha = redis_client.get(captcha_key)

            # 验证验证码是否过期
            if not correct_captcha:
                return JsonResponse({'error': '验证码已过期'}, status=400)

            # 验证验证码
            if captcha.upper() != correct_captcha.decode('utf-8'):
                return JsonResponse({'error': '验证码错误，请重试。'}, status=400)
            if user_type == 'student':
                user_info = StudentInfo.objects.get(student_id=user_id)
                user = user_info.user  # 关联的 User 模型
            elif user_type == 'teacher':
                user_info = TeacherInfo.objects.get(teacher_id=user_id)
                user = user_info.user  # 关联的 User 模型
            else:
                return JsonResponse({'error': 'Invalid user type.'}, status=400)

            # 验证密码
            if check_password(password, user.password):
                # 登录成功，生成 JWT
                refresh = RefreshToken.for_user(user)
                return JsonResponse({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'role': user_type
                }, status=200)
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
                if form.is_valid():
                    # 创建 User 对象
                    user = User(username=form.cleaned_data['student_id'])
                    user.set_password(form.cleaned_data['password'])  # 使用 set_password 进行密码哈希
                    user.save()

                    # 创建 StudentInfo 关联对象
                    student_info = form.save(commit=False)  # 不保存到数据库
                    student_info.user = user  # 关联 User 对象

                    student_info.password=user.password
                    student_info.save()  # 保存到数据库


                    return JsonResponse({'message': 'Student registered successfully!'}, status=201)

            elif role == 'teacher':
                form = TeacherRegistrationForm(data)
                if form.is_valid():
                    # 创建 User 对象
                    user = User(username=form.cleaned_data['teacher_id'])
                    user.set_password(form.cleaned_data['password'])  # 使用 set_password 进行密码哈希
                    user.save()

                    # 创建 TeacherInfo 关联对象
                    teacher_info = form.save(commit=False)  # 不保存到数据库
                    teacher_info.user = user  # 关联 User 对象
                    teacher_info.password = user.password
                    teacher_info.save()  # 保存到数据库

                    return JsonResponse({'message': 'Teacher registered successfully!'}, status=201)

            else:
                return JsonResponse({'error': 'Invalid role type'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)  # 处理其他异常并返回错误信息

    return JsonResponse({'error': 'Invalid request method'}, status=405)
def success(request):
    return render(request, 'success.html')
def login_required_api(view_func):
    @wraps(view_func)
    def _wrapped_view_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required.'}, status=401)
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func

"""
    验证码的部署逻辑：
    1、用户请求登陆或其他操作，向后端发送信息
    2、后端生成验证码的图片以及正确的编码，并用redis存储
    3、把图片通过二进制流的方式发送到前端
    4、前端接受到二进制流后通过img标签展示
    5、用户填写的验证码通过表单发回到后端进行校验
"""

# 配置 Redis 连接
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
@csrf_exempt
def generate_captcha(request):
    # 生成随机验证码文本
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    # 生成验证码图片
    image = ImageCaptcha()
    captcha_image = image.generate_image(captcha_text)

    # 将验证码存储到 Redis 中，设置有效期为 300 秒
    captcha_key = f"captcha_{request.session.session_key}"
    redis_client.setex(captcha_key, 300, captcha_text)

    # 返回验证码图片
    response = HttpResponse(content_type="image/png")
    captcha_image.save(response, "PNG")
    return response
