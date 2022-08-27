from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Messanger(models.Model):
    """Table for messanger icons"""
    
    #trainers = models.ManyToManyField(Trainer, through='TrainerMessanger')
    messanger = models.CharField(max_length=100)
    icon_url = models.TextField()

class Trainer(models.Model):
    """Trainer table. One trainer to many courses"""

    messangers = models.ManyToManyField(Messanger, through='TrainerMessanger')
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(5.0)]
        )
    experience = models.IntegerField()
    photo_url = models.TextField()

class Course(models.Model):
    """Course table. Many courses to one trainer. One course to many trainings"""

    trainer = models.ForeignKey(Trainer, related_name='courses', on_delete=models.CASCADE)
    description = models.TextField()
    excersize_amount = models.IntegerField()
    title = models.CharField(max_length=100)
    image_url = models.TextField()

class Training(models.Model):
    """Training table. Many trainings to one course"""

    course = models.ForeignKey(Course, related_name='trainings', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.TimeField()
    photo_url = models.TextField()
    video_url = models.TextField()

class TrainerMessanger(models.Model):
    """Connection table for many-to-many between Trainer table and Messanger table with nickname field for every trainer messanger"""

    trainer = models.ForeignKey(Trainer, related_name='trainer_messanger', on_delete=models.CASCADE)
    messanger = models.ForeignKey(Messanger, related_name='messanger_trainer', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
