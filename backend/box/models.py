from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Messenger(models.Model):
    """Table for messenger icons"""
    
    #trainers = models.ManyToManyField(Trainer, through='TrainerMessenger')
    messenger_name = models.CharField(max_length=100)
    icon_url = models.TextField()

class Trainer(models.Model):
    """Trainer table. One trainer to many courses"""

    messengers = models.ManyToManyField(Messenger, through='TrainerMessenger')
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
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

class UserProfile(models.Model):
    """User table"""

    #user = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    username = models.TextField()
    phone_num = models.CharField(max_length=20)
    email = models.TextField()

class Training(models.Model):
    """Training table. Many trainings to one course"""
    user = models.ManyToManyField(UserProfile, through='TrainingUser')
    course = models.ForeignKey(Course, related_name='trainings', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    photo_url = models.TextField()
    description = models.TextField()
    duration = models.IntegerField(blank=True, default=60)

class Exercise(models.Model):
    """Exercise table. Many exercises to one Training"""
    class Choises(models.IntegerChoices):
        LECTURE = 0
        PRACTICE = 1

    training = models.ForeignKey(Training, related_name='exercises', on_delete=models.CASCADE)
    exercise_type = models.IntegerField(choices=Choises.choices, blank=True, default=1)
    duration = models.IntegerField(blank=True, default=60)
    video_url = models.TextField()
    video_ratio = models.FloatField(default=0.5)

class TrainerMessenger(models.Model):
    """Connection table for many-to-many between Trainer table and Messenger table with nickname field for every trainer messenger"""

    trainer = models.ForeignKey(Trainer, related_name='trainer_messenger', on_delete=models.CASCADE)
    messenger = models.ForeignKey(Messenger, related_name='messenger_trainer', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)

class TrainingUser(models.Model):
    """Connection table for many-to-many relationship. Also uses for like count"""

    user = models.ForeignKey(UserProfile, related_name='user_training', on_delete=models.CASCADE)
    training = models.ForeignKey(Training, related_name='training_user', on_delete=models.CASCADE)
    like_status = models.BooleanField()