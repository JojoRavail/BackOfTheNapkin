from django.db import models
from django.contrib.auth.models import Users

# Create your models here.
class CoreModel(models.Model):
    
    request_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    request_field_1 = models.CharField(max_length=255)
    request_field_2 = models.CharField(max_length=255)
    answered=models.BooleanField(default=False)
    answer_sent=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
