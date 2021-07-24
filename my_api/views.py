from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import StudentInfoSerializer, StudentLoginSerializer
from .models import StudentInfo, StudentUser


class StudentsInfoAPIView(APIView):
    def get(self, request):
        students_info = StudentInfo.objects.all()
        serializer = StudentInfoSerializer(students_info, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentInfoSerializer(data=request.data)

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


class StudentLoginAPIView(APIView):

    def get(self, request):
        student_users = StudentUser.objects.all()
        serializer = StudentLoginSerializer(student_users, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = StudentLoginSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
