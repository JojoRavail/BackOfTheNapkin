from django.db import models

# Create your models here.
class CoreModel(models.Model):
    request_id = models.CharField(max_length=255,primary_key=True)
    user = models.ForeignKey(Users,on_delete=models.CASCADE))
    what = models.CharField(max_length=255)
    who = models.CharField(max_length=255)
    answered=models.BooleanField(default=False)
    answer_sent=models.BooleanField(default=False)
