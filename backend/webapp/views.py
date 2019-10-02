# -*- coding: utf-8 -*-
import random
from django.http import JsonResponse
from webapp.mixins import APIViewMixin
from questions.models import Question
from users.models import User

# /question - receive a username and return a question
# /answer - receive a username and a answer and return if right or wrong

class QuestionView(APIViewMixin):
    post_services = ("get_question", )
    get_services = ("get_question", )
    model = Question

    def _get_question(self, data):
        response = {}
        
        # Check if the username was provided and start or create the object
        username = data.get("username")
        if username:
            username_query = User.objects.all().filter(
                username=username
            )
            if len(username_query) > 0:
                user = username_query[0]
            else:
                user = User(
                    username=username,
                    answered={ "count" : 0, "questions": [] }
                )
                user.save()

            # Get a random new question
            answered = user.answered
            keep = False
            while not keep:
                all_questions = self.model.objects.all().filter(
                    dificulty__lte=user.dificulty_range()
                )
                picked = random.sample(list(all_questions), 1)[0]
                if not picked.id in answered["questions"]:
                    keep = True
                
                response = picked.expose()
        else:
            response["message"] = "Not enough parameters"


        return response
        
