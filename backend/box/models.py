from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Messenger(models.Model):
    """Table for messenger icons"""
    
    #trainers = models.ManyToManyField(Trainer, through='TrainerMessenger')
    messenger = models.CharField(max_length=100)
    icon_url = models.TextField()

class Trainer(models.Model):
    """Trainer table. One trainer to many courses"""

    messengers = models.ManyToManyField(Messenger, through='TrainerMessenger')
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5.0)]
        )
    experience = models.IntegerField()
    photo_url = models.TextField()
    info = models.TextField()

class Course(models.Model):
    """Course table. Many courses to one trainer. One course to many trainings"""

    trainer = models.ForeignKey(Trainer, related_name='courses', on_delete=models.CASCADE)
    description = models.TextField()
    exercise_amount = models.IntegerField()
    title = models.CharField(max_length=100)
    photo_url = models.TextField()
    readiness = models.BooleanField(default=True)

class Training(models.Model):
    """Training table. Many trainings to one course"""

    course = models.ForeignKey(Course, related_name='trainings', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.TimeField()
    photo_url = models.TextField()
    video_url = models.TextField()
    video_ratio = models.FloatField(default=0.5)

class TrainerMessenger(models.Model):
    """Connection table for many-to-many between Trainer table and Messenger table with nickname field for every trainer messenger"""

    trainer = models.ForeignKey(Trainer, related_name='trainer_messenger', on_delete=models.CASCADE)
    messenger = models.ForeignKey(Messenger, related_name='messenger_trainer', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
