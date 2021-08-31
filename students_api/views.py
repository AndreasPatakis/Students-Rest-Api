from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from .serializers import StudentInfoSerializer, UserStudentSerializer, StudentNotesSerializer
from .models import StudentInfo, UserStudent, StudentNotes
from students_api import permissions


class StudentsInfoAPIView(APIView):
    serializer_class = StudentInfoSerializer

    def get(self, request):
        students_info = StudentInfo.objects.all()
        serializer = self.serializer_class(students_info, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class StudentInfoAPIView(APIView):

    def get_object_if_exists(self,id):
        try:
            return StudentInfo.objects.get(id=id)
        except StudentInfo.DoesNotExist:
            return False

    def get(self, request, id):
        student_info = self.get_object_if_exists(id)
        if not student_info:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)
        serializer = StudentInfoSerializer(student_info)
        return Response(serializer.data)

    def put(self, request, id):
        student_info = self.get_object_if_exists(id)
        if not student_info:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

        serializer = StudentInfoSerializer(student_info,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    #def patch(self, request, id):

    def delete(self, request, id):
        student_info = self.get_object_if_exists(id)
        if not student_info:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)
        student_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentsInfoViewSet(viewsets.ViewSet):
    serializer_class = StudentInfoSerializer

    def list(self, request):
        students_data = StudentInfo.objects.all()
        serializer = self.serializer_class(students_data, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, retrive, pk=None):
        queryset = StudentInfo.objects.all()
        students_data = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(students_data)
        return Response(serializer.data)


class UserStudentViewSet(viewsets.ViewSet):
    """Handles request associated with UserStudent model"""
    serializer_class = UserStudentSerializer

    #Permissions classes: you can usen only SAFE_METHODS and methods that are authenticated to use
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    #Allows as to search using any field we want
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('name','email',)

    def list(self, request):
        """Returns all the users"""
        users = UserStudent.objects.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        """Handles creating a user"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Return a user of a specific id"""
        queryset = UserStudent.objects.all()
        user_data = get_object_or_404(queryset,pk=pk)
        serializer = self.serializer_class(user_data)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """Deletes the user specified by id"""
        queryset = UserStudent.objects.all()
        user = get_object_or_404(queryset,pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class StudentNotesViewSet(viewsets.ViewSet):
    """Handles requests made for StudentNotes model"""
    serializer_class = StudentNotesSerializer

    #Permissions classes: you can usen only SAFE_METHODS and methods that are authenticated to use
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        permissions.UpdateOwnNotes,
        IsAuthenticated
        )

    def list(self, request):
        """Returns all the users"""
        users = StudentNotes.objects.filter(user_student=request.user)
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        """Handles creating a user"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(user_student=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Return a user of a specific id"""
        queryset = StudentNotes.objects.all()
        user_data = get_object_or_404(queryset,pk=pk)
        if user_data.user_student == request.user:
            serializer = self.serializer_class(user_data)
            return Response(serializer.data)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        """Deletes the user specified by id"""
        queryset = StudentNotes.objects.all()
        user = get_object_or_404(queryset,pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
