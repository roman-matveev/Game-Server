from django.db import models

class Score(models.Model):
    score = models.IntegerField()
    id = models.IntegerField(primary_key=True)
