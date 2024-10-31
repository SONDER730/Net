# More_apps/competition_announcement/urls.py

from django.urls import path
from .views import CompetitionListView

urlpatterns = [
    path('list/', CompetitionListView.as_view(), name='competition-list'),
]
