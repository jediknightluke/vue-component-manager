# API/authentication/views.py
from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate
from rest_framework import generics, permissions, response, status
from .serializers import UserSerializer, NoteCardSerializer
from django.contrib.auth import authenticate
from .models import CustomUser, NoteCard
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()  # Make a mutable copy of the request data
        data['password'] = make_password(data['password'])  # Hash the password

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            user = None

        if user is None:
            return response.Response(
                {"error": "Email not found."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        user = authenticate(request, username=email, password=password)

        if user is None:
            return response.Response(
                {"error": "Incorrect password."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        token, _ = Token.objects.get_or_create(user=user)
        return response.Response({'token': token.key}, status=status.HTTP_200_OK)
        

class NoteCardCreateView(generics.CreateAPIView):
    queryset = NoteCard.objects.all()
    serializer_class = NoteCardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
