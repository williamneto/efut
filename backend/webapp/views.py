# -*- coding: utf-8 -*-
from django.http import JsonResponse
from webapp.mixins import APIViewMixin
from questions.models import Question

# /question - receive a username and return a question
# /answer - receive a username and a answer and return if right or wrong

class QuestionView(APIViewMixin):
    post_services = ("get_question", )
    get_services = ("get_question", )
    model = Question

    def _get_question(self, data):
        #data = {"eeeeiiita": "Booomm"}       

        return data
        
