# -*- coding: utf-8 -*-
from django_mysql.models import Model, JSONField
from django.db import models

class League(models.Model):
    league_id = models.IntegerField()
    name = models.CharField(
        max_length=300
    )
    type = models.CharField(
        max_length=300
    )
    country = models.CharField(
        max_length=300
    )
    country_code = models.CharField(
        max_length=300,
        null=True
    )
    season = models.IntegerField()
    season_start = models.DateField()
    season_end = models.DateField()
    logo = models.CharField(
        max_length=600,
        null=True
    )
    flag = models.CharField(
        max_length=600,
        null=True
    )
    standings = models.IntegerField()
    is_current = models.IntegerField()

    def __str__(self):
        return "%s - %s" % (self.name, self.season)
    
    def to_json(self):
        data = {
            "id": self.id,
            "league_id": self.league_id,
            "type": self.type,
            "country": self.country,
            "country_code": self.country_code,
            "season": self.season,
            "season_start": self.season_start,
            "season_end": self.season_end,
            "logo": self.logo,
            "flag": self.flag,
            "standings": self.standings,
            "is_current": self.is_current
        }

        return data

class Team(models.Model):
    team_id = models.IntegerField()
    name = models.CharField(
        max_length=300
    )
    logo = models.CharField(
        max_length=600
    )

    def __str__(self):
        return self.name
    
    def to_json(self):
        data = {
            "id": self.id,
            "team_id": self.team_id,
            "name": self.name,
            "logo": self.logo
        }

        return data

class Fixture(models.Model):
    fixture_id = models.IntegerField()
    league_id = models.IntegerField()
    league_ref = models.ForeignKey(
        League,
        on_delete=models.SET_NULL,
        null=True
    )
    event_date = models.DateTimeField()
    event_timestamp = models.IntegerField()
    round = models.CharField(
        max_length=300,
        null=True
    )
    status = models.CharField(
        max_length=300,
        null=True
    )
    venue = models.CharField(
        max_length=300,
        null=True
    )
    home_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="home_team"
    )
    away_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="away_team"
    )
    goals_home_team = models.IntegerField()
    goals_away_team = models.IntegerField()

    def __str__(self):
        return "%s VS %s - %s" % (self.home_team.name, self.away_team.name, self.round)
    
    def to_json(self):
        data = {
            "id": self.id,
            "fixture_id": self.fixture_id,
            "league_id": self.league_id,
            "event_date": self.event_date,
            "event_timestamp": self.event_timestamp,
            "round": self.round,
            "status": self.status,
            "venue": self.venue,
            "home_team": self.home_team.to_json(),
            "away_team": self.away_team.to_json(),
            "goals_home_team": self.goals_home_team,
            "goals_away_team": self.goals_away_team
        }

        return data
