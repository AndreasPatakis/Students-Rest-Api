from django.contrib import admin
from students_api import models


admin.site.register(models.StudentInfo)
admin.site.register(models.UserStudent)
admin.site.register(models.StudentNotes)
