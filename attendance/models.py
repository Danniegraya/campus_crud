from django.db import models

class MultipleChoiceQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    choice_a = models.CharField(max_length=200)
    choice_b = models.CharField(max_length=200)
    choice_c = models.CharField(max_length=200)
    choice_d = models.CharField(max_length=200)
    correct_choice = models.CharField(max_length=1)

class OpenQuestion(models.Model):
    question_text = models.CharField(max_length=200)

class Answer(models.Model):
    question = models.ForeignKey(MultipleChoiceQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)