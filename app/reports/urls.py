from django.urls import include, path
from rest_framework import routers
from . import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'report', views.ReportsViewSet)
router.register(r'info', views.ReportInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('info/', views.ReportInfoView),
]
