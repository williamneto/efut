from django.contrib import admin

from football.models import League, Fixture, Team

class LeagueAdmin(admin.ModelAdmin):
    list_display = ("name", "country_code", "season")
    list_filter = ("season", "country_code")
    search_fields = ("name", "country", "country_code", "league_id")
admin.site.register(League, LeagueAdmin)

admin.site.register(Fixture)
admin.site.register(Team)
