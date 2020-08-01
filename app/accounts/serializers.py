from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework import exceptions
from django.contrib.auth import authenticate
from .models import User

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    gender = serializers.CharField(max_length=6)
    dob = serializers.DateField()
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    phone_no = serializers.CharField(max_length=10)
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['password'], first_name = validated_data['first_name'], last_name=validated_data['last_name'], gender=validated_data['gender'], dob=validated_data['dob'], phone_no=validated_data['phone_no']) 
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'gender', 'dob', 'phone_no')

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email', '')
        password = data.get('password', '')

        if email and password:
            user = authenticate(email = email, password = password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise exceptions.ValidationError('User Logged Out')
            else:
                raise exceptions.ValidationError('Invalid Email id/Password')
        else:
            raise exceptions.ValidationError('Email id/Password not provided') 
        
        return data

class RegistrationSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()
    password2 = serializers.CharField()
