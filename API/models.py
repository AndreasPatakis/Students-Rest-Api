from django.db import models


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





class StudentData(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=420,unique=True)
    home_university = models.CharField(max_length=60)
    outgoing_university = models.CharField(max_length=60)
    register_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.name} {self.surname}'
