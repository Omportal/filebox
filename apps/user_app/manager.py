# managers.py
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User
from django.db import models


class CustomUserManager(BaseUserManager):
    """Custom user model manager"""

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', False)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email: str, password: str, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        user = self.create_user(email=email, password=password, **extra_fields)
        return user
