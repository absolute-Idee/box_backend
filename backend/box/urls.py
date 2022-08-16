from django.urls import path
from .views import GetCourseView, GetTrainerView

app_name = "box"

urlpatterns = [
    path('GetCourse/', GetCourseView.as_view()),
    path('GetTrainer/', GetTrainerView.as_view()),
]