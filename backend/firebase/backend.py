import os

from backend.settings import BASE_DIR
from box.models import UserProfile

from rest_framework import authentication
from firebase_admin import auth, credentials, initialize_app

from .exceptions import *


cred = credentials.Certificate(os.path.join(BASE_DIR, "test_cred.json"))

default_app = initialize_app(cred)


class FirebaseBackend(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        #print(auth_header)
        if not auth_header:
            raise NoAuthToken("No auth token provided")

        id_token = auth_header.split(" ").pop()
        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise InvalidAuthToken("Invalid auth token")

        if not id_token or not decoded_token:
            return None

        try:
            uid = decoded_token.get("uid")
        except Exception:
            raise FirebaseError()

        user, created = UserProfile.objects.get_or_create(username=uid)

        return (user, None)