from django.db import models

# Create your models here.
class PageModel(models.Model):
    """ A test model for future REST API"""
    image_url = models.CharField(max_length=200)
    page_id = models.IntegerField()
    video_duration = models.DateTimeField()