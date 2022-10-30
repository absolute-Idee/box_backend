from django.urls import path
from .views import GetCourseView, GetTrainerView, GetCourseByIdView, GetTrainerByIdView

app_name = "box"

urlpatterns = [
    path('GetCourse/', GetCourseView.as_view(), name='get_course'),
    path('GetTrainer/', GetTrainerView.as_view(), name='get_trainer'),
    
    path('GetCourse/<int:pk>', GetCourseByIdView.as_view(), name='get_course_by_id'),
    path('GetTrainer/<int:pk>', GetTrainerByIdView.as_view(), name='get_trainer_by_id'),
]