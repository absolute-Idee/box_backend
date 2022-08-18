from .models import Training, Trainer, Course
from rest_framework import serializers


class TrainerSerializer(serializers.ModelSerializer):
    """Trainer table serializer"""

    class Meta:
        model = Trainer
        fields = ("__all__")


class TrainingSerializer(serializers.ModelSerializer):
    """Training table serializer"""

    class Meta:
        model = Training
        fields = ("__all__")


class CourseSerializer(serializers.ModelSerializer):
    """Course serializer with short trainer info and all trainings in course nested"""

    trainer_name = serializers.CharField(read_only=True, source="trainer.name")
    trainer_surname = serializers.CharField(read_only=True, source="trainer.surname")
    trainer_photo = serializers.CharField(read_only=True, source="trainer.photo_url")
    trainings = TrainingSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'description', 'trainer', 'trainer_name', 'trainer_surname', 'trainer_photo', 'title', 'image_url', 'trainings')
