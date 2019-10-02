# -*- coding: utf-8 -*-
from django.db import models
from django_mysql.models import Model, JSONField

QUESTION_TYPES = (
    ("0", "Relational"),
    ("1", "Math"),
    ("2", "Comparative")
)
class Question(Model):
    statement = models.CharField(
        max_length=300
    )
    hint = models.CharField(
        max_length=300,
        null=True
    )
    answer = models.CharField(
        max_length=300
    )
    type = models.CharField(
        max_length=300,
        choices=QUESTION_TYPES
    )
    origin = JSONField()

    def __str__(self):
        return self.statement
    
    def to_json(self):
        data = {
            "id": self.id,
            "statement": self.statement,
            "hint": self.hint,
            "answer": self.answer,
            "type": self.type
        }

        return data
    
