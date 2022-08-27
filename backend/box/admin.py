from django.contrib import admin
from .models import Trainer, Course, Training, Messanger, TrainerMessanger

# Register your models here.
admin.site.register(Trainer)
admin.site.register(Course)
admin.site.register(Training)
admin.site.register(Messanger)
admin.site.register(TrainerMessanger)