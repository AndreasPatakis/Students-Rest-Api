from django.urls import path, include
from students_api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('students_info',views.StudentsInfoViewSet, basename='students_info')
router.register('users', views.UserStudentViewSet, basename='users')
router.register('notes', views.StudentNotesViewSet, basename='notes')


urlpatterns=[
    path('viewset/', include(router.urls)),
    path('login/',views.UserLoginApiView.as_view()),
    path('infos/',views.StudentsInfoAPIView.as_view()),
    path('info/<int:id>/',views.StudentInfoAPIView.as_view())
]
