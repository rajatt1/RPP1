from django.db import models

# Create your models here.
class projectM(models.Model):
    project_name = models.CharField(max_length=200, unique=True, null=False)
    project_ID = models.AutoField(primary_key=True)

    def __str__(self):
        return f"project_name: {self.project_name}, project_ID: {self.project_ID}"
    