from django.urls import path
from .views import TestAuthView

app_name = "firebase"

urlpatterns = [
    path('Test/', TestAuthView.as_view(), name='put_test'),
]