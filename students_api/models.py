from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.conf import settings



class UserStudentManager(BaseUserManager):
    """Manages the creation of a UserStudent"""

    #We have to overwrite the default create_user because we have changed the USERNAME_FIELD from name to email
    #Password set to none because if password is not given, then django handles the exception
    def create_user(self, email, name, password=None):
        """Creates a user"""
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(email=email, name=name)
        #set_password hashes the password
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates a superuser"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserStudent(AbstractBaseUser, PermissionsMixin):
    """Model for our UserStudent setup"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #"objects" is used by the cli to know how to handle users creation
    objects = UserStudentManager()

    #Because we use as a username field the email(name is the default), we have to specify it,
    #and also specify name as a required field because otherwise it won't be
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve the short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email


class StudentInfo(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50,unique=True)
    home_university = models.CharField(max_length=50)
    outgoing_university = models.CharField(max_length=50)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class StudentNotes(models.Model):
    """Student's Private Notes"""
    user_student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    note_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of the object"""
        return self.note_text
