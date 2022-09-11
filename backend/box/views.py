from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import TrainerSerializer, CourseSerializer, UnfinishedCourseSerializer
from .models import Course, Trainer


# Create your views here.
class GetCourseView(APIView):
    """Course view with trainer info and trainings"""

    def get(self, request):
        course_true = Course.objects.filter(readiness=True)
        serializer_true = CourseSerializer(course_true, many=True)

        course_false = Course.objects.filter(readiness=False)
        serializer_false = UnfinishedCourseSerializer(course_false, many=True) 

        return Response(serializer_true.data + serializer_false.data)


class GetTrainerView(APIView):
    """Trainer view"""

    def get(self, request):
        trainer = Trainer.objects.all()
        serializer = TrainerSerializer(trainer, many=True)
        return Response(serializer.data)