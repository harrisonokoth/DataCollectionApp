from django import forms
from .models import IntegrationConfig

class IntegrationConfigForm(forms.ModelForm):
    class Meta:
        model = IntegrationConfig
        fields = ['api_key', 'endpoint_url', 'parameters']
