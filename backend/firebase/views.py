from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User
from firebase.serializers import UserSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .backend import FirebaseBackend


# Create your views here.
class TestAuthView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request):
        a = FirebaseBackend.authenticate(self=self, request=request)
        if a is None:
            return Response({'test':'None'})
        else:
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data)
        