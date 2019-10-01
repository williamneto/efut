from django.contrib import admin

from football.models import League, Fixture, Team

admin.site.register(League)
admin.site.register(Fixture)
admin.site.register(Team)
