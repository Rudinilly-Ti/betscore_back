from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import partidas_ao_vivo  # Função para buscar partidas ao vivo
from api.views import get_agenda
from api.views import get_agenda_time  # Função para buscar agenda de partidas
from api.views import get_classificacao  # Função para buscar times
from api.views import get_partidas  # Função para buscar partidas
# Configurar o roteador para a API
router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),  # Painel administrativo
    path('api/', include(router.urls)),  # Inclui as rotas padrão da API
    path('api/partidas/', get_partidas, name='get_partidas'),  # Rota para obter partidas do dia
    path('api/partidas-ao-vivo/', partidas_ao_vivo, name='partidas_ao_vivo'),  # Rota para partidas ao vivo
    path('api/partidas-agendadas/', get_agenda, name='agenda'),
    path('api/classificacao/', get_classificacao, name='classificacao'),  # Rota para obter classificação
    path('api/agenda/time/<int:team_id>', get_agenda_time, name='agenda_time'),  # Rota para agendar partidas de um time    
]
