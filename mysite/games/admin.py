from django.contrib import admin

from .models import Game, GameContent, Lobby

admin.site.register(Game)


class LobbyAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'name')


admin.site.register(Lobby, LobbyAdmin)


admin.site.register(GameContent)
