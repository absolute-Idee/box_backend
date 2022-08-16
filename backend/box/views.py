from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import TrainerSerializer, CourseSerializer
from .models import Course, Trainer


# Create your views here.
class GetCourseView(APIView):
    """Course view with trainer info and trainings"""

    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)


class GetTrainerView(APIView):
    """Trainer view"""

    def get(self, request):
        trainer = Trainer.objects.all()
        serializer = TrainerSerializer(trainer, many=True)
        return Response(serializer.data)