from rest_framework import serializers

from API import models

class StudentDataSerializer(serializers.ModelSerializer):
    """Serialiazes a StudentData type object"""

    class Meta:
        model = models.StudentData
        fields = ('id','name','surname','email','home_university','outgoing_university',)
        extra_kwargs = {
            'register_date':{
                'read_only':True
            }
        }


class StudentRegisterSerializer(serializers.ModelSerializer):
    """Serializes StudentRegister type data"""
    password2 = serializers.CharField(max_length=30,style={'input_type':'password'},write_only=True)
    class Meta:
        model = models.StudentRegister
        fields = ('name', 'email', 'password', 'password2')
        extra_kwargs = {
            'password':{
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self):
        """Create new user"""
        email=validated_data['email'],
        name=validated_data['name'],
        password=validated_data['password']
        if user.password != user.password2:
            raise serializers.ValidationError({"Password":"Passwords must match"})
        else:
            user = models.StudentRegister.objects.create_user(name,email,password)
        return user




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
