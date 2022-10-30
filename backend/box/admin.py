from django.contrib import admin
from .models import Trainer, Course, Training, Messenger, TrainerMessenger, UserProfile, TrainingUser, Exercise

# Register your models here.
admin.site.register(Trainer)
admin.site.register(Course)
admin.site.register(Training)
admin.site.register(Messenger)
admin.site.register(TrainerMessenger)
admin.site.register(UserProfile)
admin.site.register(TrainingUser)
admin.site.register(Exercise)