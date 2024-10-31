from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
urlpatterns = [
path('student_home/', views.student_home, name='student_home'),

    path('competitions/', views.competition_list, name='competition_list'),
    path('competitions/apply/<int:competition_id>/', views.apply_for_competition, name='apply_for_competition'),
    path('my-competitions/', views.my_competitions, name='my_competitions'),
    path('upload/', views.student_upload_file, name='student_upload_file'),
    path('files/', views.student_uploaded_files, name='student_uploaded_files'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

