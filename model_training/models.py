from django.db import models

class ModelTrainingJob(models.Model):
    """Model to store information about model training jobs."""
    model_name = models.CharField(max_length=255)  # Name of the model being trained
    training_data_path = models.FileField(upload_to='training_data/')  # Path to the training dataset
    hyperparameters = models.JSONField(blank=True, null=True)  # Hyperparameters for training
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the job was created
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ], default='pending')  # Status of the training job

    def __str__(self):
        return f"Training Job for {self.model_name} - Status: {self.status}"


class TrainedModel(models.Model):
    """Model to store information about trained models."""
    training_job = models.OneToOneField(ModelTrainingJob, related_name='trained_model', on_delete=models.CASCADE)
    model_file = models.FileField(upload_to='trained_models/')  # Path to the saved model file
    accuracy = models.FloatField()  # Accuracy of the trained model
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the model was created

    def __str__(self):
        return f"{self.training_job.model_name} - Accuracy: {self.accuracy}"


class ModelEvaluation(models.Model):
    """Model to store evaluation results of trained models."""
    trained_model = models.ForeignKey(TrainedModel, related_name='evaluations', on_delete=models.CASCADE)
    evaluation_metric = models.CharField(max_length=50)  # Name of the evaluation metric (e.g., 'accuracy')
    metric_value = models.FloatField()  # Value of the evaluation metric
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the evaluation was done

    def __str__(self):
        return f"Evaluation of {self.trained_model.training_job.model_name} - {self.evaluation_metric}: {self.metric_value}"
