from django.db import models

class DataSet(models.Model):
    """Model to store information about datasets."""
    name = models.CharField(max_length=255)  # Name of the dataset
    description = models.TextField(blank=True)  # Description of the dataset
    file_path = models.FileField(upload_to='datasets/')  # Path to the uploaded dataset file
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the dataset was uploaded

    def __str__(self):
        return self.name


class DataPreprocessingStep(models.Model):
    """Model to store preprocessing steps applied to datasets."""
    dataset = models.ForeignKey(DataSet, related_name='preprocessing_steps', on_delete=models.CASCADE)
    step_name = models.CharField(max_length=255)  # Name of the preprocessing step
    parameters = models.JSONField(blank=True, null=True)  # Parameters used in the step (as a JSON)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the step was created

    def __str__(self):
        return f"{self.step_name} for {self.dataset.name}"


class DataTransformation(models.Model):
    """Model to store details about data transformations."""
    preprocessing_step = models.ForeignKey(DataPreprocessingStep, related_name='transformations', on_delete=models.CASCADE)
    transformation_type = models.CharField(max_length=255)  # Type of transformation (e.g., normalization)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the transformation was created

    def __str__(self):
        return f"{self.transformation_type} for {self.preprocessing_step.step_name}"
