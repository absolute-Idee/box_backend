from django.contrib import admin
from .models import Trainer, Course, Training, Messenger, TrainerMessenger, User, TrainingUser

# Register your models here.
admin.site.register(Trainer)
admin.site.register(Course)
admin.site.register(Training)
admin.site.register(Messenger)
admin.site.register(TrainerMessenger)
admin.site.register(User)
admin.site.register(TrainingUser)