from django.shortcuts import render
from .models import Report, ReportInfo
from rest_framework import viewsets
from .serializers import ReportSerializer, ReportInfoSerializer

# Create your views here.
class ReportsViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all().order_by('date_added')
    serializer_class = ReportSerializer

class ReportInfoViewSet(viewsets.ModelViewSet):
    queryset = ReportInfo.objects.all().order_by('parameter')
    serializer_class = ReportInfoSerializer