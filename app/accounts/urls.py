from django.urls import include, path
from rest_framework import routers
# from rest_framework.authtoken.views import obtain_auth_token
from . import views
# from allauth.account.views import confirm_email
# from django.conf.urls import url
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('reports/', include('reports.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('hello/', views.DashboardInfoView.as_view(), name='hello'),

    # path('api-token-auth/', obtain_auth_token),
    # url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^account/', include('allauth.urls')),
    # url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]