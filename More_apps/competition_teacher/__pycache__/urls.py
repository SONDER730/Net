from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from . import views
urlpatterns = [
path('teacher_home/', views.teacher_home, name='teacher_home'),

path('manage-applications/', views.manage_applications, name='manage_applications'),
path('manage-applications/approve/<int:application_id>/', views.approve_application, name='approve_application'),
path('manage-applications/reject/<int:application_id>/', views.reject_application, name='reject_application'),
path('view_files/', views.teacher_view_files, name='teacher_view_files'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)