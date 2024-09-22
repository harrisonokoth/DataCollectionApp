from django.contrib import admin
from .models import ModelTrainingJob, TrainedModel, ModelEvaluation

admin.site.register(ModelTrainingJob)
admin.site.register(TrainedModel)
admin.site.register(ModelEvaluation)
