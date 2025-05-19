from django.db import models

# Create your models here.
class Problem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=10000,default="No description provided.")
    code = models.CharField(max_length=20, unique=True)
    difficulty = models.CharField(
        max_length=10,
        blank=True,
        choices=[("Hard", "Hard"), ("Easy", "Easy"), ("Medium", "Medium")],
    )

class CodeSubmission(models.Model):
    language = models.CharField(max_length=100)
    code = models.TextField()
    input_data = models.TextField(null=True,blank=True)
    output_data = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    