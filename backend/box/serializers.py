from pyexpat import model
from .models import Training, Trainer, Course, TrainerMessanger, Messanger
from rest_framework import serializers


class MessangerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Messanger
        fields = ('id', 'messanger', 'icon_url')


class TMSerializer(serializers.ModelSerializer):

    messanger = MessangerSerializer()

    class Meta:
        model = TrainerMessanger
        fields = ('messanger', 'nickname')


class TrainerSerializer(serializers.ModelSerializer):
    """Trainer table serializer"""

    messangers = TMSerializer(many=True, source='trainer_messanger')

    class Meta:
        model = Trainer
        fields = ('id', 'surname', 'name', 'patronymic', 'rating', 'experience', 'photo_url', 'messangers')
        


class TrainingSerializer(serializers.ModelSerializer):
    """Training table serializer"""

    class Meta:
        model = Training
        fields = ("__all__")
        

class TrainerShortSerializer(serializers.Serializer):
    trainer_name = serializers.CharField(read_only=True)
    trainer_surname = serializers.CharField(read_only=True)
    trainer_photo = serializers.CharField(read_only=True)


class CourseSerializer(serializers.ModelSerializer):
    """Course serializer with short trainer info and all trainings in course nested"""

    # trainer_name = serializers.CharField(read_only=True, source="trainer.name")
    # trainer_surname = serializers.CharField(read_only=True, source="trainer.surname")
    # trainer_photo = serializers.CharField(read_only=True, source="trainer.photo_url")

    # def __init__(self, data, *args, **kwargs):
    #     self.data = data
    #     super().__init__(*args, **kwargs)



    trainer_short = TrainerShortSerializer()
    trainings = TrainingSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'description', 'trainer', 'title', 'image_url', 'trainings')
