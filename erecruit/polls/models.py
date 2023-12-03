# models.py
from django.db import models
from django.core.validators import MinLengthValidator

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('agent', 'Agent'), ('applicant', 'Applicant')])
    password = models.CharField(max_length=100, validators=[MinLengthValidator(8)])
