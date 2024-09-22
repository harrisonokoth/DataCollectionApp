from django.contrib import admin
from .models import DataSet, DataPreprocessingStep, DataTransformation

admin.site.register(DataSet)
admin.site.register(DataPreprocessingStep)
admin.site.register(DataTransformation)
