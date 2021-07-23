from django.db import models


class StudentInfo(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50,unique=True)
    home_university = models.CharField(max_length=50)
    outgoing_university = models.CharField(max_length=50)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
