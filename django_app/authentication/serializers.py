# API/authentication/serializers.py
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import CustomUser, NoteCard

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']

        extra_kwargs = {
            'password': {'write_only': True}
        }

class NoteCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteCard
        fields = ['id', 'user', 'title', 'body']