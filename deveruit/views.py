from django.shortcuts import render
from rest_framework import generics, authentication, permissions
from deveruit import serializers
from deveruit.models import Recruitment, Request, Message, User
from rest_framework import viewsets
from . import models
from django.http import JsonResponse

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

def msg_create(request,request_id):
    msg = Message.objects.create(request_id=request_id)
    req = Request.objects.get(id=request_id)
    recruitment = Recruitment.objects.get(id=req.recruit_id)
    if req.is_approved:
        msg.message = recruitment.approval_msg
    else:
        msg.message = recruitment.refusal_msg
    if msg.is_valid:
        msg.save()
    selializer = MessageSerializer(msg)
    return JsonResponse(selializer.data)
