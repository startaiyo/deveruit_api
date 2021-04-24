from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from deveruit import serializers
from deveruit.models import Recruitment, Request, Message, User
from rest_framework import viewsets


class CreateUserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)

class RecruitmentViewSet(viewsets.ModelViewSet):
    queryset = Recruitment.objects.all()
    serializer_class = serializers.RecruitmentSerializer
    authentication_classes = (authentication.TokenAuthentication,)

    def perform_create(self, serializer):
        serializer.save(created_user=self.request.user)
    
class MyRecruitmentViewSet(viewsets.ModelViewSet):
    queryset = Recruitment.objects.all()
    serializer_class = serializers.RecruitmentSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    
    def get_queryset(self):
        return self.queryset.filter(created_user=self.request.user)


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = serializers.RequestSerializer
    authentication_classes = (authentication.TokenAuthentication,)

    def get_queryset(self):
        return self.queryset.filter(recruiter=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer
    authentication_classes = (authentication.TokenAuthentication,)

    def get_queryset(self):
        return self.queryset.filter(receiver=self.request.user)

