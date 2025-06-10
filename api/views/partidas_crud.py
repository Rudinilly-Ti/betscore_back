import requests
from datetime import datetime
from django.http import JsonResponse
from decouple import config  # Importa o método para carregar variáveis do .env

BASE_URL = 'https://api.sportmonks.com/v3/football'
API_KEY = config('MYSPORTMONKS_API')  # Carrega a chave do .env

def get_partidas(request):
    hoje = datetime.now()
    start_date = hoje.strftime('%Y-%m-%d')
    url = f'{BASE_URL}/leagues/date/2025-06-01?include=today.scores;today.participants;today.stage;today.group;today.round'
    params = {
        'api_token': API_KEY,
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch data'}, status=response.status_code)
