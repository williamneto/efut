# -*- coding: utf-8 -*-
from football.driver import APIFootball
from football.models import League, Fixture, Team
 
api = APIFootball()

def download_leagues(season):
    leagues = api.get_season_leagues(season).json()["api"]["leagues"]
    league_objs = []
    league_names = []

    print("**** A carregar %s ligas" % str(len(leagues)))
    for l in leagues:
        query = League.objects.all().filter(
            name=l["name"],
            season=season
        )
        if len(query) == 0:
            l_obj = League(
                name=l["name"],
                league_id=l["league_id"],
                type=l["type"],
                country=l["country"],
                country_code=l["country_code"],
                season=l["season"],
                season_start=l["season_start"],
                season_end=l["season_end"],
                logo=l["logo"],
                flag=l["flag"],
                standings=l["standings"],
                is_current=l["is_current"]
            )
            l_obj.save()

            league_objs.append(l_obj.to_json())
            print(">>> Salvo liga %s - %s" % (l["name"], l["season"]))

def update_teams_data():
    teams_objs = Team.objects.all()
    print("***** Baixando dados de %s times" % str(len(teams_objs)))
    for team_obj in teams_objs:
        data = api.get_team_data(team_obj.team_id)

        team_obj.country = data["country"]
        team_obj.founded = data["founded"]
        team_obj.venue_name = data["venue_name"]
        team_obj.venue_city = data["venue_city"]
        team_obj.save()
        print(">>>> Atualizados dados de: %s" % team_obj.name)

def download_country_fixtures(country, season):
    leagues_query = League.objects.all().filter(
        country=country,
        season=season
    )

    print("***** Baixando jogos do %s de %s" % (country, season))
    if len(leagues_query) > 0:
        print(">>>> %s ligas encontradas para o país %s em %s" % (str(len(leagues_query)), country, season) )
        for l in leagues_query:
            league_fixtures = api.get_league_fixtures(l.league_id)["api"]["fixtures"]
            
            for f in league_fixtures:
                # Start a fixture object
                f_query = Fixture.objects.all().filter(
                    fixture_id=f["fixture_id"],
                    event_timestamp=f["event_timestamp"]
                )
                if len(f_query) == 0:
                    f_obj = Fixture(
                        fixture_id=f["fixture_id"],
                        league_id=f["league_id"],
                        league_ref=l,
                        event_date=f["event_date"],
                        event_timestamp=f["event_timestamp"],
                        round=f["round"],
                        status=f["status"],
                        venue=f["venue"],
                        goals_home_team=f["goalsHomeTeam"],
                        goals_away_team=f["goalsAwayTeam"]
                    )

                    # Lets check if there is a team with this name
                    home_team_query = Team.objects.all().filter(
                        name=f["homeTeam"]["team_name"]
                    )
                    if len(home_team_query) == 0:
                        home_team = Team(
                            team_id=f["homeTeam"]["team_id"],
                            name=f["homeTeam"]["team_name"],
                            logo=f["homeTeam"]["logo"]
                        )
                        home_team.save()
                    else:
                        home_team = home_team_query[0]
                    
                    away_team_query = Team.objects.all().filter(
                        name=f["awayTeam"]["team_name"]
                    )
                    if len(away_team_query) == 0:
                        away_team = Team(
                            team_id=f["awayTeam"]["team_id"],
                            name=f["awayTeam"]["team_name"],
                            logo=f["awayTeam"]["logo"]
                        )
                        away_team.save()
                    else:
                        away_team = away_team_query[0]
                    
                    # Save home_team and away_team
                    f_obj.home_team = home_team
                    f_obj.away_team = away_team
                    f_obj.save()

                    print(">>>> Salvo partida:  %s" % f_obj.__str__())

    else:
        print("Impossível baixar")