from rest_framework import serializers

from API import models

class StudentDataSerializer(serializers.ModelSerializer):
    """Serialiazes a StudentData type object"""

    class Meta:
        model = models.StudentData
        fields = ('id','name','surname','email','home_university','outgoing_university','register_date')
        extra_kwargs = {
            'register_date':{
                'read_only':True
            }
        }




# class StudentCredsSerializer(serializers.ModelSerializer):
#     """Serializes a StudentCreds type object"""
#
#     class Meta:
#         model = models.StudentCreds
#         fields = ('id', 'name', 'email', 'password')
#         #So it does not retrive password hash on GET requests
#         extra_kwargs = {
#             'password':{
#                 'write_only': True,
#                 'style': {'input_type': 'password'}
#             }
#         }
