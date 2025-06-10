from datetime import datetime, timedelta
from pytz import timezone
from django.http import JsonResponse
import requests
from decouple import config

# Configurações da API
API_KEY = config('MYSPORTMONKS_API')
BASE_URL = 'https://api.sportmonks.com/v3/football'

def get_agenda(request):
    """
    Endpoint para buscar partidas agendadas no intervalo de datas e ajustar o timezone.
    """
    hoje = datetime.utcnow()
    daqui_a_um_mes = hoje + timedelta(days=30)  # Buscar jogos nos próximos 30 dias

    start_date = hoje.strftime('%Y-%m-%d')      # Data inicial
    end_date = daqui_a_um_mes.strftime('%Y-%m-%d')  # Data final



    # url = f"{BASE_URL}/fixtures/between/{start_date}/{end_date}"  # Endpoint correto
    # params = {
    #     'api_token': API_KEY,
    # }
    # response = requests.get(url, params=params)

    # if response.status_code == 200:
    #     data = response.json()
    #     # Converter os horários para o timezone de São Paulo
    #     saopaulo_tz = timezone('America/Sao_Paulo')
    #     for partida in data.get('data', []):
    #         if 'starting_at' in partida:
    #             utc_time = datetime.strptime(partida['starting_at'], '%Y-%m-%d %H:%M:%S')
    #             partida['starting_at'] = utc_time.replace(tzinfo=timezone('UTC')).astimezone(saopaulo_tz).strftime('%Y-%m-%d %H:%M:%S')
    #     return JsonResponse(data)
    # else:
    #     return JsonResponse({'error': 'Erro ao buscar dados da API'}, status=response.status_code)
    
    
