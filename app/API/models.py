from django.db import models
from django.contrib import admin
import time
# Create your models here.
class users(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    user_info = models.CharField(max_length = 5000)

class usersAdmin(admin.ModelAdmin):
    list_display = ('username','user_info')

admin.site.register(users,usersAdmin)

class games(models.Model):
    user_id = models.CharField(max_length = 50)
    game_name = models.CharField(max_length = 50)
    game_info = models.CharField(max_length = 5000)
    game_date = models.DateTimeField(auto_now_add=True)


class gamesAdmin(admin.ModelAdmin):
    list_display = ('game_name','game_info','game_date')

admin.site.register(games,gamesAdmin)

class rounds(models.Model):
    game_id = models.CharField(max_length = 50)
    round_name = models.CharField(max_length = 50)
    round_info = models.CharField(max_length = 5000)
    round_date = models.DateTimeField(auto_now_add=True)


class roundsAdmin(admin.ModelAdmin):
    list_display = ('round_name','round_info','round_date')

admin.site.register(rounds,roundsAdmin)


