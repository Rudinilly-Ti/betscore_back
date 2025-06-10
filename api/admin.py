from django.contrib import admin
from .models import Partida  # Atualize o nome para Partida

@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display = ('time_casa', 'time_visitante', 'gols_casa', 'gols_visitante', 'data_partida')
    search_fields = ('time_casa', 'time_visitante')  # Adiciona funcionalidade de busca
    list_filter = ('data_partida',)  # Filtro por data no Django Admin
