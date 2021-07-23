from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin


# class StudentCredsManager(model.Model):
#     """Manager of Student object"""
#
#     def create_user(self, name, email, password=None):
#         """Create a Student user"""
#         if not email:
#             raise ValueError("User must have an email")
#
#         email = self.normalize_email(email)
#         user = self.model(name, email)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
# class StudentCreds(models.Model):
#     name = models.CharField(max_length=30)
#     email = models.EmailField(max_length=420,unique=True)
#     is_staff = models.BooleanField(default=False)
#
#     objects = StudentCredsManager():
#
#
#     def __str__(self):
#         """Return string representation of user"""
#         return self.email


class StudentRegisterManager(BaseUserManager):
    """Manager of Student object"""

    def create_user(self, name, email, password=None):
        """Overrides Create User"""
        if not email:
            raise ValueError("User must have an email")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password):
        """Overrides CreateSuperUser"""
        user = self.create_user(name,email,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user




class StudentRegister(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=420, unique=True)
    is_staff = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    objects = StudentRegisterManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
    def __str__():
        return self.email



class StudentData(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=420,unique=True)
    home_university = models.CharField(max_length=60)
    outgoing_university = models.CharField(max_length=60)


    def __str__(self):
        return f'{self.name} {self.surname}'
