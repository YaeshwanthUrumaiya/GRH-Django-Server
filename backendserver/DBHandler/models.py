from django.db import models

class GameUserData(models.Model):
    Id = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=100)
    GameName = models.CharField(max_length=100)
    DateTime = models.DateField()
    Values = models.JSONField(default=dict) 

# Create your models here.
