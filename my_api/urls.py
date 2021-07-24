from django.urls import path
from my_api import views

urlpatterns=[
    path('login/',views.StudentLoginAPIView.as_view()),
    path('infos/',views.StudentsInfoAPIView.as_view()),
    path('info/<int:id>/',views.StudentInfoAPIView.as_view())
]
