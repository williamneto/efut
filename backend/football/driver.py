# -*- coding: utf-8 -*-
import urllib
import json
import requests
from backend.local_settings import API_FOOTBALL_KEY

class APIFootball:
    host = "https://api-football-v1.p.rapidapi.com/v2"
    key = API_FOOTBALL_KEY

    def __init__(self):
        self.headers = {
            "X-RapidAPI-Key": self.key,
            "Accept": "application/json"
        } 
    
    # Get all seasons
    def get_seasons(self):
        url = "%s/seasons" % self.host

        response = requests.get(url, headers=self.headers)

        return response.json()
    
    # Get all countries
    def get_countries(self):
        url = "%s/countries" % self.host
        response = requests.get(url, headers=self.headers).json()

        return response
    
    # Get all leagues from one country
    def get_country_leagues(self, country, season=None):
        if season:
            url = "%s/leagues/country/%s/%s" % (
                self.host,
                country,
                season
            )
        else:
            url = "%s/leagues/country/%s/" % (
                self.host,
                country
            )

        response = requests.get(url, headers=self.headers).json()

        return response
    
    # Get all leagues from one {season}
    def get_season_leagues(self, season):
        url = "%s/leagues/season/%s" % (
            self.host,
            season
        )

        response = requests.get(url, headers=self.headers)

        return response

    # Get all fixtures from one league
    def get_league_fixtures(self, league_id, date=None):
        if date:
            url = "%s/fixtures/league/%s/%s/" % (
                self.host,
                league_id,
                date
            )
        else:
            url = "%s/fixtures/league/%s/" % (
                self.host,
                league_id
            )
        
        response = requests.get(url, headers=self.headers).json()

        return response
