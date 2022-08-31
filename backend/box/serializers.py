from .models import Training, Trainer, Course, TrainerMessenger, Messenger
from rest_framework import serializers


class MessengerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Messenger
        fields = ('id', 'messenger', 'icon_url')


class TMSerializer(serializers.ModelSerializer):

    messenger = MessengerSerializer()

    class Meta:
        model = TrainerMessenger
        fields = ('messenger', 'nickname')


class TrainerSerializer(serializers.ModelSerializer):
    """Trainer table serializer"""

    messengers = TMSerializer(many=True, source='trainer_messenger')

    class Meta:
        model = Trainer
        fields = ('id', 'surname', 'name', 'patronymic', 'rating', 'experience', 'photo_url', 'messengers', 'info')
        

class TrainingSerializer(serializers.ModelSerializer):
    """Training table serializer"""

    class Meta:
        model = Training
        fields = ("__all__")
        

class TrainerShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trainer
        fields = ('id', 'surname', 'name', 'patronymic', 'photo_url')


class CourseSerializer(serializers.ModelSerializer):
    """Course serializer with short trainer info and all trainings in course nested"""

    # trainer_name = serializers.CharField(read_only=True, source="trainer.name")
    # trainer_surname = serializers.CharField(read_only=True, source="trainer.surname")
    # trainer_photo = serializers.CharField(read_only=True, source="trainer.photo_url")

    trainer = TrainerShortSerializer(read_only=True)
    trainings = TrainingSerializer(many=True)

    class Meta:
        model = Course
        depth=1
        fields = ('id', 'readiness', 'description', 'trainer', 'title', 'photo_url', 'exercise_amount', 'trainings')
