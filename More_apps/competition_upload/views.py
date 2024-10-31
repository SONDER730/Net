# More_apps/competition_upload/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Competition
from .serializers import CompetitionSerializer

class CompetitionUploadView(APIView):
    def post(self, request):
        serializer = CompetitionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # 保存竞赛信息到数据库
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CompetitionListView(APIView):
    def get(self, request):
        competitions = Competition.objects.all()  # 查询所有竞赛
        serializer = CompetitionSerializer(competitions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)