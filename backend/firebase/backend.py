import os
from time import timezone 

from box.models import UserProfile
from rest_framework import authentication
from firebase_admin import auth, credentials, initialize_app
from .exceptions import *


cred = credentials.Certificate(
    {
        "type": "service_account",
        "project_id": "genuine-airfoil-357313",
        "private_key_id": "fea03611f9cf03f2bfb26139150a82b28f69988c",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCepctstLhyH/Ex\n1XiLNhuGcYEp/EVrwT7RLUQI1b4uQJekLFnR2k+RHi3eMhEnkHNq45TR7PrkoCf7\n3p6V6kUBW8GKNfzVPbCkriZYDltYzSafLmlGjGRIRAWKezO2Q5FsN0D2DZC4ba5A\nXN8qj60SoY3R6JBZ5iWd9IfPlL+PET34mYCPfz/u+EGUi8/qHjgtUrVjYFY6iNEH\nhjRmiPce5s3YG3EOerE1wSOL2dy2zAa739+FIZ4VeLDpVBtYPXQsj5BFAQ2IiqfA\nt0/mdFEdvxHRVBYWVqzxYuaP6pBCEg24ei+KO0RY9gQc1CCFEQnPfkNZ4zG1AzAp\nJnskFNoHAgMBAAECggEAEFFzZCIOmsaIU5zmgkM1f5WrOHtXVKcS5Aco6VO69Rz1\nvBBHyNsQtheJlkJGG3CzPnpcM1+RyvRiSHj0jO0E3gfnF2VINVLcGYREM2h+otqv\nL05hy7zjD7/XZhAYGJZInf3s86IfkajOdJZY6hLPNYxifwXR2z1d/ypI0eQ18+wj\nl4rZk0OgLr/u2Q33rGt7iSCK+Vu0/1Bj9yzdHa5Q8Q9x5XN4H9Br9FEJqOlYc5TQ\nhmJ0jYURNYPZCE0I3SJbzm5FXKIKOg76xx/9pc7h0DVEg149eeKxt6XFajozlqkA\nciBvQOMZQjLOXM8lcKhf1qMfrwfcBVglinSsQmamyQKBgQDTRQApQkNajspX2j8I\niB1CjQpDuAFyIhlw1Z8K+ZTT4ln/wmNkAh9ZgSgbDw07jF1tmEMph4YHfObN3u1A\nHjp0XKmHV7EzItrQHOc8R7kFQuFzOHN4YlLd35Z1o3RvB51CEGlY2syNWyM9qj+0\nDCvRYBuVcN5o+F9c5Kg6zhRVZQKBgQDAPKO9/GmG4DGmZVC9HUxYOmOOMY3RB8le\nnc0F293l0GqDinHspLxrYyNrryfzC8ZbpcIyNoLWfQjidyBKJlTXTJKbtcZiHygV\nFP3ij9zYD5ywsBcoAlDqlu0FyrcAMalGbgrJMP7BHrVl40ZfVv1HXATTuqDxGST8\n56ubLE6g+wKBgQDJ0VdXEoqe3lqi08R1FPnGkk7k48jVy4c8B4U3ibXHNqo8rOgf\nJ/vkl4HFX3qHkQ3K3LID4QeC7ajZrwQ6xOWYNNBpjrain8AhIAswxV8UjJArbhi4\nPkzk0Gq9k9htG/v4mQ7Zp6HRwucGSDU0fI/7IfEXr8t2wRTv+ypNioFYFQKBgEry\nmWhF06KpH9Je58aDeLNhOFVEzqSzY3gHD9r76Jxj0FMuk9IOPAOmKDYgmPOyIIi0\nrGzFQed74g3hIe6m2ScDjJk2mnzA5vCpOX6uVgzKsW1VigGoPYHoi8pZSVXDBtsV\nphDgkEIcxd5OaK5dDOxYXO1rcrns8rXDYO1jrdgnAoGBAJs2/ZaV2il3M53BRbx+\nAe0advqrcW1Q7HVd6ArkK6xplUjU93p54v2JJY0hEHePHcPn2PkrWD/zmUvIeL7c\nKTzaPmO2elFIgBRN/lB7PmgbM9Pvv/S5jVKD7a/SfNXarqdux11x7OTGdkJsfjEc\n4u2Yj/Gn5SgsDdo42OC9FuhE\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-prtci@genuine-airfoil-357313.iam.gserviceaccount.com",
        "client_id": "112866968071335778736",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-prtci%40genuine-airfoil-357313.iam.gserviceaccount.com"
    }
)


default_app = initialize_app(cred)

uid = 'hnAYV5grCtSx8WD2VK9ifYw6BuK2'

custom_token = auth.create_custom_token(uid)
print(custom_token)

class FirebaseBackend(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        print(auth_header)
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