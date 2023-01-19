from django.db import models

# Create your models here.
class GPTRequest(models.Model):
    what = models.CharField(max_length=255)
    who = models.CharField(max_length=255)
