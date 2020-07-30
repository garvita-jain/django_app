from django.shortcuts import render

from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('first_name')
	serializer_class = UserSerializer
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