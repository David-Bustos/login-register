from django.db import models
from datetime import datetime
import bcrypt
import re

class UserManager(models.Manager):

    def register_validator(self, postData):
        errors = {}
        today=datetime.now().strftime('%Y-%m-%d')

        if User.objects.filter(email=postData['email']):
            errors['email'] = "This email already registered"

        if len(postData['fname']) < 2:
            errors['fname'] = "First name must have at least 2 characters"
        if len(postData['lname']) < 2:
            errors['lname'] = "Last name must have at least 2 characters"
        if len(postData['pass']) < 8:
            errors['pass'] = "Password must have at least 8 characters"
        if postData['date'] == '':
            errors['date'] = "Birthday is required"
        if postData['date'] > today:
            errors['date'] = "Birthday is not valid"

        return errors

    def login_validator(self, postData):
        errors = {}

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

