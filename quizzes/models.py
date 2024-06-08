from django.db import models

class Answer(models.Model):
    question_id = models.IntegerField()
    answer = models.CharField(max_length=200)