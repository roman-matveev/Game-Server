from django.db import models

class User(models.Model):
    name = models.CharField(max_length=15)
    id = models.AutoField(primary_key=True)
