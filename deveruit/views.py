from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from deveruit import serializers
from deveruit.models import Recruitment, Request, Message
from rest_framework import viewsets


class CreateUserView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer

class RecruitmentViewSet(viewsets.ModelViewSet):
    queryset = Recruitment.objects.all()
    serializer_class = serializers.RecruitmentSerializer


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = serializers.RequestSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer

