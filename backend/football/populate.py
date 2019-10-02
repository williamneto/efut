# -*- coding: utf-8 -*-
from football.models import Team

def set_teams_popularity():
    first = ["Flamengo", "Corinthians", "Sao Paulo", "Palmeiras", "Vasco"]
    second = ["Cruzeiro", "Gremio", "Internacional", "Santos", "Atetico Mineiro"]
    third = ["Botafogo", "Bahia", "Fluminense", "Sport", "Santa Cruz"]

    for team in Team.objects.all():
        if any(name in team.name for name in third):
            team.popularity = 3
        elif any(name in team.name for name in second):
            team.popularity = 2
        elif any(name in team.name for name in first):
            team.popularity = 1
        else:
            team.popularity = 4
        team.save()
        print(">>> Salvo popularidade %s para o time %s" % (str(team.popularity), team.name))