# -*- coding: utf-8 -*-
from django.db import models
from django_mysql.models import Model, JSONField

class User(Model):
    username = models.CharField(
        max_length=300
    )
    points = models.IntegerField(
        default=0
    )
    answered = JSONField()
    
    def dificulty_range(self):
        dificulty = 0
        answered_questions = self.answered["count"]

        if answered_questions <= 10:
            dificulty = 2
        elif answered_questions <= 20:
            dificulty = 3
        elif answered_questions <= 30:
            dificulty = 4
        else:
            dificulty = 5
        
        return dificulty

    def __str__(self):
        return self.username
