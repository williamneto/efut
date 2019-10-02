# -*- coding: utf-8 -*-
from football.models import Team
from questions.models import Question

class TeamRelationalQuestion:
    model = Question
    statement = None
    hint = None
    answer = None
    options = None
    origin = None
    valid_origin = False

    # An answer origin field for a relational question is one of the folowing Team attribute:
    # - venue_city
    # - founded
    # - logo
    # An answer origin id for a relational question is the one Team id
    def __init__(self, origin):
        # Working with the internal team_id, not the external from the API
        if origin.get("team_id") and origin.get("field"):
            self.origin = origin
            self.valid_origin = True

            self.formulate()
    
    def formulate(self):
        if self.valid_origin:
            team = Team.objects.get(
                id=self.origin["team_id"]
            )

            if self.origin["field"] == "venue_city":
                self.statement = "Onde fica o estádio do %s?" % team.name
                self.answer = team.venue_city
            elif self.origin["field"] == "founded":
                self.statement = "Em que ano foi fundado o clube %s?" % team.name
                self.answer = team.founded
            elif self.origin["field"] == "logo":
                self.statement = "Este é o escudo de qual time?"
                self.answer = team.name
                self.hint = team.logo
        else:
            self.statement = "Invalid origin"
        
    def to_model(self):
        question = self.model(
            statement=self.statement,
            hint=self.hint,
            answer=self.answer,
            type="0",
            origin=self.origin
        )

        return question

        

    