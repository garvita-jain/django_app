from django.shortcuts import render

from .models import User
from rest_framework import viewsets
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, LoginSerializer, RegistrationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import login, logout
from rest_framework.decorators import api_view

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('first_name')
	serializer_class = UserSerializer

class LoginView(APIView):
	def post(self, request):
		serializer = LoginSerializer(data = request.data)
		# serializer.is_valid(raise_exception=True):
		if serializer.is_valid():
			user = serializer.validated_data['user']
			login(request, user)
			token, created = Token.objects.get_or_create(user=user)
			return Response({'Token': token.key}, status=200)
		else:
			msg = {'message': "Wrong credentials."}
			return Response(msg, status=200)

class LogoutView(APIView):
	authentication_class = (TokenAuthentication, )

	def post(self, request):
		logout(request)
		return Response(status=204)

class RegistrationView(APIView):
	def post(self, request):
		if request.method == 'POST':
			serializer = RegistrationSerializer(data=request.data)
			data = {}
			if serializer.is_valid():
				user = serializer.save()
				data['response'] = "Registration Successful"
				data['email'] = user.email
				data['first_name'] = user.first_name
			else :
				data = {'message': 'Error in Registration'}
			return Response(data)

# class Dashboard(APIView):
# 	permission_classes = (IsAuthenticated,)

# 	def get(self, request):
# 		content = {'message': 'Hello, World!'}
# 		return Response(content)