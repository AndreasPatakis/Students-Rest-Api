from rest_framework import serializers
from students_api import models


class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentInfo
        fields = ['id','first_name','last_name','email','home_university','outgoing_university','created_on']
        extra_kwargs = {
            'created_on':{
                'read_only':True
            }
        }


class UserStudentSerializer(serializers.ModelSerializer):
    """Serializer for UserStudent model"""
    class Meta:
        model = models.UserStudent
        fields = ['id','name', 'email', 'password']
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """We overwrite create method so that we use our custom create_user from UserStudent model"""
        user = models.UserStudent.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """We overwrite update method so it hashes the password"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class StudentNotesSerializer(serializers.ModelSerializer):
    """Serializer for the StudentNotes model"""
    class Meta:
        model = models.StudentNotes
        fields = ('id','user_student', 'note_text', 'created_on')
        extra_kwargs = {
            'user_student':{'read_only':True}
        }
