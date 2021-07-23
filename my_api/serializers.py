from rest_framework import serializers
from my_api import models


class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentInfo
        fields = ['id','first_name','last_name','email','home_university','outgoing_university','created_on']
        extra_kwargs = {
            'created_on':{
                'read_only':True
            }
        }
