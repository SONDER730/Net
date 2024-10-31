# More_apps/competition_upload/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.CompetitionUploadView.as_view(), name='competition-upload'),
    path('list/', views.CompetitionListView.as_view(), name='competition-list'),
]
