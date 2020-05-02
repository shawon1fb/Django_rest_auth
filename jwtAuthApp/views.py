from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_jwt.settings import api_settings
from .utils import jwt_response_payload_handler
from django.contrib.auth.models import User

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class JwtAuthApp(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        print(request.data)
        print(request.query_params.get('two'))
        print("query params ------")
        for k, v in request.GET.items():
            print(f"{k} :{v}")

        print("body json ------")
        for k, v in request.data.items():
            print(f"{k} :{v}")
        return Response(data=request.data)


class LoginWithoutSerializer(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        print(request.user)
        if request.user.is_authenticated:
            return Response(data={"message": "you already login"})

        data = request.data
        print(data)
        username = data.get("username")
        # email = data.get("email")
        password = data.get("password")
        print(username)
        print(password)
        qs = User.objects.filter(
            Q(username__iexact=username) |
            Q(email__iexact=username)
        ).distinct()
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                payload = jwt_payload_handler(user_obj)
                token = jwt_encode_handler(payload)
                response = jwt_response_payload_handler(user=user_obj, request=request, token=token)
                return JsonResponse(data=response)
            else:
                return Response(data={"details": "wrong password"})
        # user = authenticate(username=username, password=password)
        return Response(data={"details": "invalid login credentials"})


class RegisterWithoutSerializer(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        print(request.user)
        if request.user.is_authenticated:
            return Response(data={"message": "you already Registered..."})

        data = request.data
        print(data)
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        print(username)
        print(password)
        qs = User.objects.filter(
            Q(username__iexact=username) |
            Q(email__iexact=username)
        )
        if qs.exists():
            return JsonResponse(data={"details": "User already exists"})
        else:
            print("create user ----")
            user = User.objects.create_user(username=username, email=email)
            user.set_password(password)
            user.save()
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            response = jwt_response_payload_handler(user=user, request=request, token=token)
            return JsonResponse(data=response)
