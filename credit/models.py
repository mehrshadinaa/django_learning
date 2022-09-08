from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)

    def __str__(self):
        return '{}-token'.format(self.user)


class Expense(models.Model):
    question_text = models.CharField(max_length=200)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.question_text
