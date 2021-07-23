from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import StudentInfoSerializer
from .models import StudentInfo


class StudentsInfoAPIView(APIView):
    def get(self, request):
        students_info = StudentInfo.objects.all()
        serializer = StudentInfoSerializer(students_info, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentInfoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.Data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class StudentInfoAPIView(APIView):

    def get_object_if_exists(self):
        try:
            return StudentInfo.objects(id=id)
        except StudentInfo.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        student_info = self.get_object_if_exists()
        serializer = StudentInfoSerializer(student_info)
        return Response(serializer.data)
