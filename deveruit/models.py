from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, github_name, password=None, **extra_fields):

        if not github_name:
            raise ValueError('Users must have a github name')
 
        user = self.model(github_name=github_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, github_name, password=None):
        
        user = self.create_user(github_name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        max_length=255,
    )
    github_name = models.CharField(max_length=100, unique=True)
    image = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
 
    objects = UserManager()
 
    USERNAME_FIELD = 'github_name'
 
    def __str__(self):
        return self.github_name


class Recruitment(models.Model):
    created_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='created_user',
        on_delete=models.CASCADE
    )
    img = models.ImageField(blank=True, null=True, upload_to='image/')
    detail = models.TextField()
    approval_msg = models.CharField(max_length=200)
    refusal_msg = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.created_user

class Request(models.Model):
    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='applicant',
        on_delete=models.CASCADE
    )
    recruiter = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='recruiter',
        on_delete=models.CASCADE
    )
    is_approved = models.BooleanField(default=False)
    is_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('applicant', 'recruiter'),)

    def __str__(self):
        return str(self.applicant)

class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='sender',
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='receiver',
        on_delete=models.CASCADE
    )
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return str(self.sender)
