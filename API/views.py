from django.shortcuts import render
from rest_framework import viewsets
from API import serializers
from API import models
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings



class StudentLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class StudentDataViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.StudentDataSerializer
    queryset = models.StudentData.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

    def perform_create(self, serializer):
        serializer.save()
