# More_apps/competition_upload/serializers.py

from rest_framework import serializers
from .models import Competition

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'created_at']
