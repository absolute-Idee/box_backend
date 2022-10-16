from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import TrainerSerializer, CourseSerializer, UnfinishedCourseSerializer
from .models import Course, Trainer

from firebase.backend import FirebaseBackend


# Create your views here.
class GetCourseView(APIView):
    """Course view with trainer info and trainings"""

    def get(self, request):
        a = FirebaseBackend.authenticate(self=self, request=request)
        if a:
            course_true = Course.objects.filter(readiness=True)
            serializer_true = CourseSerializer(course_true, many=True)

            course_false = Course.objects.filter(readiness=False)
            serializer_false = UnfinishedCourseSerializer(course_false, many=True) 

            return Response(serializer_true.data + serializer_false.data)
        else:
            return Response({'Error':'Wrong Auth'})


class GetTrainerView(APIView):
    """Trainer view"""

    def get(self, request):
        a = FirebaseBackend.authenticate(self=self, request=request)
        if a:
            trainer = Trainer.objects.all()
            serializer = TrainerSerializer(trainer, many=True)
            return Response(serializer.data)
        else:
            return Response({'Error':'Wrong Auth'})