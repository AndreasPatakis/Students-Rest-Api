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


class StudentLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentUser
        fields = ['id','username','email','password']
        extra_kwargs = {
            'password':{
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.StudentUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )

        return user
