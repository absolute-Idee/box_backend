from .models import Training, Trainer, Course, TrainerMessenger, Messenger, TrainingUser, Exercise
from rest_framework import serializers


class MessengerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Messenger
        fields = ('id', 'messenger_name', 'icon_url')


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


class ExerciseSerializer(serializers.ModelSerializer):
    """Exercise table serializer"""

    class Meta:
        model = Exercise
        fields = ('id', 'exercise_type', 'duration', 'video_url', 'video_ratio')


class TrainingSerializer(serializers.ModelSerializer):
    """Training table serializer. Likes field count users in training whose like_status is True, that is likes amount in the training"""

    likes = serializers.SerializerMethodField() 
    exercises = ExerciseSerializer(many=True)

    @staticmethod
    def get_likes(obj):
        return TrainingUser.objects.filter(training_id=obj.id, like_status=True).count()

    class Meta:
        model = Training
        fields = ('id', 'title', 'description', 'likes', 'photo_url', 'exercises', 'duration')
        

class TrainerShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trainer
        fields = ('id', 'surname', 'name', 'patronymic', 'photo_url')


class UnfinishedCourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    readiness = serializers.BooleanField()
    photo_url = serializers.CharField(style={'base_template': 'textarea.html'})
    title = serializers.CharField(max_length=100)


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
