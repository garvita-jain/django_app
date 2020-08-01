from django.shortcuts import render

from .models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
# from django.contrib.auth.decorators import login_required

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('first_name')
	serializer_class = UserSerializer

class LoginView(APIView):
	def post(self, request):
		serializer = LoginSerializer(data = request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		login(request, user)
		token, created = Token.objects.get_or_create(user=user)
		return Response({'Token': token.key}, status=200)

class LogoutView(APIView):
	authentication_class = (TokenAuthentication, )

	def post(self, request):
		logout(request)
		return Response(status=204)


class Dashboard(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		content = {'message': 'Hello, World!'}
		return Response(content)

# @login_required
# def index(request):
#     return render(request,'accounts/index.html')

# def sign_up(request):
#     context = {}
#     form = UserCreationForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             user = form.save()
#             login(request,user)
#             return render(request,'accounts/index.html')
#     context['form']=form
#     return render(request,'registration/sign_up.html',context)