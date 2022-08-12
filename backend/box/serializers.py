from box.models import PageModel
from rest_framework import serializers


class PageModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    image_url = serializers.CharField(max_length=200)
    page_id = serializers.IntegerField()
    video_duration = serializers.DateTimeField()