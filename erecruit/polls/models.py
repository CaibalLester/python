# models.py
from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('agent', 'Agent'), ('applicant', 'Applicant')])
    password = models.CharField(max_length=100, validators=[MinLengthValidator(8)])

class Log(models.Model):
    username = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('agent', 'Agent'), ('applicant', 'Applicant')])
    password = models.CharField(max_length=100, validators=[MinLengthValidator(8)])

class Ail(models.Model):
    fullname = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)  # Assuming a 15-digit maximum for a contact number
    email = models.EmailField()
    sss_id = models.CharField(max_length=20)  # Adjust the max length as needed
    national_id = models.CharField(max_length=20)  # Adjust the max length as needed
    occupation = models.CharField(max_length=100)
    annual_salary = models.DecimalField(max_digits=10, decimal_places=2)


class Mal(models.Model):
    fullname = models.CharField(max_length=100)
    gender = models.CharField(max_length=500)
    age = models.PositiveSmallIntegerField(null=True, default='default_value')
    birthdate = models.DateTimeField(default=timezone.now, null=True)
    address = models.CharField(max_length=500)

class Help(models.Model):
    username = models.CharField(max_length=50, null=True, default='default_username')
    email = models.EmailField(max_length=254, null=True, blank=True, default='default_email')
    comments = models.TextField(blank=True, null=True, default='default_comments')
