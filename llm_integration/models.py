from django.db import models

class LLMModel(models.Model):
    """Model to store information about LLMs."""
    name = models.CharField(max_length=255)  # Name of the LLM
    version = models.CharField(max_length=50)  # Version of the LLM
    description = models.TextField(blank=True)  # Description of the LLM
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the model was added

    def __str__(self):
        return f"{self.name} (v{self.version})"


class IntegrationConfig(models.Model):
    """Model to store configuration settings for LLM integration."""
    llm_model = models.ForeignKey(LLMModel, related_name='configurations', on_delete=models.CASCADE)
    api_key = models.CharField(max_length=255)  # API key for LLM access
    endpoint_url = models.URLField()  # Endpoint URL for the LLM
    parameters = models.JSONField(blank=True, null=True)  # Parameters for API calls (as JSON)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the config was created

    def __str__(self):
        return f"Config for {self.llm_model.name}"


class LLMRequest(models.Model):
    """Model to store requests sent to the LLM."""
    config = models.ForeignKey(IntegrationConfig, related_name='requests', on_delete=models.CASCADE)
    input_text = models.TextField()  # Input text sent to the LLM
    output_text = models.TextField(blank=True)  # Response text from the LLM
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the request was made

    def __str__(self):
        return f"Request to {self.config.llm_model.name} on {self.created_at}"
