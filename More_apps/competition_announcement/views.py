# More_apps/competition_announcement/views.py

from rest_framework import generics
from .models import Competition
from .serializers import CompetitionSerializer
from rest_framework.permissions import AllowAny

class CompetitionListView(generics.ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [AllowAny]
