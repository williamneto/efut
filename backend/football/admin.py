from django.contrib import admin

from football.models import League, Fixture, Team

class LeagueAdmin(admin.ModelAdmin):
    list_display = ("name", "country_code", "season")
    list_filter = ("season", "country_code")
    search_fields = ("name", "country", "country_code", "league_id")
admin.site.register(League, LeagueAdmin)

class FixtureAdmin(admin.ModelAdmin):
    list_display = ("__str__", "league_ref")
    list_filter = ("league_ref", "venue")
    search_fields = ("season", )
admin.site.register(Fixture, FixtureAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "venue_city", "venue_name", "founded", "popularity")
    search_fields = ("name", )
    list_filter = ("popularity", )
admin.site.register(Team, TeamAdmin)

