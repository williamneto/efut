# -*- coding: utf-8 -*-
import random
from django.http import JsonResponse
from django.db.models import Q
from webapp.mixins import APIViewMixin
from football.models import Team
from questions.models import Question
from users.models import User

class RankView(APIViewMixin):
    post_services = ("get_rank")

    def _get_rank(self, data):
        response = {
            "rank": []
        }

        all_users = User.objects.all().order_by("-points")
        for user in all_users[:5]:
            response["rank"].append({
                "username": user.username,
                "points": user.points
            })

        return response

class UserView(APIViewMixin):
    post_services = ("get_user_points")
    
    def _get_user_points(self, data):
        response = {}
        username = data.get("username")

        if username:
            user_query = User.objects.all().filter(
                username=username
            )
            if len(user_query) > 0:
                response["points"] = user_query[0].points
        
        return response

# /question - receive a username and return a question
# /answer - receive a username and a answer and return if right or wrong

class QuestionView(APIViewMixin):
    post_services = ("get_question", "answer_question")
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

                if picked.type == "0":
                    origin = picked.origin
                    
                    option_teams = random.sample(list(Team.objects.filter()), 2)
                    options = [picked.answer]
                    for t in option_teams:
                        if origin["field"] == "logo":
                            options.append(t.name)
                        else:
                            options.append(t.to_json()[origin["field"]])
                    
                    response = { 
                        "question": picked.expose(),
                        "options": random.sample(options, len(options))
                    }
        else:
            response["message"] = "Not enough parameters"

        return response
    
    def _answer_question(self, data):
        response =  {}

        username = data.get("username")
        question_id = data.get("question_id")
        user_answer = data.get("answer")
        if username and question_id and user_answer:
            question = self.model.objects.get(id=question_id)
            user = User.objects.all().filter(
                username=username
            )[0]
            answered = user.answered
            if not question.id in answered["questions"]:
                if question.answer == user_answer:
                    answered["count"] += 1
                    answered["questions"].append(question.id)
                    user.answered = answered
                    user.points += 10
                    user.save()

                    response["correct"] = True
                    response["user_points"] = user.points
                else:
                    if user.points >= 10:
                        user.points -= 5
                        user.save()

                    response["correct"] = False
                    response["points"] = user.points

        else:
            response["message"] = "Not enough parameters"
        
        return response
        
