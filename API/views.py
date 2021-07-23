from django.shortcuts import render
from rest_framework import viewsets
from API import serializers
from API import models
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.views import APIView



#
# class StudentLoginApiView(ObtainAuthToken):
#     renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class StudentRegisterApiView(APIView):
    """Create account API"""
    def post(self, request):
        serializer = serializers.StudentRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.create()
            data['response'] = 'Successfully Registered!'
        else:
            data = serializer.errors
        return Response(data)



class StudentDataViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.StudentDataSerializer
    queryset = models.StudentData.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

    def perform_create(self, serializer):
        serializer.save()
