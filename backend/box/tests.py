from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from .models import Trainer, Course, Training
from .serializers import CourseSerializer, TrainerSerializer


class TestTrainerModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        Trainer.objects.create(surname='Urbaev', name='Max', patronymic='Gennadievich', rating=4.4, experience=2, photo_url='fJSNjndnSfs')

    def test_model_fields(self):
        trainer = Trainer.objects.get(id=1)
        self.assertEqual(trainer.name, 'Max')
        self.assertEqual(trainer.rating, 4.4)
        self.assertEqual(trainer.experience, 2)


class TestGeetTrainers(APITestCase):

    @classmethod
    def setUpTestData(cls):
        Trainer.objects.create(surname='Urbaev', name='Max', patronymic='Gennadievich', rating=4.4, experience=2, photo_url='fJSNjndnSfs')
        # Course.objects.create(trainer_id=1, description='first course', excersize_amount=1, title='Trainer 1 course')
        # Training.objects.create(course_id=1, title='punches', description='punches training', duration='00:15:12')

    def test_get_trainer(self):
        response = self.client.get(reverse('box:get_trainer'))
        trainers = Trainer.objects.all()
        print(trainers.values())
        serializer = TrainerSerializer(trainers, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
