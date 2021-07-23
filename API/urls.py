from django.urls import path, include

from rest_framework.routers import DefaultRouter

from API import views

router = DefaultRouter()
router.register('studentData',views.StudentDataViewSet,base_name="studentData")

urlpatterns = [
    #path('login/',views.StudentLoginApiView.as_view()),
    path('register/',views.StudentRegisterApiView.as_view()),
    path('',include(router.urls))
]
