from django.contrib import admin
from .models import LLMModel, IntegrationConfig, LLMRequest

admin.site.register(LLMModel)
admin.site.register(IntegrationConfig)
admin.site.register(LLMRequest)
