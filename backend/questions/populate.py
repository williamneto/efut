# -*- coding: utf-8 -*-
from django.db.models import Q
from questions.questions import TeamRelationalQuestion
from questions.models import Question
from football.models import Team

fields = ["venue_city", "founded", "logo"]

def create_relational_questions():
    teams = Team.objects.all()
    for team in teams:
        #import pdb; pdb.set_trace()
        if team.venue_city and team.founded and team.logo:
            for field in fields:
                origin = {
                    "team_id": team.id,
                    "field": field
                }
                quest = TeamRelationalQuestion(origin)
                question = quest.to_model()


                question.save()
                print(">>>> Salva pergunta '%s'" % question.statement)
