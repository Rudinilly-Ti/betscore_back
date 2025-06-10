import requests
from django.http import JsonResponse
from decouple import config  # Importa o método para carregar variáveis do .env

BASE_URL = 'https://api.sportmonks.com/v3/football'
API_KEY = config('MYSPORTMONKS_API')  # Carrega a chave do .env

def get_classificacao(request):
    # url = f'{BASE_URL}/standings/seasons/23614?include=participant;rule.type;details.type;form;stage;league;group'
    # params = {
    #     'api_token': API_KEY,
    # }
    # response = requests.get(url, params=params)

    # if response.status_code == 200:
    #     data = response.json()
    #     return JsonResponse(data, safe=False)
    # else:
    #     return JsonResponse({'error': 'Failed to fetch data'}, status=response.status_code)
    null = None
    true = True
    false = False

    data = [{
    "id": 229326,
    "participant_id": 8,
    "sport_id": 1,
    "league_id": 8,
    "season_id": 23614,
    "stage_id": 77471288,
    "group_id": null,
    "round_id": 339273,
    "standing_rule_id": 117804,
    "position": 1,
    "result": "equal",
    "points": 84,
    "participant": {
      "id": 8,
      "sport_id": 1,
      "country_id": 462,
      "venue_id": 230,
      "gender": "male",
      "name": "Liverpool",
      "short_code": "LIV",
      "image_path": "https://cdn.sportmonks.com/images/soccer/teams/8/8.png",
      "founded": 1892,
      "type": "domestic",
      "placeholder": false,
      "last_played_at": "2025-05-25 15:00:00"
    },
    "rule": {
      "id": 117804,
      "model_type": "stage",
      "model_id": 77471288,
      "type_id": 180,
      "position": 1,
      "type": {
        "id": 180,
        "name": "UEFA Champions League",
        "code": "uefa-champions-league",
        "developer_name": "UEFA_CHAMPIONS_LEAGUE",
        "model_type": "standing_rule",
        "stat_group": null
      }
    },
    "details": [
      {
        "id": 3131200654,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 143,
        "value": 5,
        "type": {
          "id": 143,
          "name": "Away Draw",
          "code": "away-draw",
          "developer_name": "AWAY_DRAWS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200658,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 146,
        "value": 25,
        "type": {
          "id": 146,
          "name": "Away Goals Conceded",
          "code": "away-conceded",
          "developer_name": "AWAY_CONCEDED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200652,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 141,
        "value": 19,
        "type": {
          "id": 141,
          "name": "Away Matched Played",
          "code": "away-matches-played",
          "developer_name": "AWAY_MATCHES",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200659,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 179,
        "value": 45,
        "type": {
          "id": 179,
          "name": "Goal Difference",
          "code": "goal-difference",
          "developer_name": "OVERALL_GOAL_DIFFERENCE",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200653,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 142,
        "value": 11,
        "type": {
          "id": 142,
          "name": "Away Won",
          "code": "away-won",
          "developer_name": "AWAY_WINS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200657,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 145,
        "value": 44,
        "type": {
          "id": 145,
          "name": "Away Goals Scored",
          "code": "away-scored",
          "developer_name": "AWAY_SCORED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200645,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 136,
        "value": 14,
        "type": {
          "id": 136,
          "name": "Home Won",
          "code": "home-won",
          "developer_name": "HOME_WINS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200655,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 144,
        "value": 3,
        "type": {
          "id": 144,
          "name": "Away Lost",
          "code": "away-lost",
          "developer_name": "AWAY_LOST",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3421579117,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 7939,
        "value": 78,
        "type": {
          "id": 7939,
          "name": "Expected Points (xPTS)",
          "code": "expected-points",
          "developer_name": "EXPECTED_POINTS",
          "model_type": "statistic",
          "stat_group": "offensive"
        }
      },
      {
        "id": 3131200647,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 138,
        "value": 1,
        "type": {
          "id": 138,
          "name": "Home Lost",
          "code": "home-lost",
          "developer_name": "HOME_LOST",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200648,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 185,
        "value": 46,
        "type": {
          "id": 185,
          "name": "Home Points",
          "code": "home-points",
          "developer_name": "HOME_POINTS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200649,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 139,
        "value": 42,
        "type": {
          "id": 139,
          "name": "Home Goals Scored",
          "code": "home-scored",
          "developer_name": "HOME_SCORED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200650,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 140,
        "value": 16,
        "type": {
          "id": 140,
          "name": "Home Goals Conceded",
          "code": "home-conceded",
          "developer_name": "HOME_CONCEDED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200651,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 187,
        "value": 84,
        "type": {
          "id": 187,
          "name": "Overall Points",
          "code": "overall-points",
          "developer_name": "TOTAL_POINTS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200656,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 186,
        "value": 38,
        "type": {
          "id": 186,
          "name": "Away Points",
          "code": "away-points",
          "developer_name": "AWAY_POINTS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200643,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 132,
        "value": 4,
        "type": {
          "id": 132,
          "name": "Overall Lost",
          "code": "overall-lost",
          "developer_name": "OVERALL_LOST",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200638,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 133,
        "value": 86,
        "type": {
          "id": 133,
          "name": "Overal Goals Scored",
          "code": "overall-goals-for",
          "developer_name": "OVERALL_SCORED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200639,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 134,
        "value": 41,
        "type": {
          "id": 134,
          "name": "Overall Goals Conceded",
          "code": "overall-goals-against",
          "developer_name": "OVERALL_CONCEDED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200640,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 129,
        "value": 38,
        "type": {
          "id": 129,
          "name": "Overall Matches Played",
          "code": "overall-matches-played",
          "developer_name": "OVERALL_MATCHES",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200641,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 130,
        "value": 25,
        "type": {
          "id": 130,
          "name": "Overall Won",
          "code": "overall-won",
          "developer_name": "OVERALL_WINS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200642,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 131,
        "value": 9,
        "type": {
          "id": 131,
          "name": "Overall Draw",
          "code": "overall-draw",
          "developer_name": "OVERALL_DRAWS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200644,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 135,
        "value": 19,
        "type": {
          "id": 135,
          "name": "Home Matched Played",
          "code": "home-matches-played",
          "developer_name": "HOME_MATCHES",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200646,
        "standing_type": "standing",
        "standing_id": 229326,
        "type_id": 137,
        "value": 4,
        "type": {
          "id": 137,
          "name": "Home Draw",
          "code": "home-draw",
          "developer_name": "HOME_DRAWS",
          "model_type": "standings",
          "stat_group": "home"
        }
      }
    ],
    "form": [
      {
        "id": 2202480712,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134454,
        "form": "W",
        "sort_order": 1
      },
      {
        "id": 2220180189,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134468,
        "form": "W",
        "sort_order": 2
      },
      {
        "id": 2233644918,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134479,
        "form": "W",
        "sort_order": 3
      },
      {
        "id": 2271343873,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134488,
        "form": "W",
        "sort_order": 5
      },
      {
        "id": 2288076319,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134502,
        "form": "W",
        "sort_order": 6
      },
      {
        "id": 2301449225,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134508,
        "form": "W",
        "sort_order": 7
      },
      {
        "id": 2335434424,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134516,
        "form": "W",
        "sort_order": 8
      },
      {
        "id": 2351317593,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134523,
        "form": "D",
        "sort_order": 9
      },
      {
        "id": 2381746207,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134537,
        "form": "W",
        "sort_order": 11
      },
      {
        "id": 3036245777,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134546,
        "form": "D",
        "sort_order": 24
      },
      {
        "id": 2574451405,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134558,
        "form": "D",
        "sort_order": 20
      },
      {
        "id": 2832963864,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134563,
        "form": "W",
        "sort_order": 23
      },
      {
        "id": 3139697011,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134578,
        "form": "W",
        "sort_order": 25
      },
      {
        "id": 3292981440,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134590,
        "form": "W",
        "sort_order": 27
      },
      {
        "id": 2414509020,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134602,
        "form": "W",
        "sort_order": 12
      },
      {
        "id": 2433501451,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134607,
        "form": "W",
        "sort_order": 13
      },
      {
        "id": 2616719007,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134614,
        "form": "W",
        "sort_order": 21
      },
      {
        "id": 2256382262,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134628,
        "form": "L",
        "sort_order": 4
      },
      {
        "id": 2463648767,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134637,
        "form": "D",
        "sort_order": 15
      },
      {
        "id": 2721175744,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134648,
        "form": "W",
        "sort_order": 22
      },
      {
        "id": 2361990622,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134872,
        "form": "W",
        "sort_order": 10
      },
      {
        "id": 2438795800,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134887,
        "form": "D",
        "sort_order": 14
      },
      {
        "id": 2482415847,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134897,
        "form": "W",
        "sort_order": 16
      },
      {
        "id": 2487676833,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134903,
        "form": "W",
        "sort_order": 17
      },
      {
        "id": 2491568232,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134918,
        "form": "W",
        "sort_order": 18
      },
      {
        "id": 2499948844,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134924,
        "form": "D",
        "sort_order": 19
      },
      {
        "id": 3322865919,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134937,
        "form": "W",
        "sort_order": 28
      },
      {
        "id": 3573042983,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134943,
        "form": "W",
        "sort_order": 29
      },
      {
        "id": 3178394721,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134951,
        "form": "D",
        "sort_order": 26
      },
      {
        "id": 4226346213,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134968,
        "form": "W",
        "sort_order": 30
      },
      {
        "id": 4385178224,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134973,
        "form": "L",
        "sort_order": 31
      },
      {
        "id": 4613720094,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134983,
        "form": "W",
        "sort_order": 32
      },
      {
        "id": 4816053833,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19134995,
        "form": "W",
        "sort_order": 33
      },
      {
        "id": 5004788228,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19135003,
        "form": "W",
        "sort_order": 34
      },
      {
        "id": 5180040203,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19135013,
        "form": "L",
        "sort_order": 35
      },
      {
        "id": 5337950805,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19135022,
        "form": "D",
        "sort_order": 36
      },
      {
        "id": 5510424015,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19135032,
        "form": "L",
        "sort_order": 37
      },
      {
        "id": 5619543207,
        "standing_type": "standing",
        "standing_id": 229326,
        "fixture_id": 19135042,
        "form": "D",
        "sort_order": 38
      }
    ],
    "stage": {
      "id": 77471288,
      "sport_id": 1,
      "league_id": 8,
      "season_id": 23614,
      "type_id": 223,
      "name": "Regular Season",
      "sort_order": 1,
      "finished": true,
      "is_current": false,
      "starting_at": "2024-08-16",
      "ending_at": "2025-05-25",
      "games_in_current_week": false,
      "tie_breaker_rule_id": null
    },
    "league": {
      "id": 8,
      "sport_id": 1,
      "country_id": 462,
      "name": "Premier League",
      "active": true,
      "short_code": "UK PL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/leagues/8/8.png",
      "type": "league",
      "sub_type": "domestic",
      "last_played_at": "2025-05-25 15:00:00",
      "category": 1,
      "has_jerseys": false
    },
    "group": null
  },
  {
    "id": 229316,
    "participant_id": 19,
    "sport_id": 1,
    "league_id": 8,
    "season_id": 23614,
    "stage_id": 77471288,
    "group_id": null,
    "round_id": 339273,
    "standing_rule_id": 117805,
    "position": 2,
    "result": "equal",
    "points": 74,
    "participant": {
      "id": 19,
      "sport_id": 1,
      "country_id": 462,
      "venue_id": 204,
      "gender": "male",
      "name": "Arsenal",
      "short_code": "ARS",
      "image_path": "https://cdn.sportmonks.com/images/soccer/teams/19/19.png",
      "founded": 1886,
      "type": "domestic",
      "placeholder": false,
      "last_played_at": "2025-05-25 15:00:00"
    },
    "rule": {
      "id": 117805,
      "model_type": "stage",
      "model_id": 77471288,
      "type_id": 180,
      "position": 2,
      "type": {
        "id": 180,
        "name": "UEFA Champions League",
        "code": "uefa-champions-league",
        "developer_name": "UEFA_CHAMPIONS_LEAGUE",
        "model_type": "standing_rule",
        "stat_group": null
      }
    },
    "details": [
      {
        "id": 3423871998,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 7939,
        "value": 70,
        "type": {
          "id": 7939,
          "name": "Expected Points (xPTS)",
          "code": "expected-points",
          "developer_name": "EXPECTED_POINTS",
          "model_type": "statistic",
          "stat_group": "offensive"
        }
      },
      {
        "id": 3131200434,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 143,
        "value": 8,
        "type": {
          "id": 143,
          "name": "Away Draw",
          "code": "away-draw",
          "developer_name": "AWAY_DRAWS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200418,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 133,
        "value": 69,
        "type": {
          "id": 133,
          "name": "Overal Goals Scored",
          "code": "overall-goals-for",
          "developer_name": "OVERALL_SCORED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200436,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 186,
        "value": 35,
        "type": {
          "id": 186,
          "name": "Away Points",
          "code": "away-points",
          "developer_name": "AWAY_POINTS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200427,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 138,
        "value": 2,
        "type": {
          "id": 138,
          "name": "Home Lost",
          "code": "home-lost",
          "developer_name": "HOME_LOST",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200421,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 130,
        "value": 20,
        "type": {
          "id": 130,
          "name": "Overall Won",
          "code": "overall-won",
          "developer_name": "OVERALL_WINS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200435,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 144,
        "value": 2,
        "type": {
          "id": 144,
          "name": "Away Lost",
          "code": "away-lost",
          "developer_name": "AWAY_LOST",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200438,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 146,
        "value": 17,
        "type": {
          "id": 146,
          "name": "Away Goals Conceded",
          "code": "away-conceded",
          "developer_name": "AWAY_CONCEDED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200439,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 179,
        "value": 35,
        "type": {
          "id": 179,
          "name": "Goal Difference",
          "code": "goal-difference",
          "developer_name": "OVERALL_GOAL_DIFFERENCE",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200428,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 185,
        "value": 39,
        "type": {
          "id": 185,
          "name": "Home Points",
          "code": "home-points",
          "developer_name": "HOME_POINTS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200429,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 139,
        "value": 35,
        "type": {
          "id": 139,
          "name": "Home Goals Scored",
          "code": "home-scored",
          "developer_name": "HOME_SCORED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200433,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 142,
        "value": 9,
        "type": {
          "id": 142,
          "name": "Away Won",
          "code": "away-won",
          "developer_name": "AWAY_WINS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200419,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 134,
        "value": 34,
        "type": {
          "id": 134,
          "name": "Overall Goals Conceded",
          "code": "overall-goals-against",
          "developer_name": "OVERALL_CONCEDED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200420,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 129,
        "value": 38,
        "type": {
          "id": 129,
          "name": "Overall Matches Played",
          "code": "overall-matches-played",
          "developer_name": "OVERALL_MATCHES",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200422,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 131,
        "value": 14,
        "type": {
          "id": 131,
          "name": "Overall Draw",
          "code": "overall-draw",
          "developer_name": "OVERALL_DRAWS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200423,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 132,
        "value": 4,
        "type": {
          "id": 132,
          "name": "Overall Lost",
          "code": "overall-lost",
          "developer_name": "OVERALL_LOST",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200424,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 135,
        "value": 19,
        "type": {
          "id": 135,
          "name": "Home Matched Played",
          "code": "home-matches-played",
          "developer_name": "HOME_MATCHES",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200425,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 136,
        "value": 11,
        "type": {
          "id": 136,
          "name": "Home Won",
          "code": "home-won",
          "developer_name": "HOME_WINS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200426,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 137,
        "value": 6,
        "type": {
          "id": 137,
          "name": "Home Draw",
          "code": "home-draw",
          "developer_name": "HOME_DRAWS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200430,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 140,
        "value": 17,
        "type": {
          "id": 140,
          "name": "Home Goals Conceded",
          "code": "home-conceded",
          "developer_name": "HOME_CONCEDED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200431,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 187,
        "value": 74,
        "type": {
          "id": 187,
          "name": "Overall Points",
          "code": "overall-points",
          "developer_name": "TOTAL_POINTS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200432,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 141,
        "value": 19,
        "type": {
          "id": 141,
          "name": "Away Matched Played",
          "code": "away-matches-played",
          "developer_name": "AWAY_MATCHES",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200437,
        "standing_type": "standing",
        "standing_id": 229316,
        "type_id": 145,
        "value": 34,
        "type": {
          "id": 145,
          "name": "Away Goals Scored",
          "code": "away-scored",
          "developer_name": "AWAY_SCORED",
          "model_type": "standings",
          "stat_group": "away"
        }
      }
    ],
    "form": [
      {
        "id": 2203038828,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134455,
        "form": "W",
        "sort_order": 1
      },
      {
        "id": 2217728615,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134464,
        "form": "W",
        "sort_order": 2
      },
      {
        "id": 2230413892,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134473,
        "form": "D",
        "sort_order": 3
      },
      {
        "id": 2274816572,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134489,
        "form": "D",
        "sort_order": 5
      },
      {
        "id": 2287650726,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134494,
        "form": "W",
        "sort_order": 6
      },
      {
        "id": 2302755439,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134503,
        "form": "W",
        "sort_order": 7
      },
      {
        "id": 2331045349,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134513,
        "form": "L",
        "sort_order": 8
      },
      {
        "id": 2351317623,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134523,
        "form": "D",
        "sort_order": 9
      },
      {
        "id": 2385353401,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134535,
        "form": "D",
        "sort_order": 11
      },
      {
        "id": 2451304924,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134547,
        "form": "D",
        "sort_order": 15
      },
      {
        "id": 2580401962,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134553,
        "form": "W",
        "sort_order": 21
      },
      {
        "id": 2879150124,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134564,
        "form": "W",
        "sort_order": 24
      },
      {
        "id": 3065957554,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134577,
        "form": "W",
        "sort_order": 25
      },
      {
        "id": 3237638370,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134584,
        "form": "L",
        "sort_order": 26
      },
      {
        "id": 2410182982,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134594,
        "form": "W",
        "sort_order": 12
      },
      {
        "id": 2428599420,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134611,
        "form": "W",
        "sort_order": 13
      },
      {
        "id": 2624792092,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134613,
        "form": "D",
        "sort_order": 22
      },
      {
        "id": 2258903658,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134631,
        "form": "W",
        "sort_order": 4
      },
      {
        "id": 2463547702,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134634,
        "form": "D",
        "sort_order": 16
      },
      {
        "id": 2721176081,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134652,
        "form": "W",
        "sort_order": 23
      },
      {
        "id": 2361114317,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134874,
        "form": "L",
        "sort_order": 10
      },
      {
        "id": 2438991757,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134880,
        "form": "W",
        "sort_order": 14
      },
      {
        "id": 2479507719,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134891,
        "form": "W",
        "sort_order": 17
      },
      {
        "id": 2488725130,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134900,
        "form": "W",
        "sort_order": 18
      },
      {
        "id": 2494466499,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134910,
        "form": "W",
        "sort_order": 19
      },
      {
        "id": 2498200779,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134921,
        "form": "D",
        "sort_order": 20
      },
      {
        "id": 3322461401,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134931,
        "form": "D",
        "sort_order": 27
      },
      {
        "id": 3647990950,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134944,
        "form": "D",
        "sort_order": 28
      },
      {
        "id": 3829544079,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134950,
        "form": "W",
        "sort_order": 29
      },
      {
        "id": 4211881982,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134960,
        "form": "W",
        "sort_order": 30
      },
      {
        "id": 4274269382,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134972,
        "form": "D",
        "sort_order": 31
      },
      {
        "id": 4561673822,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134980,
        "form": "D",
        "sort_order": 32
      },
      {
        "id": 4807288211,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19134994,
        "form": "W",
        "sort_order": 33
      },
      {
        "id": 4872163514,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19135000,
        "form": "D",
        "sort_order": 34
      },
      {
        "id": 5131053568,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19135009,
        "form": "L",
        "sort_order": 35
      },
      {
        "id": 5337950912,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19135022,
        "form": "D",
        "sort_order": 36
      },
      {
        "id": 5496226753,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19135029,
        "form": "W",
        "sort_order": 37
      },
      {
        "id": 5619791728,
        "standing_type": "standing",
        "standing_id": 229316,
        "fixture_id": 19135046,
        "form": "W",
        "sort_order": 38
      }
    ],
    "stage": {
      "id": 77471288,
      "sport_id": 1,
      "league_id": 8,
      "season_id": 23614,
      "type_id": 223,
      "name": "Regular Season",
      "sort_order": 1,
      "finished": true,
      "is_current": false,
      "starting_at": "2024-08-16",
      "ending_at": "2025-05-25",
      "games_in_current_week": false,
      "tie_breaker_rule_id": null
    },
    "league": {
      "id": 8,
      "sport_id": 1,
      "country_id": 462,
      "name": "Premier League",
      "active": true,
      "short_code": "UK PL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/leagues/8/8.png",
      "type": "league",
      "sub_type": "domestic",
      "last_played_at": "2025-05-25 15:00:00",
      "category": 1,
      "has_jerseys": false
    },
    "group": null
  },
  {
    "id": 229327,
    "participant_id": 9,
    "sport_id": 1,
    "league_id": 8,
    "season_id": 23614,
    "stage_id": 77471288,
    "group_id": null,
    "round_id": 339273,
    "standing_rule_id": 117806,
    "position": 3,
    "result": "equal",
    "points": 71,
    "participant": {
      "id": 9,
      "sport_id": 1,
      "country_id": 462,
      "venue_id": 151,
      "gender": "male",
      "name": "Manchester City",
      "short_code": "MCI",
      "image_path": "https://cdn.sportmonks.com/images/soccer/teams/9/9.png",
      "founded": 1880,
      "type": "domestic",
      "placeholder": false,
      "last_played_at": "2025-05-25 15:00:00"
    },
    "rule": {
      "id": 117806,
      "model_type": "stage",
      "model_id": 77471288,
      "type_id": 180,
      "position": 3,
      "type": {
        "id": 180,
        "name": "UEFA Champions League",
        "code": "uefa-champions-league",
        "developer_name": "UEFA_CHAMPIONS_LEAGUE",
        "model_type": "standing_rule",
        "stat_group": null
      }
    },
    "details": [
      {
        "id": 3432092037,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 7939,
        "value": 65,
        "type": {
          "id": 7939,
          "name": "Expected Points (xPTS)",
          "code": "expected-points",
          "developer_name": "EXPECTED_POINTS",
          "model_type": "statistic",
          "stat_group": "offensive"
        }
      },
      {
        "id": 3131200681,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 179,
        "value": 28,
        "type": {
          "id": 179,
          "name": "Goal Difference",
          "code": "goal-difference",
          "developer_name": "OVERALL_GOAL_DIFFERENCE",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200677,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 144,
        "value": 6,
        "type": {
          "id": 144,
          "name": "Away Lost",
          "code": "away-lost",
          "developer_name": "AWAY_LOST",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200660,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 133,
        "value": 72,
        "type": {
          "id": 133,
          "name": "Overal Goals Scored",
          "code": "overall-goals-for",
          "developer_name": "OVERALL_SCORED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200661,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 134,
        "value": 44,
        "type": {
          "id": 134,
          "name": "Overall Goals Conceded",
          "code": "overall-goals-against",
          "developer_name": "OVERALL_CONCEDED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200673,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 187,
        "value": 71,
        "type": {
          "id": 187,
          "name": "Overall Points",
          "code": "overall-points",
          "developer_name": "TOTAL_POINTS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200678,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 186,
        "value": 29,
        "type": {
          "id": 186,
          "name": "Away Points",
          "code": "away-points",
          "developer_name": "AWAY_POINTS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200679,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 145,
        "value": 29,
        "type": {
          "id": 145,
          "name": "Away Goals Scored",
          "code": "away-scored",
          "developer_name": "AWAY_SCORED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200672,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 140,
        "value": 23,
        "type": {
          "id": 140,
          "name": "Home Goals Conceded",
          "code": "home-conceded",
          "developer_name": "HOME_CONCEDED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200663,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 130,
        "value": 21,
        "type": {
          "id": 130,
          "name": "Overall Won",
          "code": "overall-won",
          "developer_name": "OVERALL_WINS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200664,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 131,
        "value": 8,
        "type": {
          "id": 131,
          "name": "Overall Draw",
          "code": "overall-draw",
          "developer_name": "OVERALL_DRAWS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200680,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 146,
        "value": 21,
        "type": {
          "id": 146,
          "name": "Away Goals Conceded",
          "code": "away-conceded",
          "developer_name": "AWAY_CONCEDED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200662,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 129,
        "value": 38,
        "type": {
          "id": 129,
          "name": "Overall Matches Played",
          "code": "overall-matches-played",
          "developer_name": "OVERALL_MATCHES",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200665,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 132,
        "value": 9,
        "type": {
          "id": 132,
          "name": "Overall Lost",
          "code": "overall-lost",
          "developer_name": "OVERALL_LOST",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200666,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 135,
        "value": 19,
        "type": {
          "id": 135,
          "name": "Home Matched Played",
          "code": "home-matches-played",
          "developer_name": "HOME_MATCHES",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200667,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 136,
        "value": 13,
        "type": {
          "id": 136,
          "name": "Home Won",
          "code": "home-won",
          "developer_name": "HOME_WINS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200668,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 137,
        "value": 3,
        "type": {
          "id": 137,
          "name": "Home Draw",
          "code": "home-draw",
          "developer_name": "HOME_DRAWS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200669,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 138,
        "value": 3,
        "type": {
          "id": 138,
          "name": "Home Lost",
          "code": "home-lost",
          "developer_name": "HOME_LOST",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200670,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 185,
        "value": 42,
        "type": {
          "id": 185,
          "name": "Home Points",
          "code": "home-points",
          "developer_name": "HOME_POINTS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200671,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 139,
        "value": 43,
        "type": {
          "id": 139,
          "name": "Home Goals Scored",
          "code": "home-scored",
          "developer_name": "HOME_SCORED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200674,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 141,
        "value": 19,
        "type": {
          "id": 141,
          "name": "Away Matched Played",
          "code": "away-matches-played",
          "developer_name": "AWAY_MATCHES",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200675,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 142,
        "value": 8,
        "type": {
          "id": 142,
          "name": "Away Won",
          "code": "away-won",
          "developer_name": "AWAY_WINS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200676,
        "standing_type": "standing",
        "standing_id": 229327,
        "type_id": 143,
        "value": 5,
        "type": {
          "id": 143,
          "name": "Away Draw",
          "code": "away-draw",
          "developer_name": "AWAY_DRAWS",
          "model_type": "standings",
          "stat_group": "away"
        }
      }
    ],
    "form": [
      {
        "id": 2205683299,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134461,
        "form": "W",
        "sort_order": 1
      },
      {
        "id": 2217340394,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134469,
        "form": "W",
        "sort_order": 2
      },
      {
        "id": 2231484439,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134482,
        "form": "W",
        "sort_order": 3
      },
      {
        "id": 2274816557,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134489,
        "form": "D",
        "sort_order": 5
      },
      {
        "id": 2286553335,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134500,
        "form": "D",
        "sort_order": 6
      },
      {
        "id": 2302736692,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134511,
        "form": "W",
        "sort_order": 7
      },
      {
        "id": 2334858782,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134522,
        "form": "W",
        "sort_order": 8
      },
      {
        "id": 2346792187,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134531,
        "form": "W",
        "sort_order": 9
      },
      {
        "id": 2380842990,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134534,
        "form": "L",
        "sort_order": 11
      },
      {
        "id": 2446974747,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134545,
        "form": "D",
        "sort_order": 15
      },
      {
        "id": 2573555086,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134554,
        "form": "D",
        "sort_order": 21
      },
      {
        "id": 2879150172,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134564,
        "form": "L",
        "sort_order": 24
      },
      {
        "id": 3091788616,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134579,
        "form": "W",
        "sort_order": 25
      },
      {
        "id": 3292981773,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134590,
        "form": "L",
        "sort_order": 26
      },
      {
        "id": 2410717265,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134600,
        "form": "L",
        "sort_order": 12
      },
      {
        "id": 2433501636,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134607,
        "form": "L",
        "sort_order": 13
      },
      {
        "id": 2658172015,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134617,
        "form": "W",
        "sort_order": 22
      },
      {
        "id": 2256382186,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134629,
        "form": "W",
        "sort_order": 4
      },
      {
        "id": 2468780895,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134638,
        "form": "L",
        "sort_order": 16
      },
      {
        "id": 2728580751,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134649,
        "form": "W",
        "sort_order": 23
      },
      {
        "id": 2361990648,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134869,
        "form": "L",
        "sort_order": 10
      },
      {
        "id": 2438795836,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134886,
        "form": "W",
        "sort_order": 14
      },
      {
        "id": 2477240864,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134889,
        "form": "L",
        "sort_order": 17
      },
      {
        "id": 2486210733,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134904,
        "form": "D",
        "sort_order": 18
      },
      {
        "id": 2491342422,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134915,
        "form": "W",
        "sort_order": 19
      },
      {
        "id": 2497545628,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134925,
        "form": "W",
        "sort_order": 20
      },
      {
        "id": 3322505558,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134932,
        "form": "W",
        "sort_order": 27
      },
      {
        "id": 3536912490,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134945,
        "form": "L",
        "sort_order": 28
      },
      {
        "id": 3772407430,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134956,
        "form": "D",
        "sort_order": 29
      },
      {
        "id": 4226040225,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134965,
        "form": "W",
        "sort_order": 30
      },
      {
        "id": 4402571127,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134976,
        "form": "D",
        "sort_order": 31
      },
      {
        "id": 4493908890,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134984,
        "form": "W",
        "sort_order": 32
      },
      {
        "id": 4770515802,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19134992,
        "form": "W",
        "sort_order": 33
      },
      {
        "id": 4862260260,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19135004,
        "form": "W",
        "sort_order": 34
      },
      {
        "id": 5075392738,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19135017,
        "form": "W",
        "sort_order": 35
      },
      {
        "id": 5284603184,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19135026,
        "form": "D",
        "sort_order": 36
      },
      {
        "id": 5516110972,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19135037,
        "form": "W",
        "sort_order": 37
      },
      {
        "id": 5619882941,
        "standing_type": "standing",
        "standing_id": 229327,
        "fixture_id": 19135040,
        "form": "W",
        "sort_order": 38
      }
    ],
    "stage": {
      "id": 77471288,
      "sport_id": 1,
      "league_id": 8,
      "season_id": 23614,
      "type_id": 223,
      "name": "Regular Season",
      "sort_order": 1,
      "finished": true,
      "is_current": false,
      "starting_at": "2024-08-16",
      "ending_at": "2025-05-25",
      "games_in_current_week": false,
      "tie_breaker_rule_id": null
    },
    "league": {
      "id": 8,
      "sport_id": 1,
      "country_id": 462,
      "name": "Premier League",
      "active": true,
      "short_code": "UK PL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/leagues/8/8.png",
      "type": "league",
      "sub_type": "domestic",
      "last_played_at": "2025-05-25 15:00:00",
      "category": 1,
      "has_jerseys": false
    },
    "group": null
  },
  {
    "id": 229320,
    "participant_id": 18,
    "sport_id": 1,
    "league_id": 8,
    "season_id": 23614,
    "stage_id": 77471288,
    "group_id": null,
    "round_id": 339273,
    "standing_rule_id": 117807,
    "position": 4,
    "result": "up",
    "points": 69,
    "participant": {
      "id": 18,
      "sport_id": 1,
      "country_id": 462,
      "venue_id": 321614,
      "gender": "male",
      "name": "Chelsea",
      "short_code": "CHE",
      "image_path": "https://cdn.sportmonks.com/images/soccer/teams/18/18.png",
      "founded": 1905,
      "type": "domestic",
      "placeholder": false,
      "last_played_at": "2025-05-28 19:00:00"
    },
    "rule": {
      "id": 117807,
      "model_type": "stage",
      "model_id": 77471288,
      "type_id": 180,
      "position": 4,
      "type": {
        "id": 180,
        "name": "UEFA Champions League",
        "code": "uefa-champions-league",
        "developer_name": "UEFA_CHAMPIONS_LEAGUE",
        "model_type": "standing_rule",
        "stat_group": null
      }
    },
    "details": [
      {
        "id": 3432092036,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 7939,
        "value": 62,
        "type": {
          "id": 7939,
          "name": "Expected Points (xPTS)",
          "code": "expected-points",
          "developer_name": "EXPECTED_POINTS",
          "model_type": "statistic",
          "stat_group": "offensive"
        }
      },
      {
        "id": 3131200512,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 135,
        "value": 19,
        "type": {
          "id": 135,
          "name": "Home Matched Played",
          "code": "home-matches-played",
          "developer_name": "HOME_MATCHES",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200527,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 179,
        "value": 21,
        "type": {
          "id": 179,
          "name": "Goal Difference",
          "code": "goal-difference",
          "developer_name": "OVERALL_GOAL_DIFFERENCE",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200521,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 142,
        "value": 8,
        "type": {
          "id": 142,
          "name": "Away Won",
          "code": "away-won",
          "developer_name": "AWAY_WINS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200523,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 144,
        "value": 7,
        "type": {
          "id": 144,
          "name": "Away Lost",
          "code": "away-lost",
          "developer_name": "AWAY_LOST",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200511,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 132,
        "value": 9,
        "type": {
          "id": 132,
          "name": "Overall Lost",
          "code": "overall-lost",
          "developer_name": "OVERALL_LOST",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200524,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 186,
        "value": 28,
        "type": {
          "id": 186,
          "name": "Away Points",
          "code": "away-points",
          "developer_name": "AWAY_POINTS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200525,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 145,
        "value": 29,
        "type": {
          "id": 145,
          "name": "Away Goals Scored",
          "code": "away-scored",
          "developer_name": "AWAY_SCORED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200526,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 146,
        "value": 25,
        "type": {
          "id": 146,
          "name": "Away Goals Conceded",
          "code": "away-conceded",
          "developer_name": "AWAY_CONCEDED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200517,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 139,
        "value": 35,
        "type": {
          "id": 139,
          "name": "Home Goals Scored",
          "code": "home-scored",
          "developer_name": "HOME_SCORED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200518,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 140,
        "value": 18,
        "type": {
          "id": 140,
          "name": "Home Goals Conceded",
          "code": "home-conceded",
          "developer_name": "HOME_CONCEDED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200506,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 133,
        "value": 64,
        "type": {
          "id": 133,
          "name": "Overal Goals Scored",
          "code": "overall-goals-for",
          "developer_name": "OVERALL_SCORED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200507,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 134,
        "value": 43,
        "type": {
          "id": 134,
          "name": "Overall Goals Conceded",
          "code": "overall-goals-against",
          "developer_name": "OVERALL_CONCEDED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200508,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 129,
        "value": 38,
        "type": {
          "id": 129,
          "name": "Overall Matches Played",
          "code": "overall-matches-played",
          "developer_name": "OVERALL_MATCHES",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200509,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 130,
        "value": 20,
        "type": {
          "id": 130,
          "name": "Overall Won",
          "code": "overall-won",
          "developer_name": "OVERALL_WINS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200510,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 131,
        "value": 9,
        "type": {
          "id": 131,
          "name": "Overall Draw",
          "code": "overall-draw",
          "developer_name": "OVERALL_DRAWS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200513,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 136,
        "value": 12,
        "type": {
          "id": 136,
          "name": "Home Won",
          "code": "home-won",
          "developer_name": "HOME_WINS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200514,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 137,
        "value": 5,
        "type": {
          "id": 137,
          "name": "Home Draw",
          "code": "home-draw",
          "developer_name": "HOME_DRAWS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200515,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 138,
        "value": 2,
        "type": {
          "id": 138,
          "name": "Home Lost",
          "code": "home-lost",
          "developer_name": "HOME_LOST",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200516,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 185,
        "value": 41,
        "type": {
          "id": 185,
          "name": "Home Points",
          "code": "home-points",
          "developer_name": "HOME_POINTS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200519,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 187,
        "value": 69,
        "type": {
          "id": 187,
          "name": "Overall Points",
          "code": "overall-points",
          "developer_name": "TOTAL_POINTS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200520,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 141,
        "value": 19,
        "type": {
          "id": 141,
          "name": "Away Matched Played",
          "code": "away-matches-played",
          "developer_name": "AWAY_MATCHES",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200522,
        "standing_type": "standing",
        "standing_id": 229320,
        "type_id": 143,
        "value": 4,
        "type": {
          "id": 143,
          "name": "Away Draw",
          "code": "away-draw",
          "developer_name": "AWAY_DRAWS",
          "model_type": "standings",
          "stat_group": "away"
        }
      }
    ],
    "form": [
      {
        "id": 2205683316,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134461,
        "form": "L",
        "sort_order": 1
      },
      {
        "id": 2219847933,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134472,
        "form": "W",
        "sort_order": 2
      },
      {
        "id": 2233280597,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134475,
        "form": "D",
        "sort_order": 3
      },
      {
        "id": 2270488994,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134492,
        "form": "W",
        "sort_order": 5
      },
      {
        "id": 2287650810,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134496,
        "form": "W",
        "sort_order": 6
      },
      {
        "id": 2307139095,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134507,
        "form": "D",
        "sort_order": 7
      },
      {
        "id": 2335434464,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134516,
        "form": "L",
        "sort_order": 8
      },
      {
        "id": 2350897101,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134527,
        "form": "W",
        "sort_order": 9
      },
      {
        "id": 2385353390,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134535,
        "form": "D",
        "sort_order": 11
      },
      {
        "id": 2452140124,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134551,
        "form": "W",
        "sort_order": 15
      },
      {
        "id": 2573726453,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134560,
        "form": "D",
        "sort_order": 21
      },
      {
        "id": 2887738088,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134566,
        "form": "W",
        "sort_order": 24
      },
      {
        "id": 3051615195,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134574,
        "form": "L",
        "sort_order": 25
      },
      {
        "id": 3248668994,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134585,
        "form": "L",
        "sort_order": 26
      },
      {
        "id": 2409033184,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134599,
        "form": "W",
        "sort_order": 12
      },
      {
        "id": 2432455020,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134605,
        "form": "W",
        "sort_order": 13
      },
      {
        "id": 2663045162,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134615,
        "form": "W",
        "sort_order": 22
      },
      {
        "id": 2257163350,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134623,
        "form": "W",
        "sort_order": 4
      },
      {
        "id": 2468878541,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134636,
        "form": "W",
        "sort_order": 16
      },
      {
        "id": 2728580817,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134649,
        "form": "L",
        "sort_order": 23
      },
      {
        "id": 2367143603,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134873,
        "form": "D",
        "sort_order": 10
      },
      {
        "id": 2438801037,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134888,
        "form": "W",
        "sort_order": 14
      },
      {
        "id": 2481996531,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134892,
        "form": "D",
        "sort_order": 17
      },
      {
        "id": 2487106775,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134902,
        "form": "L",
        "sort_order": 18
      },
      {
        "id": 2492364124,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134914,
        "form": "L",
        "sort_order": 19
      },
      {
        "id": 2497493519,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134922,
        "form": "D",
        "sort_order": 20
      },
      {
        "id": 3314872566,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134936,
        "form": "W",
        "sort_order": 27
      },
      {
        "id": 3637839976,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134941,
        "form": "W",
        "sort_order": 28
      },
      {
        "id": 3829544205,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134950,
        "form": "L",
        "sort_order": 29
      },
      {
        "id": 4231489935,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134964,
        "form": "W",
        "sort_order": 30
      },
      {
        "id": 4385178317,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134970,
        "form": "D",
        "sort_order": 31
      },
      {
        "id": 4614200134,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134982,
        "form": "D",
        "sort_order": 32
      },
      {
        "id": 4807288310,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19134993,
        "form": "W",
        "sort_order": 33
      },
      {
        "id": 4916522285,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19135002,
        "form": "W",
        "sort_order": 34
      },
      {
        "id": 5180040775,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19135013,
        "form": "W",
        "sort_order": 35
      },
      {
        "id": 5320225148,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19135024,
        "form": "L",
        "sort_order": 36
      },
      {
        "id": 5394881714,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19135033,
        "form": "W",
        "sort_order": 37
      },
      {
        "id": 5620025094,
        "standing_type": "standing",
        "standing_id": 229320,
        "fixture_id": 19135045,
        "form": "W",
        "sort_order": 38
      }
    ],
    "stage": {
      "id": 77471288,
      "sport_id": 1,
      "league_id": 8,
      "season_id": 23614,
      "type_id": 223,
      "name": "Regular Season",
      "sort_order": 1,
      "finished": true,
      "is_current": false,
      "starting_at": "2024-08-16",
      "ending_at": "2025-05-25",
      "games_in_current_week": false,
      "tie_breaker_rule_id": null
    },
    "league": {
      "id": 8,
      "sport_id": 1,
      "country_id": 462,
      "name": "Premier League",
      "active": true,
      "short_code": "UK PL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/leagues/8/8.png",
      "type": "league",
      "sub_type": "domestic",
      "last_played_at": "2025-05-25 15:00:00",
      "category": 1,
      "has_jerseys": false
    },
    "group": null
  },
  {
    "id": 229329,
    "participant_id": 20,
    "sport_id": 1,
    "league_id": 8,
    "season_id": 23614,
    "stage_id": 77471288,
    "group_id": null,
    "round_id": 339273,
    "standing_rule_id": 127207,
    "position": 5,
    "result": "down",
    "points": 66,
    "participant": {
      "id": 20,
      "sport_id": 1,
      "country_id": 462,
      "venue_id": 449,
      "gender": "male",
      "name": "Newcastle United",
      "short_code": "NEW",
      "image_path": "https://cdn.sportmonks.com/images/soccer/teams/20/20.png",
      "founded": 1892,
      "type": "domestic",
      "placeholder": false,
      "last_played_at": "2025-05-25 15:00:00"
    },
    "rule": {
      "id": 127207,
      "model_type": "stage",
      "model_id": 77471288,
      "type_id": 180,
      "position": 5,
      "type": {
        "id": 180,
        "name": "UEFA Champions League",
        "code": "uefa-champions-league",
        "developer_name": "UEFA_CHAMPIONS_LEAGUE",
        "model_type": "standing_rule",
        "stat_group": null
      }
    },
    "details": [
      {
        "id": 3424071067,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 7939,
        "value": 60,
        "type": {
          "id": 7939,
          "name": "Expected Points (xPTS)",
          "code": "expected-points",
          "developer_name": "EXPECTED_POINTS",
          "model_type": "statistic",
          "stat_group": "offensive"
        }
      },
      {
        "id": 3131200717,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 187,
        "value": 66,
        "type": {
          "id": 187,
          "name": "Overall Points",
          "code": "overall-points",
          "developer_name": "TOTAL_POINTS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200707,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 130,
        "value": 20,
        "type": {
          "id": 130,
          "name": "Overall Won",
          "code": "overall-won",
          "developer_name": "OVERALL_WINS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200711,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 136,
        "value": 12,
        "type": {
          "id": 136,
          "name": "Home Won",
          "code": "home-won",
          "developer_name": "HOME_WINS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200712,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 137,
        "value": 2,
        "type": {
          "id": 137,
          "name": "Home Draw",
          "code": "home-draw",
          "developer_name": "HOME_DRAWS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200704,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 133,
        "value": 68,
        "type": {
          "id": 133,
          "name": "Overal Goals Scored",
          "code": "overall-goals-for",
          "developer_name": "OVERALL_SCORED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200706,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 129,
        "value": 38,
        "type": {
          "id": 129,
          "name": "Overall Matches Played",
          "code": "overall-matches-played",
          "developer_name": "OVERALL_MATCHES",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200723,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 145,
        "value": 28,
        "type": {
          "id": 145,
          "name": "Away Goals Scored",
          "code": "away-scored",
          "developer_name": "AWAY_SCORED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200724,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 146,
        "value": 27,
        "type": {
          "id": 146,
          "name": "Away Goals Conceded",
          "code": "away-conceded",
          "developer_name": "AWAY_CONCEDED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200725,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 179,
        "value": 21,
        "type": {
          "id": 179,
          "name": "Goal Difference",
          "code": "goal-difference",
          "developer_name": "OVERALL_GOAL_DIFFERENCE",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200705,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 134,
        "value": 47,
        "type": {
          "id": 134,
          "name": "Overall Goals Conceded",
          "code": "overall-goals-against",
          "developer_name": "OVERALL_CONCEDED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200708,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 131,
        "value": 6,
        "type": {
          "id": 131,
          "name": "Overall Draw",
          "code": "overall-draw",
          "developer_name": "OVERALL_DRAWS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200709,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 132,
        "value": 12,
        "type": {
          "id": 132,
          "name": "Overall Lost",
          "code": "overall-lost",
          "developer_name": "OVERALL_LOST",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200710,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 135,
        "value": 19,
        "type": {
          "id": 135,
          "name": "Home Matched Played",
          "code": "home-matches-played",
          "developer_name": "HOME_MATCHES",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200713,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 138,
        "value": 5,
        "type": {
          "id": 138,
          "name": "Home Lost",
          "code": "home-lost",
          "developer_name": "HOME_LOST",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200714,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 185,
        "value": 38,
        "type": {
          "id": 185,
          "name": "Home Points",
          "code": "home-points",
          "developer_name": "HOME_POINTS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200715,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 139,
        "value": 40,
        "type": {
          "id": 139,
          "name": "Home Goals Scored",
          "code": "home-scored",
          "developer_name": "HOME_SCORED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200716,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 140,
        "value": 20,
        "type": {
          "id": 140,
          "name": "Home Goals Conceded",
          "code": "home-conceded",
          "developer_name": "HOME_CONCEDED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200718,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 141,
        "value": 19,
        "type": {
          "id": 141,
          "name": "Away Matched Played",
          "code": "away-matches-played",
          "developer_name": "AWAY_MATCHES",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200719,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 142,
        "value": 8,
        "type": {
          "id": 142,
          "name": "Away Won",
          "code": "away-won",
          "developer_name": "AWAY_WINS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200720,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 143,
        "value": 4,
        "type": {
          "id": 143,
          "name": "Away Draw",
          "code": "away-draw",
          "developer_name": "AWAY_DRAWS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200721,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 144,
        "value": 7,
        "type": {
          "id": 144,
          "name": "Away Lost",
          "code": "away-lost",
          "developer_name": "AWAY_LOST",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200722,
        "standing_type": "standing",
        "standing_id": 229329,
        "type_id": 186,
        "value": 28,
        "type": {
          "id": 186,
          "name": "Away Points",
          "code": "away-points",
          "developer_name": "AWAY_POINTS",
          "model_type": "standings",
          "stat_group": "away"
        }
      }
    ],
    "form": [
      {
        "id": 2203085837,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134457,
        "form": "W",
        "sort_order": 1
      },
      {
        "id": 2219824256,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134463,
        "form": "D",
        "sort_order": 2
      },
      {
        "id": 2233280511,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134480,
        "form": "W",
        "sort_order": 3
      },
      {
        "id": 2271344312,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134486,
        "form": "L",
        "sort_order": 5
      },
      {
        "id": 2286553362,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134500,
        "form": "D",
        "sort_order": 6
      },
      {
        "id": 2303215024,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134509,
        "form": "D",
        "sort_order": 7
      },
      {
        "id": 2330386195,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134518,
        "form": "L",
        "sort_order": 8
      },
      {
        "id": 2350897344,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134527,
        "form": "L",
        "sort_order": 9
      },
      {
        "id": 2384851357,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134539,
        "form": "W",
        "sort_order": 11
      },
      {
        "id": 2446976926,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134544,
        "form": "L",
        "sort_order": 15
      },
      {
        "id": 2580176305,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134561,
        "form": "W",
        "sort_order": 21
      },
      {
        "id": 2832964183,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134570,
        "form": "L",
        "sort_order": 24
      },
      {
        "id": 3091788841,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134579,
        "form": "L",
        "sort_order": 25
      },
      {
        "id": 3284723216,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134591,
        "form": "W",
        "sort_order": 26
      },
      {
        "id": 2417214108,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134601,
        "form": "L",
        "sort_order": 12
      },
      {
        "id": 2427852913,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134606,
        "form": "D",
        "sort_order": 13
      },
      {
        "id": 2598658214,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134620,
        "form": "L",
        "sort_order": 22
      },
      {
        "id": 2259242884,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134632,
        "form": "W",
        "sort_order": 4
      },
      {
        "id": 2463548519,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134639,
        "form": "W",
        "sort_order": 16
      },
      {
        "id": 2721176615,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134650,
        "form": "W",
        "sort_order": 23
      },
      {
        "id": 2361114432,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134874,
        "form": "W",
        "sort_order": 10
      },
      {
        "id": 2438796152,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134887,
        "form": "D",
        "sort_order": 14
      },
      {
        "id": 2478844667,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134894,
        "form": "W",
        "sort_order": 17
      },
      {
        "id": 2487106873,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134905,
        "form": "W",
        "sort_order": 18
      },
      {
        "id": 2492370447,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134916,
        "form": "W",
        "sort_order": 19
      },
      {
        "id": 2496950102,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134927,
        "form": "W",
        "sort_order": 20
      },
      {
        "id": 3322866176,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134937,
        "form": "L",
        "sort_order": 27
      },
      {
        "id": 3660897923,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134947,
        "form": "W",
        "sort_order": 28
      },
      {
        "id": 4666973620,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134957,
        "form": "W",
        "sort_order": 32
      },
      {
        "id": 4226138864,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134966,
        "form": "W",
        "sort_order": 29
      },
      {
        "id": 4417547763,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134975,
        "form": "W",
        "sort_order": 30
      },
      {
        "id": 4630190369,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134985,
        "form": "W",
        "sort_order": 31
      },
      {
        "id": 4780824112,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19134989,
        "form": "L",
        "sort_order": 33
      },
      {
        "id": 4945038784,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19135005,
        "form": "W",
        "sort_order": 34
      },
      {
        "id": 5170319443,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19135012,
        "form": "D",
        "sort_order": 35
      },
      {
        "id": 5320224239,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19135024,
        "form": "W",
        "sort_order": 36
      },
      {
        "id": 5496226790,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19135029,
        "form": "L",
        "sort_order": 37
      },
      {
        "id": 5619883015,
        "standing_type": "standing",
        "standing_id": 229329,
        "fixture_id": 19135044,
        "form": "L",
        "sort_order": 38
      }
    ],
    "stage": {
      "id": 77471288,
      "sport_id": 1,
      "league_id": 8,
      "season_id": 23614,
      "type_id": 223,
      "name": "Regular Season",
      "sort_order": 1,
      "finished": true,
      "is_current": false,
      "starting_at": "2024-08-16",
      "ending_at": "2025-05-25",
      "games_in_current_week": false,
      "tie_breaker_rule_id": null
    },
    "league": {
      "id": 8,
      "sport_id": 1,
      "country_id": 462,
      "name": "Premier League",
      "active": true,
      "short_code": "UK PL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/leagues/8/8.png",
      "type": "league",
      "sub_type": "domestic",
      "last_played_at": "2025-05-25 15:00:00",
      "category": 1,
      "has_jerseys": false
    },
    "group": null
  },
  {
    "id": 229317,
    "participant_id": 15,
    "sport_id": 1,
    "league_id": 8,
    "season_id": 23614,
    "stage_id": 77471288,
    "group_id": null,
    "round_id": 339273,
    "standing_rule_id": 127208,
    "position": 6,
    "result": "equal",
    "points": 66,
    "participant": {
      "id": 15,
      "sport_id": 1,
      "country_id": 462,
      "venue_id": 5,
      "gender": "male",
      "name": "Aston Villa",
      "short_code": "AVL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/teams/15/15.png",
      "founded": 1874,
      "type": "domestic",
      "placeholder": false,
      "last_played_at": "2025-05-25 15:00:00"
    },
    "rule": {
      "id": 127208,
      "model_type": "stage",
      "model_id": 77471288,
      "type_id": 181,
      "position": 6,
      "type": {
        "id": 181,
        "name": "UEFA Europa League",
        "code": "uefa-europa-league",
        "developer_name": "UEFA_EUROPA_LEAGUE",
        "model_type": "standing_rule",
        "stat_group": null
      }
    },
    "details": [
      {
        "id": 3131200456,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 143,
        "value": 2,
        "type": {
          "id": 143,
          "name": "Away Draw",
          "code": "away-draw",
          "developer_name": "AWAY_DRAWS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200452,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 140,
        "value": 20,
        "type": {
          "id": 140,
          "name": "Home Goals Conceded",
          "code": "home-conceded",
          "developer_name": "HOME_CONCEDED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200455,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 142,
        "value": 8,
        "type": {
          "id": 142,
          "name": "Away Won",
          "code": "away-won",
          "developer_name": "AWAY_WINS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200454,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 141,
        "value": 19,
        "type": {
          "id": 141,
          "name": "Away Matched Played",
          "code": "away-matches-played",
          "developer_name": "AWAY_MATCHES",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3425869150,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 7939,
        "value": 56,
        "type": {
          "id": 7939,
          "name": "Expected Points (xPTS)",
          "code": "expected-points",
          "developer_name": "EXPECTED_POINTS",
          "model_type": "statistic",
          "stat_group": "offensive"
        }
      },
      {
        "id": 3131200440,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 133,
        "value": 58,
        "type": {
          "id": 133,
          "name": "Overal Goals Scored",
          "code": "overall-goals-for",
          "developer_name": "OVERALL_SCORED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200441,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 134,
        "value": 51,
        "type": {
          "id": 134,
          "name": "Overall Goals Conceded",
          "code": "overall-goals-against",
          "developer_name": "OVERALL_CONCEDED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200444,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 131,
        "value": 9,
        "type": {
          "id": 131,
          "name": "Overall Draw",
          "code": "overall-draw",
          "developer_name": "OVERALL_DRAWS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200450,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 185,
        "value": 40,
        "type": {
          "id": 185,
          "name": "Home Points",
          "code": "home-points",
          "developer_name": "HOME_POINTS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200442,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 129,
        "value": 38,
        "type": {
          "id": 129,
          "name": "Overall Matches Played",
          "code": "overall-matches-played",
          "developer_name": "OVERALL_MATCHES",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200443,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 130,
        "value": 19,
        "type": {
          "id": 130,
          "name": "Overall Won",
          "code": "overall-won",
          "developer_name": "OVERALL_WINS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200445,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 132,
        "value": 10,
        "type": {
          "id": 132,
          "name": "Overall Lost",
          "code": "overall-lost",
          "developer_name": "OVERALL_LOST",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200446,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 135,
        "value": 19,
        "type": {
          "id": 135,
          "name": "Home Matched Played",
          "code": "home-matches-played",
          "developer_name": "HOME_MATCHES",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200447,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 136,
        "value": 11,
        "type": {
          "id": 136,
          "name": "Home Won",
          "code": "home-won",
          "developer_name": "HOME_WINS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200448,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 137,
        "value": 7,
        "type": {
          "id": 137,
          "name": "Home Draw",
          "code": "home-draw",
          "developer_name": "HOME_DRAWS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200449,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 138,
        "value": 1,
        "type": {
          "id": 138,
          "name": "Home Lost",
          "code": "home-lost",
          "developer_name": "HOME_LOST",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200451,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 139,
        "value": 34,
        "type": {
          "id": 139,
          "name": "Home Goals Scored",
          "code": "home-scored",
          "developer_name": "HOME_SCORED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200453,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 187,
        "value": 66,
        "type": {
          "id": 187,
          "name": "Overall Points",
          "code": "overall-points",
          "developer_name": "TOTAL_POINTS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200457,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 144,
        "value": 9,
        "type": {
          "id": 144,
          "name": "Away Lost",
          "code": "away-lost",
          "developer_name": "AWAY_LOST",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200458,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 186,
        "value": 26,
        "type": {
          "id": 186,
          "name": "Away Points",
          "code": "away-points",
          "developer_name": "AWAY_POINTS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200459,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 145,
        "value": 24,
        "type": {
          "id": 145,
          "name": "Away Goals Scored",
          "code": "away-scored",
          "developer_name": "AWAY_SCORED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200460,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 146,
        "value": 31,
        "type": {
          "id": 146,
          "name": "Away Goals Conceded",
          "code": "away-conceded",
          "developer_name": "AWAY_CONCEDED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200461,
        "standing_type": "standing",
        "standing_id": 229317,
        "type_id": 179,
        "value": 7,
        "type": {
          "id": 179,
          "name": "Goal Difference",
          "code": "goal-difference",
          "developer_name": "OVERALL_GOAL_DIFFERENCE",
          "model_type": "standings",
          "stat_group": "overall"
        }
      }
    ],
    "form": [
      {
        "id": 2203404351,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134459,
        "form": "W",
        "sort_order": 1
      },
      {
        "id": 2217728791,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134464,
        "form": "L",
        "sort_order": 2
      },
      {
        "id": 2231104819,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134478,
        "form": "W",
        "sort_order": 3
      },
      {
        "id": 2271548952,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134483,
        "form": "W",
        "sort_order": 5
      },
      {
        "id": 2291179039,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134498,
        "form": "D",
        "sort_order": 6
      },
      {
        "id": 2307139300,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134504,
        "form": "D",
        "sort_order": 7
      },
      {
        "id": 2330386006,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134514,
        "form": "W",
        "sort_order": 8
      },
      {
        "id": 2346792361,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134524,
        "form": "D",
        "sort_order": 9
      },
      {
        "id": 2381746281,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134537,
        "form": "L",
        "sort_order": 11
      },
      {
        "id": 2446974979,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134543,
        "form": "W",
        "sort_order": 15
      },
      {
        "id": 2580127781,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134555,
        "form": "W",
        "sort_order": 21
      },
      {
        "id": 2840806545,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134572,
        "form": "L",
        "sort_order": 24
      },
      {
        "id": 3091789147,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134573,
        "form": "D",
        "sort_order": 25
      },
      {
        "id": 3248669040,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134585,
        "form": "W",
        "sort_order": 27
      },
      {
        "id": 2410183986,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134595,
        "form": "D",
        "sort_order": 12
      },
      {
        "id": 2432455298,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134605,
        "form": "L",
        "sort_order": 13
      },
      {
        "id": 2624792200,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134613,
        "form": "D",
        "sort_order": 22
      },
      {
        "id": 2256761155,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134624,
        "form": "W",
        "sort_order": 4
      },
      {
        "id": 2464533392,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134640,
        "form": "L",
        "sort_order": 16
      },
      {
        "id": 2765658463,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134644,
        "form": "D",
        "sort_order": 23
      },
      {
        "id": 2366627631,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134877,
        "form": "L",
        "sort_order": 10
      },
      {
        "id": 2439001488,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134881,
        "form": "W",
        "sort_order": 14
      },
      {
        "id": 2477240847,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134889,
        "form": "W",
        "sort_order": 17
      },
      {
        "id": 2487107004,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134905,
        "form": "L",
        "sort_order": 18
      },
      {
        "id": 2492370523,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134909,
        "form": "D",
        "sort_order": 19
      },
      {
        "id": 2497545911,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134920,
        "form": "W",
        "sort_order": 20
      },
      {
        "id": 3313368995,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134935,
        "form": "L",
        "sort_order": 28
      },
      {
        "id": 3587206654,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134939,
        "form": "W",
        "sort_order": 29
      },
      {
        "id": 3178395201,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134951,
        "form": "D",
        "sort_order": 26
      },
      {
        "id": 4226138923,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134961,
        "form": "W",
        "sort_order": 30
      },
      {
        "id": 4331970638,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134969,
        "form": "W",
        "sort_order": 31
      },
      {
        "id": 4541753194,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134987,
        "form": "W",
        "sort_order": 32
      },
      {
        "id": 4780824317,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19134989,
        "form": "W",
        "sort_order": 33
      },
      {
        "id": 4862260393,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19135004,
        "form": "L",
        "sort_order": 34
      },
      {
        "id": 5099039944,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19135010,
        "form": "W",
        "sort_order": 35
      },
      {
        "id": 5295887071,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19135019,
        "form": "W",
        "sort_order": 36
      },
      {
        "id": 5394588835,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19135030,
        "form": "W",
        "sort_order": 37
      },
      {
        "id": 5620025460,
        "standing_type": "standing",
        "standing_id": 229317,
        "fixture_id": 19135043,
        "form": "L",
        "sort_order": 38
      }
    ],
    "stage": {
      "id": 77471288,
      "sport_id": 1,
      "league_id": 8,
      "season_id": 23614,
      "type_id": 223,
      "name": "Regular Season",
      "sort_order": 1,
      "finished": true,
      "is_current": false,
      "starting_at": "2024-08-16",
      "ending_at": "2025-05-25",
      "games_in_current_week": false,
      "tie_breaker_rule_id": null
    },
    "league": {
      "id": 8,
      "sport_id": 1,
      "country_id": 462,
      "name": "Premier League",
      "active": true,
      "short_code": "UK PL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/leagues/8/8.png",
      "type": "league",
      "sub_type": "domestic",
      "last_played_at": "2025-05-25 15:00:00",
      "category": 1,
      "has_jerseys": false
    },
    "group": null
  },
  {
    "id": 229330,
    "participant_id": 63,
    "sport_id": 1,
    "league_id": 8,
    "season_id": 23614,
    "stage_id": 77471288,
    "group_id": null,
    "round_id": 339273,
    "standing_rule_id": 127209,
    "position": 7,
    "result": "equal",
    "points": 65,
    "participant": {
      "id": 63,
      "sport_id": 1,
      "country_id": 462,
      "venue_id": 542,
      "gender": "male",
      "name": "Nottingham Forest",
      "short_code": "NFO",
      "image_path": "https://cdn.sportmonks.com/images/soccer/teams/31/63.png",
      "founded": 1865,
      "type": "domestic",
      "placeholder": false,
      "last_played_at": "2025-05-25 15:00:00"
    },
    "rule": {
      "id": 127209,
      "model_type": "stage",
      "model_id": 77471288,
      "type_id": 289,
      "position": 7,
      "type": {
        "id": 289,
        "name": "UEFA Conference League Qualifiers",
        "code": "uefa-conference-league-qualifiers",
        "developer_name": "UEFA_CONFERENCE_LEAGUE_QUALIFIERS",
        "model_type": "standing_rule",
        "stat_group": null
      }
    },
    "details": [
      {
        "id": 3131200743,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 144,
        "value": 6,
        "type": {
          "id": 144,
          "name": "Away Lost",
          "code": "away-lost",
          "developer_name": "AWAY_LOST",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3424403433,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 7939,
        "value": 49,
        "type": {
          "id": 7939,
          "name": "Expected Points (xPTS)",
          "code": "expected-points",
          "developer_name": "EXPECTED_POINTS",
          "model_type": "statistic",
          "stat_group": "offensive"
        }
      },
      {
        "id": 3131200735,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 138,
        "value": 5,
        "type": {
          "id": 138,
          "name": "Home Lost",
          "code": "home-lost",
          "developer_name": "HOME_LOST",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200726,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 133,
        "value": 58,
        "type": {
          "id": 133,
          "name": "Overal Goals Scored",
          "code": "overall-goals-for",
          "developer_name": "OVERALL_SCORED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200736,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 185,
        "value": 32,
        "type": {
          "id": 185,
          "name": "Home Points",
          "code": "home-points",
          "developer_name": "HOME_POINTS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200727,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 134,
        "value": 46,
        "type": {
          "id": 134,
          "name": "Overall Goals Conceded",
          "code": "overall-goals-against",
          "developer_name": "OVERALL_CONCEDED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200728,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 129,
        "value": 38,
        "type": {
          "id": 129,
          "name": "Overall Matches Played",
          "code": "overall-matches-played",
          "developer_name": "OVERALL_MATCHES",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200745,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 145,
        "value": 32,
        "type": {
          "id": 145,
          "name": "Away Goals Scored",
          "code": "away-scored",
          "developer_name": "AWAY_SCORED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200729,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 130,
        "value": 19,
        "type": {
          "id": 130,
          "name": "Overall Won",
          "code": "overall-won",
          "developer_name": "OVERALL_WINS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200734,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 137,
        "value": 5,
        "type": {
          "id": 137,
          "name": "Home Draw",
          "code": "home-draw",
          "developer_name": "HOME_DRAWS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200737,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 139,
        "value": 26,
        "type": {
          "id": 139,
          "name": "Home Goals Scored",
          "code": "home-scored",
          "developer_name": "HOME_SCORED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200738,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 140,
        "value": 16,
        "type": {
          "id": 140,
          "name": "Home Goals Conceded",
          "code": "home-conceded",
          "developer_name": "HOME_CONCEDED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200747,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 179,
        "value": 12,
        "type": {
          "id": 179,
          "name": "Goal Difference",
          "code": "goal-difference",
          "developer_name": "OVERALL_GOAL_DIFFERENCE",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200730,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 131,
        "value": 8,
        "type": {
          "id": 131,
          "name": "Overall Draw",
          "code": "overall-draw",
          "developer_name": "OVERALL_DRAWS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200731,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 132,
        "value": 11,
        "type": {
          "id": 132,
          "name": "Overall Lost",
          "code": "overall-lost",
          "developer_name": "OVERALL_LOST",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200732,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 135,
        "value": 19,
        "type": {
          "id": 135,
          "name": "Home Matched Played",
          "code": "home-matches-played",
          "developer_name": "HOME_MATCHES",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200733,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 136,
        "value": 9,
        "type": {
          "id": 136,
          "name": "Home Won",
          "code": "home-won",
          "developer_name": "HOME_WINS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200739,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 187,
        "value": 65,
        "type": {
          "id": 187,
          "name": "Overall Points",
          "code": "overall-points",
          "developer_name": "TOTAL_POINTS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200740,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 141,
        "value": 19,
        "type": {
          "id": 141,
          "name": "Away Matched Played",
          "code": "away-matches-played",
          "developer_name": "AWAY_MATCHES",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200741,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 142,
        "value": 10,
        "type": {
          "id": 142,
          "name": "Away Won",
          "code": "away-won",
          "developer_name": "AWAY_WINS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200742,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 143,
        "value": 3,
        "type": {
          "id": 143,
          "name": "Away Draw",
          "code": "away-draw",
          "developer_name": "AWAY_DRAWS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200744,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 186,
        "value": 33,
        "type": {
          "id": 186,
          "name": "Away Points",
          "code": "away-points",
          "developer_name": "AWAY_POINTS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200746,
        "standing_type": "standing",
        "standing_id": 229330,
        "type_id": 146,
        "value": 30,
        "type": {
          "id": 146,
          "name": "Away Goals Conceded",
          "code": "away-conceded",
          "developer_name": "AWAY_CONCEDED",
          "model_type": "standings",
          "stat_group": "away"
        }
      }
    ],
    "form": [
      {
        "id": 2203118747,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134458,
        "form": "D",
        "sort_order": 1
      },
      {
        "id": 2217304941,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134470,
        "form": "W",
        "sort_order": 2
      },
      {
        "id": 2231135854,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134481,
        "form": "D",
        "sort_order": 3
      },
      {
        "id": 2274451791,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134484,
        "form": "D",
        "sort_order": 5
      },
      {
        "id": 2287564059,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134501,
        "form": "L",
        "sort_order": 6
      },
      {
        "id": 2307139884,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134507,
        "form": "D",
        "sort_order": 7
      },
      {
        "id": 2337232493,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134519,
        "form": "W",
        "sort_order": 8
      },
      {
        "id": 2343063586,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134530,
        "form": "W",
        "sort_order": 9
      },
      {
        "id": 2384850814,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134539,
        "form": "L",
        "sort_order": 11
      },
      {
        "id": 2447805530,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134550,
        "form": "W",
        "sort_order": 15
      },
      {
        "id": 2574451426,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134558,
        "form": "D",
        "sort_order": 21
      },
      {
        "id": 2813081439,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134571,
        "form": "W",
        "sort_order": 24
      },
      {
        "id": 3091788528,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134576,
        "form": "L",
        "sort_order": 25
      },
      {
        "id": 3284722823,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134591,
        "form": "L",
        "sort_order": 26
      },
      {
        "id": 2410183693,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134594,
        "form": "L",
        "sort_order": 12
      },
      {
        "id": 2427851595,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134609,
        "form": "W",
        "sort_order": 13
      },
      {
        "id": 2652410870,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134621,
        "form": "W",
        "sort_order": 22
      },
      {
        "id": 2256382449,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134628,
        "form": "W",
        "sort_order": 4
      },
      {
        "id": 2464533361,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134640,
        "form": "W",
        "sort_order": 16
      },
      {
        "id": 2721176250,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134643,
        "form": "L",
        "sort_order": 23
      },
      {
        "id": 2361993256,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134875,
        "form": "W",
        "sort_order": 10
      },
      {
        "id": 2438796029,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134886,
        "form": "L",
        "sort_order": 14
      },
      {
        "id": 2478842995,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134890,
        "form": "W",
        "sort_order": 17
      },
      {
        "id": 2487106815,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134906,
        "form": "W",
        "sort_order": 18
      },
      {
        "id": 2491461282,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134912,
        "form": "W",
        "sort_order": 19
      },
      {
        "id": 2501389760,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134928,
        "form": "W",
        "sort_order": 20
      },
      {
        "id": 3322461428,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134931,
        "form": "D",
        "sort_order": 27
      },
      {
        "id": 3536912307,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134945,
        "form": "W",
        "sort_order": 28
      },
      {
        "id": 3772407017,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134954,
        "form": "W",
        "sort_order": 29
      },
      {
        "id": 4212594358,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134962,
        "form": "W",
        "sort_order": 30
      },
      {
        "id": 4331970518,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134969,
        "form": "L",
        "sort_order": 31
      },
      {
        "id": 4541751696,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134986,
        "form": "L",
        "sort_order": 32
      },
      {
        "id": 4854152184,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19134997,
        "form": "W",
        "sort_order": 33
      },
      {
        "id": 5057730398,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19135006,
        "form": "L",
        "sort_order": 34
      },
      {
        "id": 5201336612,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19135014,
        "form": "D",
        "sort_order": 35
      },
      {
        "id": 5330072652,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19135025,
        "form": "D",
        "sort_order": 36
      },
      {
        "id": 5488634612,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19135038,
        "form": "W",
        "sort_order": 37
      },
      {
        "id": 5620025657,
        "standing_type": "standing",
        "standing_id": 229330,
        "fixture_id": 19135045,
        "form": "L",
        "sort_order": 38
      }
    ],
    "stage": {
      "id": 77471288,
      "sport_id": 1,
      "league_id": 8,
      "season_id": 23614,
      "type_id": 223,
      "name": "Regular Season",
      "sort_order": 1,
      "finished": true,
      "is_current": false,
      "starting_at": "2024-08-16",
      "ending_at": "2025-05-25",
      "games_in_current_week": false,
      "tie_breaker_rule_id": null
    },
    "league": {
      "id": 8,
      "sport_id": 1,
      "country_id": 462,
      "name": "Premier League",
      "active": true,
      "short_code": "UK PL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/leagues/8/8.png",
      "type": "league",
      "sub_type": "domestic",
      "last_played_at": "2025-05-25 15:00:00",
      "category": 1,
      "has_jerseys": false
    },
    "group": null
  },
  {
    "id": 229319,
    "participant_id": 78,
    "sport_id": 1,
    "league_id": 8,
    "season_id": 23614,
    "stage_id": 77471288,
    "group_id": null,
    "round_id": 339273,
    "standing_rule_id": null,
    "position": 8,
    "result": "equal",
    "points": 61,
    "participant": {
      "id": 78,
      "sport_id": 1,
      "country_id": 462,
      "venue_id": 480,
      "gender": "male",
      "name": "Brighton & Hove Albion",
      "short_code": "BHA",
      "image_path": "https://cdn.sportmonks.com/images/soccer/teams/14/78.png",
      "founded": 1901,
      "type": "domestic",
      "placeholder": false,
      "last_played_at": "2025-05-25 15:00:00"
    },
    "rule": null,
    "details": [
      {
        "id": 3424287306,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 7939,
        "value": 56,
        "type": {
          "id": 7939,
          "name": "Expected Points (xPTS)",
          "code": "expected-points",
          "developer_name": "EXPECTED_POINTS",
          "model_type": "statistic",
          "stat_group": "offensive"
        }
      },
      {
        "id": 3131200505,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 179,
        "value": 7,
        "type": {
          "id": 179,
          "name": "Goal Difference",
          "code": "goal-difference",
          "developer_name": "OVERALL_GOAL_DIFFERENCE",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200489,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 132,
        "value": 9,
        "type": {
          "id": 132,
          "name": "Overall Lost",
          "code": "overall-lost",
          "developer_name": "OVERALL_LOST",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200495,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 139,
        "value": 30,
        "type": {
          "id": 139,
          "name": "Home Goals Scored",
          "code": "home-scored",
          "developer_name": "HOME_SCORED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200493,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 138,
        "value": 3,
        "type": {
          "id": 138,
          "name": "Home Lost",
          "code": "home-lost",
          "developer_name": "HOME_LOST",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200494,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 185,
        "value": 32,
        "type": {
          "id": 185,
          "name": "Home Points",
          "code": "home-points",
          "developer_name": "HOME_POINTS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200488,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 131,
        "value": 13,
        "type": {
          "id": 131,
          "name": "Overall Draw",
          "code": "overall-draw",
          "developer_name": "OVERALL_DRAWS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200491,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 136,
        "value": 8,
        "type": {
          "id": 136,
          "name": "Home Won",
          "code": "home-won",
          "developer_name": "HOME_WINS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200496,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 140,
        "value": 26,
        "type": {
          "id": 140,
          "name": "Home Goals Conceded",
          "code": "home-conceded",
          "developer_name": "HOME_CONCEDED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200497,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 187,
        "value": 61,
        "type": {
          "id": 187,
          "name": "Overall Points",
          "code": "overall-points",
          "developer_name": "TOTAL_POINTS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200498,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 141,
        "value": 19,
        "type": {
          "id": 141,
          "name": "Away Matched Played",
          "code": "away-matches-played",
          "developer_name": "AWAY_MATCHES",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200484,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 133,
        "value": 66,
        "type": {
          "id": 133,
          "name": "Overal Goals Scored",
          "code": "overall-goals-for",
          "developer_name": "OVERALL_SCORED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200485,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 134,
        "value": 59,
        "type": {
          "id": 134,
          "name": "Overall Goals Conceded",
          "code": "overall-goals-against",
          "developer_name": "OVERALL_CONCEDED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200487,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 130,
        "value": 16,
        "type": {
          "id": 130,
          "name": "Overall Won",
          "code": "overall-won",
          "developer_name": "OVERALL_WINS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200490,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 135,
        "value": 19,
        "type": {
          "id": 135,
          "name": "Home Matched Played",
          "code": "home-matches-played",
          "developer_name": "HOME_MATCHES",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200492,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 137,
        "value": 8,
        "type": {
          "id": 137,
          "name": "Home Draw",
          "code": "home-draw",
          "developer_name": "HOME_DRAWS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200486,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 129,
        "value": 38,
        "type": {
          "id": 129,
          "name": "Overall Matches Played",
          "code": "overall-matches-played",
          "developer_name": "OVERALL_MATCHES",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200500,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 143,
        "value": 5,
        "type": {
          "id": 143,
          "name": "Away Draw",
          "code": "away-draw",
          "developer_name": "AWAY_DRAWS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200501,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 144,
        "value": 6,
        "type": {
          "id": 144,
          "name": "Away Lost",
          "code": "away-lost",
          "developer_name": "AWAY_LOST",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200502,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 186,
        "value": 29,
        "type": {
          "id": 186,
          "name": "Away Points",
          "code": "away-points",
          "developer_name": "AWAY_POINTS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200503,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 145,
        "value": 36,
        "type": {
          "id": 145,
          "name": "Away Goals Scored",
          "code": "away-scored",
          "developer_name": "AWAY_SCORED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200504,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 146,
        "value": 33,
        "type": {
          "id": 146,
          "name": "Away Goals Conceded",
          "code": "away-conceded",
          "developer_name": "AWAY_CONCEDED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200499,
        "standing_type": "standing",
        "standing_id": 229319,
        "type_id": 142,
        "value": 8,
        "type": {
          "id": 142,
          "name": "Away Won",
          "code": "away-won",
          "developer_name": "AWAY_WINS",
          "model_type": "standings",
          "stat_group": "away"
        }
      }
    ],
    "form": [
      {
        "id": 2203090249,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134456,
        "form": "W",
        "sort_order": 1
      },
      {
        "id": 2216729130,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134465,
        "form": "W",
        "sort_order": 2
      },
      {
        "id": 2230413886,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134473,
        "form": "D",
        "sort_order": 3
      },
      {
        "id": 2274451765,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134484,
        "form": "D",
        "sort_order": 5
      },
      {
        "id": 2287651329,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134496,
        "form": "L",
        "sort_order": 6
      },
      {
        "id": 2307637564,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134506,
        "form": "W",
        "sort_order": 7
      },
      {
        "id": 2330386050,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134518,
        "form": "W",
        "sort_order": 8
      },
      {
        "id": 2346792543,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134526,
        "form": "D",
        "sort_order": 9
      },
      {
        "id": 2380843011,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134534,
        "form": "W",
        "sort_order": 11
      },
      {
        "id": 2451305049,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134549,
        "form": "D",
        "sort_order": 15
      },
      {
        "id": 2582279154,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134556,
        "form": "W",
        "sort_order": 21
      },
      {
        "id": 2813081930,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134571,
        "form": "L",
        "sort_order": 24
      },
      {
        "id": 3051615292,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134574,
        "form": "W",
        "sort_order": 25
      },
      {
        "id": 3237536985,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134592,
        "form": "W",
        "sort_order": 26
      },
      {
        "id": 2410183316,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134593,
        "form": "W",
        "sort_order": 12
      },
      {
        "id": 2423498320,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134604,
        "form": "D",
        "sort_order": 13
      },
      {
        "id": 2652412248,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134619,
        "form": "W",
        "sort_order": 22
      },
      {
        "id": 2256382344,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134625,
        "form": "D",
        "sort_order": 4
      },
      {
        "id": 2467848773,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134635,
        "form": "L",
        "sort_order": 16
      },
      {
        "id": 2721885407,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134645,
        "form": "L",
        "sort_order": 23
      },
      {
        "id": 2361990773,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134872,
        "form": "L",
        "sort_order": 10
      },
      {
        "id": 2440264246,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134883,
        "form": "L",
        "sort_order": 14
      },
      {
        "id": 2478997857,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134898,
        "form": "D",
        "sort_order": 17
      },
      {
        "id": 2488696377,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134901,
        "form": "D",
        "sort_order": 18
      },
      {
        "id": 2492370542,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134909,
        "form": "D",
        "sort_order": 19
      },
      {
        "id": 2498200937,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134921,
        "form": "D",
        "sort_order": 20
      },
      {
        "id": 3313368730,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134930,
        "form": "W",
        "sort_order": 27
      },
      {
        "id": 3573043346,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134940,
        "form": "W",
        "sort_order": 28
      },
      {
        "id": 3772407829,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134956,
        "form": "D",
        "sort_order": 29
      },
      {
        "id": 4226138953,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134961,
        "form": "L",
        "sort_order": 30
      },
      {
        "id": 4317266457,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134971,
        "form": "L",
        "sort_order": 31
      },
      {
        "id": 4541757474,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134981,
        "form": "D",
        "sort_order": 32
      },
      {
        "id": 4773565986,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19134990,
        "form": "L",
        "sort_order": 33
      },
      {
        "id": 4944298119,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19135001,
        "form": "W",
        "sort_order": 34
      },
      {
        "id": 5170319985,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19135012,
        "form": "D",
        "sort_order": 35
      },
      {
        "id": 5284811236,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19135028,
        "form": "W",
        "sort_order": 36
      },
      {
        "id": 5510424273,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19135032,
        "form": "W",
        "sort_order": 37
      },
      {
        "id": 5619636171,
        "standing_type": "standing",
        "standing_id": 229319,
        "fixture_id": 19135047,
        "form": "W",
        "sort_order": 38
      }
    ],
    "stage": {
      "id": 77471288,
      "sport_id": 1,
      "league_id": 8,
      "season_id": 23614,
      "type_id": 223,
      "name": "Regular Season",
      "sort_order": 1,
      "finished": true,
      "is_current": false,
      "starting_at": "2024-08-16",
      "ending_at": "2025-05-25",
      "games_in_current_week": false,
      "tie_breaker_rule_id": null
    },
    "league": {
      "id": 8,
      "sport_id": 1,
      "country_id": 462,
      "name": "Premier League",
      "active": true,
      "short_code": "UK PL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/leagues/8/8.png",
      "type": "league",
      "sub_type": "domestic",
      "last_played_at": "2025-05-25 15:00:00",
      "category": 1,
      "has_jerseys": false
    },
    "group": null
  },
  {
    "id": 229315,
    "participant_id": 52,
    "sport_id": 1,
    "league_id": 8,
    "season_id": 23614,
    "stage_id": 77471288,
    "group_id": null,
    "round_id": 339273,
    "standing_rule_id": null,
    "position": 9,
    "result": "up",
    "points": 56,
    "participant": {
      "id": 52,
      "sport_id": 1,
      "country_id": 462,
      "venue_id": 146,
      "gender": "male",
      "name": "AFC Bournemouth",
      "short_code": "BOU",
      "image_path": "https://cdn.sportmonks.com/images/soccer/teams/20/52.png",
      "founded": 1899,
      "type": "domestic",
      "placeholder": false,
      "last_played_at": "2025-05-25 15:00:00"
    },
    "rule": null,
    "details": [
      {
        "id": 3424403366,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 7939,
        "value": 62,
        "type": {
          "id": 7939,
          "name": "Expected Points (xPTS)",
          "code": "expected-points",
          "developer_name": "EXPECTED_POINTS",
          "model_type": "statistic",
          "stat_group": "offensive"
        }
      },
      {
        "id": 3131200417,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 179,
        "value": 12,
        "type": {
          "id": 179,
          "name": "Goal Difference",
          "code": "goal-difference",
          "developer_name": "OVERALL_GOAL_DIFFERENCE",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200414,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 186,
        "value": 28,
        "type": {
          "id": 186,
          "name": "Away Points",
          "code": "away-points",
          "developer_name": "AWAY_POINTS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200398,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 129,
        "value": 38,
        "type": {
          "id": 129,
          "name": "Overall Matches Played",
          "code": "overall-matches-played",
          "developer_name": "OVERALL_MATCHES",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200401,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 132,
        "value": 12,
        "type": {
          "id": 132,
          "name": "Overall Lost",
          "code": "overall-lost",
          "developer_name": "OVERALL_LOST",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200402,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 135,
        "value": 19,
        "type": {
          "id": 135,
          "name": "Home Matched Played",
          "code": "home-matches-played",
          "developer_name": "HOME_MATCHES",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200404,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 137,
        "value": 4,
        "type": {
          "id": 137,
          "name": "Home Draw",
          "code": "home-draw",
          "developer_name": "HOME_DRAWS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200405,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 138,
        "value": 7,
        "type": {
          "id": 138,
          "name": "Home Lost",
          "code": "home-lost",
          "developer_name": "HOME_LOST",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200415,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 145,
        "value": 35,
        "type": {
          "id": 145,
          "name": "Away Goals Scored",
          "code": "away-scored",
          "developer_name": "AWAY_SCORED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200416,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 146,
        "value": 30,
        "type": {
          "id": 146,
          "name": "Away Goals Conceded",
          "code": "away-conceded",
          "developer_name": "AWAY_CONCEDED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200409,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 187,
        "value": 56,
        "type": {
          "id": 187,
          "name": "Overall Points",
          "code": "overall-points",
          "developer_name": "TOTAL_POINTS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200410,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 141,
        "value": 19,
        "type": {
          "id": 141,
          "name": "Away Matched Played",
          "code": "away-matches-played",
          "developer_name": "AWAY_MATCHES",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200412,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 143,
        "value": 7,
        "type": {
          "id": 143,
          "name": "Away Draw",
          "code": "away-draw",
          "developer_name": "AWAY_DRAWS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200413,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 144,
        "value": 5,
        "type": {
          "id": 144,
          "name": "Away Lost",
          "code": "away-lost",
          "developer_name": "AWAY_LOST",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200396,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 133,
        "value": 58,
        "type": {
          "id": 133,
          "name": "Overal Goals Scored",
          "code": "overall-goals-for",
          "developer_name": "OVERALL_SCORED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200397,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 134,
        "value": 46,
        "type": {
          "id": 134,
          "name": "Overall Goals Conceded",
          "code": "overall-goals-against",
          "developer_name": "OVERALL_CONCEDED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200399,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 130,
        "value": 15,
        "type": {
          "id": 130,
          "name": "Overall Won",
          "code": "overall-won",
          "developer_name": "OVERALL_WINS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200400,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 131,
        "value": 11,
        "type": {
          "id": 131,
          "name": "Overall Draw",
          "code": "overall-draw",
          "developer_name": "OVERALL_DRAWS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200403,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 136,
        "value": 8,
        "type": {
          "id": 136,
          "name": "Home Won",
          "code": "home-won",
          "developer_name": "HOME_WINS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200406,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 185,
        "value": 28,
        "type": {
          "id": 185,
          "name": "Home Points",
          "code": "home-points",
          "developer_name": "HOME_POINTS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200407,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 139,
        "value": 23,
        "type": {
          "id": 139,
          "name": "Home Goals Scored",
          "code": "home-scored",
          "developer_name": "HOME_SCORED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200408,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 140,
        "value": 16,
        "type": {
          "id": 140,
          "name": "Home Goals Conceded",
          "code": "home-conceded",
          "developer_name": "HOME_CONCEDED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200411,
        "standing_type": "standing",
        "standing_id": 229315,
        "type_id": 142,
        "value": 7,
        "type": {
          "id": 142,
          "name": "Away Won",
          "code": "away-won",
          "developer_name": "AWAY_WINS",
          "model_type": "standings",
          "stat_group": "away"
        }
      }
    ],
    "form": [
      {
        "id": 2203118767,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134458,
        "form": "D",
        "sort_order": 1
      },
      {
        "id": 2219824332,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134463,
        "form": "D",
        "sort_order": 2
      },
      {
        "id": 2231104954,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134476,
        "form": "W",
        "sort_order": 3
      },
      {
        "id": 2271345160,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134488,
        "form": "L",
        "sort_order": 5
      },
      {
        "id": 2293631107,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134493,
        "form": "W",
        "sort_order": 6
      },
      {
        "id": 2302737016,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134510,
        "form": "L",
        "sort_order": 7
      },
      {
        "id": 2331045506,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134513,
        "form": "W",
        "sort_order": 8
      },
      {
        "id": 2346793024,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134524,
        "form": "D",
        "sort_order": 9
      },
      {
        "id": 2380375399,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134533,
        "form": "L",
        "sort_order": 11
      },
      {
        "id": 2451343203,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134548,
        "form": "W",
        "sort_order": 15
      },
      {
        "id": 2573726789,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134560,
        "form": "D",
        "sort_order": 21
      },
      {
        "id": 2832964343,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134563,
        "form": "L",
        "sort_order": 24
      },
      {
        "id": 3091788662,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134580,
        "form": "W",
        "sort_order": 25
      },
      {
        "id": 3237536711,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134583,
        "form": "L",
        "sort_order": 26
      },
      {
        "id": 2410185118,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134593,
        "form": "L",
        "sort_order": 12
      },
      {
        "id": 2427908083,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134612,
        "form": "W",
        "sort_order": 13
      },
      {
        "id": 2598658844,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134620,
        "form": "W",
        "sort_order": 22
      },
      {
        "id": 2257163365,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134623,
        "form": "L",
        "sort_order": 4
      },
      {
        "id": 2470017207,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134633,
        "form": "D",
        "sort_order": 16
      },
      {
        "id": 2721177203,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134643,
        "form": "W",
        "sort_order": 23
      },
      {
        "id": 2361990808,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134869,
        "form": "W",
        "sort_order": 10
      },
      {
        "id": 2440274248,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134879,
        "form": "W",
        "sort_order": 14
      },
      {
        "id": 2482007150,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134896,
        "form": "W",
        "sort_order": 17
      },
      {
        "id": 2487030042,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134899,
        "form": "D",
        "sort_order": 18
      },
      {
        "id": 2491501098,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134913,
        "form": "D",
        "sort_order": 19
      },
      {
        "id": 2497493559,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134919,
        "form": "W",
        "sort_order": 20
      },
      {
        "id": 3313368543,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134930,
        "form": "L",
        "sort_order": 27
      },
      {
        "id": 3637171475,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134946,
        "form": "D",
        "sort_order": 28
      },
      {
        "id": 3788117427,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134949,
        "form": "L",
        "sort_order": 29
      },
      {
        "id": 4226061056,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134959,
        "form": "L",
        "sort_order": 30
      },
      {
        "id": 4317110480,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134978,
        "form": "D",
        "sort_order": 31
      },
      {
        "id": 4647348712,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134979,
        "form": "W",
        "sort_order": 32
      },
      {
        "id": 4770516402,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134991,
        "form": "D",
        "sort_order": 33
      },
      {
        "id": 4994035462,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19134999,
        "form": "D",
        "sort_order": 34
      },
      {
        "id": 5131054208,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19135009,
        "form": "W",
        "sort_order": 35
      },
      {
        "id": 5295887214,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19135019,
        "form": "L",
        "sort_order": 36
      },
      {
        "id": 5516111713,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19135037,
        "form": "L",
        "sort_order": 37
      },
      {
        "id": 5619543864,
        "standing_type": "standing",
        "standing_id": 229315,
        "fixture_id": 19135039,
        "form": "W",
        "sort_order": 38
      }
    ],
    "stage": {
      "id": 77471288,
      "sport_id": 1,
      "league_id": 8,
      "season_id": 23614,
      "type_id": 223,
      "name": "Regular Season",
      "sort_order": 1,
      "finished": true,
      "is_current": false,
      "starting_at": "2024-08-16",
      "ending_at": "2025-05-25",
      "games_in_current_week": false,
      "tie_breaker_rule_id": null
    },
    "league": {
      "id": 8,
      "sport_id": 1,
      "country_id": 462,
      "name": "Premier League",
      "active": true,
      "short_code": "UK PL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/leagues/8/8.png",
      "type": "league",
      "sub_type": "domestic",
      "last_played_at": "2025-05-25 15:00:00",
      "category": 1,
      "has_jerseys": false
    },
    "group": null
  },
  {
    "id": 229318,
    "participant_id": 236,
    "sport_id": 1,
    "league_id": 8,
    "season_id": 23614,
    "stage_id": 77471288,
    "group_id": null,
    "round_id": 339273,
    "standing_rule_id": null,
    "position": 10,
    "result": "down",
    "points": 56,
    "participant": {
      "id": 236,
      "sport_id": 1,
      "country_id": 462,
      "venue_id": 338817,
      "gender": "male",
      "name": "Brentford",
      "short_code": "BRE",
      "image_path": "https://cdn.sportmonks.com/images/soccer/teams/12/236.png",
      "founded": 1889,
      "type": "domestic",
      "placeholder": false,
      "last_played_at": "2025-05-25 15:00:00"
    },
    "rule": null,
    "details": [
      {
        "id": 3131200482,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 146,
        "value": 22,
        "type": {
          "id": 146,
          "name": "Away Goals Conceded",
          "code": "away-conceded",
          "developer_name": "AWAY_CONCEDED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3430924648,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 7939,
        "value": 50,
        "type": {
          "id": 7939,
          "name": "Expected Points (xPTS)",
          "code": "expected-points",
          "developer_name": "EXPECTED_POINTS",
          "model_type": "statistic",
          "stat_group": "offensive"
        }
      },
      {
        "id": 3131200473,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 139,
        "value": 40,
        "type": {
          "id": 139,
          "name": "Home Goals Scored",
          "code": "home-scored",
          "developer_name": "HOME_SCORED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200464,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 129,
        "value": 38,
        "type": {
          "id": 129,
          "name": "Overall Matches Played",
          "code": "overall-matches-played",
          "developer_name": "OVERALL_MATCHES",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200475,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 187,
        "value": 56,
        "type": {
          "id": 187,
          "name": "Overall Points",
          "code": "overall-points",
          "developer_name": "TOTAL_POINTS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200478,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 143,
        "value": 4,
        "type": {
          "id": 143,
          "name": "Away Draw",
          "code": "away-draw",
          "developer_name": "AWAY_DRAWS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200481,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 145,
        "value": 26,
        "type": {
          "id": 145,
          "name": "Away Goals Scored",
          "code": "away-scored",
          "developer_name": "AWAY_SCORED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200462,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 133,
        "value": 66,
        "type": {
          "id": 133,
          "name": "Overal Goals Scored",
          "code": "overall-goals-for",
          "developer_name": "OVERALL_SCORED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200463,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 134,
        "value": 57,
        "type": {
          "id": 134,
          "name": "Overall Goals Conceded",
          "code": "overall-goals-against",
          "developer_name": "OVERALL_CONCEDED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200465,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 130,
        "value": 16,
        "type": {
          "id": 130,
          "name": "Overall Won",
          "code": "overall-won",
          "developer_name": "OVERALL_WINS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200466,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 131,
        "value": 8,
        "type": {
          "id": 131,
          "name": "Overall Draw",
          "code": "overall-draw",
          "developer_name": "OVERALL_DRAWS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200476,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 141,
        "value": 19,
        "type": {
          "id": 141,
          "name": "Away Matched Played",
          "code": "away-matches-played",
          "developer_name": "AWAY_MATCHES",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200474,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 140,
        "value": 35,
        "type": {
          "id": 140,
          "name": "Home Goals Conceded",
          "code": "home-conceded",
          "developer_name": "HOME_CONCEDED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200467,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 132,
        "value": 14,
        "type": {
          "id": 132,
          "name": "Overall Lost",
          "code": "overall-lost",
          "developer_name": "OVERALL_LOST",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200468,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 135,
        "value": 19,
        "type": {
          "id": 135,
          "name": "Home Matched Played",
          "code": "home-matches-played",
          "developer_name": "HOME_MATCHES",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200469,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 136,
        "value": 9,
        "type": {
          "id": 136,
          "name": "Home Won",
          "code": "home-won",
          "developer_name": "HOME_WINS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200470,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 137,
        "value": 4,
        "type": {
          "id": 137,
          "name": "Home Draw",
          "code": "home-draw",
          "developer_name": "HOME_DRAWS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200471,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 138,
        "value": 6,
        "type": {
          "id": 138,
          "name": "Home Lost",
          "code": "home-lost",
          "developer_name": "HOME_LOST",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200472,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 185,
        "value": 31,
        "type": {
          "id": 185,
          "name": "Home Points",
          "code": "home-points",
          "developer_name": "HOME_POINTS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200477,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 142,
        "value": 7,
        "type": {
          "id": 142,
          "name": "Away Won",
          "code": "away-won",
          "developer_name": "AWAY_WINS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200479,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 144,
        "value": 8,
        "type": {
          "id": 144,
          "name": "Away Lost",
          "code": "away-lost",
          "developer_name": "AWAY_LOST",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200480,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 186,
        "value": 25,
        "type": {
          "id": 186,
          "name": "Away Points",
          "code": "away-points",
          "developer_name": "AWAY_POINTS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200483,
        "standing_type": "standing",
        "standing_id": 229318,
        "type_id": 179,
        "value": 9,
        "type": {
          "id": 179,
          "name": "Goal Difference",
          "code": "goal-difference",
          "developer_name": "OVERALL_GOAL_DIFFERENCE",
          "model_type": "standings",
          "stat_group": "overall"
        }
      }
    ],
    "form": [
      {
        "id": 2205412616,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134460,
        "form": "W",
        "sort_order": 1
      },
      {
        "id": 2220180244,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134468,
        "form": "L",
        "sort_order": 2
      },
      {
        "id": 2231104680,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134474,
        "form": "W",
        "sort_order": 3
      },
      {
        "id": 2271345049,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134491,
        "form": "L",
        "sort_order": 5
      },
      {
        "id": 2287564188,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134495,
        "form": "D",
        "sort_order": 6
      },
      {
        "id": 2302736894,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134505,
        "form": "W",
        "sort_order": 7
      },
      {
        "id": 2330386311,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134517,
        "form": "L",
        "sort_order": 8
      },
      {
        "id": 2346792881,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134525,
        "form": "W",
        "sort_order": 9
      },
      {
        "id": 2380375071,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134533,
        "form": "W",
        "sort_order": 11
      },
      {
        "id": 2446975632,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134544,
        "form": "W",
        "sort_order": 15
      },
      {
        "id": 2573555631,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134554,
        "form": "D",
        "sort_order": 21
      },
      {
        "id": 2871423631,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134565,
        "form": "L",
        "sort_order": 24
      },
      {
        "id": 3092013228,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134582,
        "form": "W",
        "sort_order": 25
      },
      {
        "id": 3196138847,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134589,
        "form": "W",
        "sort_order": 26
      },
      {
        "id": 2410070553,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134596,
        "form": "D",
        "sort_order": 12
      },
      {
        "id": 2427851879,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134603,
        "form": "W",
        "sort_order": 13
      },
      {
        "id": 2616721501,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134614,
        "form": "L",
        "sort_order": 22
      },
      {
        "id": 2256382983,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134629,
        "form": "L",
        "sort_order": 4
      },
      {
        "id": 2468878696,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134636,
        "form": "L",
        "sort_order": 16
      },
      {
        "id": 2758038398,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134646,
        "form": "W",
        "sort_order": 23
      },
      {
        "id": 2369305126,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134870,
        "form": "L",
        "sort_order": 10
      },
      {
        "id": 2439001515,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134881,
        "form": "L",
        "sort_order": 14
      },
      {
        "id": 2478847075,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134890,
        "form": "L",
        "sort_order": 17
      },
      {
        "id": 2488696395,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134901,
        "form": "D",
        "sort_order": 18
      },
      {
        "id": 2494466867,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134910,
        "form": "L",
        "sort_order": 19
      },
      {
        "id": 2497546252,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134926,
        "form": "W",
        "sort_order": 20
      },
      {
        "id": 3322505990,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134929,
        "form": "D",
        "sort_order": 27
      },
      {
        "id": 3587207521,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134939,
        "form": "L",
        "sort_order": 28
      },
      {
        "id": 3788117716,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134949,
        "form": "W",
        "sort_order": 29
      },
      {
        "id": 4226139043,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134966,
        "form": "L",
        "sort_order": 30
      },
      {
        "id": 4385178561,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134970,
        "form": "D",
        "sort_order": 31
      },
      {
        "id": 4561674105,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134980,
        "form": "D",
        "sort_order": 32
      },
      {
        "id": 4773566489,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19134990,
        "form": "W",
        "sort_order": 33
      },
      {
        "id": 5057730568,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19135006,
        "form": "W",
        "sort_order": 34
      },
      {
        "id": 5170319879,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19135011,
        "form": "W",
        "sort_order": 35
      },
      {
        "id": 5284603360,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19135021,
        "form": "W",
        "sort_order": 36
      },
      {
        "id": 5491046676,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19135031,
        "form": "L",
        "sort_order": 37
      },
      {
        "id": 5619543962,
        "standing_type": "standing",
        "standing_id": 229318,
        "fixture_id": 19135048,
        "form": "D",
        "sort_order": 38
      }
    ],
    "stage": {
      "id": 77471288,
      "sport_id": 1,
      "league_id": 8,
      "season_id": 23614,
      "type_id": 223,
      "name": "Regular Season",
      "sort_order": 1,
      "finished": true,
      "is_current": false,
      "starting_at": "2024-08-16",
      "ending_at": "2025-05-25",
      "games_in_current_week": false,
      "tie_breaker_rule_id": null
    },
    "league": {
      "id": 8,
      "sport_id": 1,
      "country_id": 462,
      "name": "Premier League",
      "active": true,
      "short_code": "UK PL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/leagues/8/8.png",
      "type": "league",
      "sub_type": "domestic",
      "last_played_at": "2025-05-25 15:00:00",
      "category": 1,
      "has_jerseys": false
    },
    "group": null
  },
  {
    "id": 229323,
    "participant_id": 11,
    "sport_id": 1,
    "league_id": 8,
    "season_id": 23614,
    "stage_id": 77471288,
    "group_id": null,
    "round_id": 339273,
    "standing_rule_id": null,
    "position": 11,
    "result": "down",
    "points": 54,
    "participant": {
      "id": 11,
      "sport_id": 1,
      "country_id": 462,
      "venue_id": 485,
      "gender": "male",
      "name": "Fulham",
      "short_code": "FUL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/teams/11/11.png",
      "founded": 1879,
      "type": "domestic",
      "placeholder": false,
      "last_played_at": "2025-05-25 15:00:00"
    },
    "rule": null,
    "details": [
      {
        "id": 3417350880,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 7939,
        "value": 57,
        "type": {
          "id": 7939,
          "name": "Expected Points (xPTS)",
          "code": "expected-points",
          "developer_name": "EXPECTED_POINTS",
          "model_type": "statistic",
          "stat_group": "offensive"
        }
      },
      {
        "id": 3131200583,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 139,
        "value": 27,
        "type": {
          "id": 139,
          "name": "Home Goals Scored",
          "code": "home-scored",
          "developer_name": "HOME_SCORED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200580,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 137,
        "value": 5,
        "type": {
          "id": 137,
          "name": "Home Draw",
          "code": "home-draw",
          "developer_name": "HOME_DRAWS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200572,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 133,
        "value": 54,
        "type": {
          "id": 133,
          "name": "Overal Goals Scored",
          "code": "overall-goals-for",
          "developer_name": "OVERALL_SCORED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200576,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 131,
        "value": 9,
        "type": {
          "id": 131,
          "name": "Overall Draw",
          "code": "overall-draw",
          "developer_name": "OVERALL_DRAWS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200579,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 136,
        "value": 7,
        "type": {
          "id": 136,
          "name": "Home Won",
          "code": "home-won",
          "developer_name": "HOME_WINS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200581,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 138,
        "value": 7,
        "type": {
          "id": 138,
          "name": "Home Lost",
          "code": "home-lost",
          "developer_name": "HOME_LOST",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200585,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 187,
        "value": 54,
        "type": {
          "id": 187,
          "name": "Overall Points",
          "code": "overall-points",
          "developer_name": "TOTAL_POINTS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200590,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 186,
        "value": 28,
        "type": {
          "id": 186,
          "name": "Away Points",
          "code": "away-points",
          "developer_name": "AWAY_POINTS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200578,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 135,
        "value": 19,
        "type": {
          "id": 135,
          "name": "Home Matched Played",
          "code": "home-matches-played",
          "developer_name": "HOME_MATCHES",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200592,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 146,
        "value": 24,
        "type": {
          "id": 146,
          "name": "Away Goals Conceded",
          "code": "away-conceded",
          "developer_name": "AWAY_CONCEDED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200573,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 134,
        "value": 54,
        "type": {
          "id": 134,
          "name": "Overall Goals Conceded",
          "code": "overall-goals-against",
          "developer_name": "OVERALL_CONCEDED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200574,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 129,
        "value": 38,
        "type": {
          "id": 129,
          "name": "Overall Matches Played",
          "code": "overall-matches-played",
          "developer_name": "OVERALL_MATCHES",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200575,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 130,
        "value": 15,
        "type": {
          "id": 130,
          "name": "Overall Won",
          "code": "overall-won",
          "developer_name": "OVERALL_WINS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200577,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 132,
        "value": 14,
        "type": {
          "id": 132,
          "name": "Overall Lost",
          "code": "overall-lost",
          "developer_name": "OVERALL_LOST",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200582,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 185,
        "value": 26,
        "type": {
          "id": 185,
          "name": "Home Points",
          "code": "home-points",
          "developer_name": "HOME_POINTS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200584,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 140,
        "value": 30,
        "type": {
          "id": 140,
          "name": "Home Goals Conceded",
          "code": "home-conceded",
          "developer_name": "HOME_CONCEDED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200586,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 141,
        "value": 19,
        "type": {
          "id": 141,
          "name": "Away Matched Played",
          "code": "away-matches-played",
          "developer_name": "AWAY_MATCHES",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200587,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 142,
        "value": 8,
        "type": {
          "id": 142,
          "name": "Away Won",
          "code": "away-won",
          "developer_name": "AWAY_WINS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200588,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 143,
        "value": 4,
        "type": {
          "id": 143,
          "name": "Away Draw",
          "code": "away-draw",
          "developer_name": "AWAY_DRAWS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200589,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 144,
        "value": 7,
        "type": {
          "id": 144,
          "name": "Away Lost",
          "code": "away-lost",
          "developer_name": "AWAY_LOST",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200591,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 145,
        "value": 27,
        "type": {
          "id": 145,
          "name": "Away Goals Scored",
          "code": "away-scored",
          "developer_name": "AWAY_SCORED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200593,
        "standing_type": "standing",
        "standing_id": 229323,
        "type_id": 179,
        "value": 0,
        "type": {
          "id": 179,
          "name": "Goal Difference",
          "code": "goal-difference",
          "developer_name": "OVERALL_GOAL_DIFFERENCE",
          "model_type": "standings",
          "stat_group": "overall"
        }
      }
    ],
    "form": [
      {
        "id": 2200759468,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134453,
        "form": "L",
        "sort_order": 1
      },
      {
        "id": 2217305349,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134467,
        "form": "W",
        "sort_order": 2
      },
      {
        "id": 2231105825,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134477,
        "form": "D",
        "sort_order": 3
      },
      {
        "id": 2271344719,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134486,
        "form": "W",
        "sort_order": 5
      },
      {
        "id": 2287563891,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134501,
        "form": "W",
        "sort_order": 6
      },
      {
        "id": 2302736819,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134511,
        "form": "L",
        "sort_order": 7
      },
      {
        "id": 2330386212,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134514,
        "form": "L",
        "sort_order": 8
      },
      {
        "id": 2347347233,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134529,
        "form": "D",
        "sort_order": 9
      },
      {
        "id": 2380289135,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134536,
        "form": "W",
        "sort_order": 11
      },
      {
        "id": 2451305124,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134547,
        "form": "D",
        "sort_order": 15
      },
      {
        "id": 2573555532,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134559,
        "form": "L",
        "sort_order": 21
      },
      {
        "id": 2832964532,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134570,
        "form": "W",
        "sort_order": 24
      },
      {
        "id": 3091789004,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134576,
        "form": "W",
        "sort_order": 25
      },
      {
        "id": 3237638874,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134587,
        "form": "L",
        "sort_order": 26
      },
      {
        "id": 2410184399,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134597,
        "form": "L",
        "sort_order": 12
      },
      {
        "id": 2432455272,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134610,
        "form": "D",
        "sort_order": 13
      },
      {
        "id": 2616446082,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134618,
        "form": "W",
        "sort_order": 22
      },
      {
        "id": 2256383425,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134627,
        "form": "D",
        "sort_order": 4
      },
      {
        "id": 2463649475,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134637,
        "form": "D",
        "sort_order": 16
      },
      {
        "id": 2767239233,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134647,
        "form": "L",
        "sort_order": 23
      },
      {
        "id": 2369305096,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134870,
        "form": "W",
        "sort_order": 10
      },
      {
        "id": 2440264260,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134883,
        "form": "W",
        "sort_order": 14
      },
      {
        "id": 2482031413,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134893,
        "form": "D",
        "sort_order": 17
      },
      {
        "id": 2487106968,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134902,
        "form": "W",
        "sort_order": 18
      },
      {
        "id": 2491501135,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134913,
        "form": "D",
        "sort_order": 19
      },
      {
        "id": 2499663390,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134923,
        "form": "D",
        "sort_order": 20
      },
      {
        "id": 3313368835,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134934,
        "form": "W",
        "sort_order": 27
      },
      {
        "id": 3573043598,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134940,
        "form": "L",
        "sort_order": 28
      },
      {
        "id": 3829544577,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134953,
        "form": "W",
        "sort_order": 29
      },
      {
        "id": 4211882156,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134960,
        "form": "L",
        "sort_order": 30
      },
      {
        "id": 4385178438,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134973,
        "form": "W",
        "sort_order": 31
      },
      {
        "id": 4647348744,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134979,
        "form": "L",
        "sort_order": 32
      },
      {
        "id": 4807288441,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19134993,
        "form": "L",
        "sort_order": 33
      },
      {
        "id": 4944297998,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19135007,
        "form": "W",
        "sort_order": 34
      },
      {
        "id": 5099040286,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19135010,
        "form": "L",
        "sort_order": 35
      },
      {
        "id": 5285373651,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19135020,
        "form": "L",
        "sort_order": 36
      },
      {
        "id": 5491046749,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19135031,
        "form": "W",
        "sort_order": 37
      },
      {
        "id": 5619883421,
        "standing_type": "standing",
        "standing_id": 229323,
        "fixture_id": 19135040,
        "form": "L",
        "sort_order": 38
      }
    ],
    "stage": {
      "id": 77471288,
      "sport_id": 1,
      "league_id": 8,
      "season_id": 23614,
      "type_id": 223,
      "name": "Regular Season",
      "sort_order": 1,
      "finished": true,
      "is_current": false,
      "starting_at": "2024-08-16",
      "ending_at": "2025-05-25",
      "games_in_current_week": false,
      "tie_breaker_rule_id": null
    },
    "league": {
      "id": 8,
      "sport_id": 1,
      "country_id": 462,
      "name": "Premier League",
      "active": true,
      "short_code": "UK PL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/leagues/8/8.png",
      "type": "league",
      "sub_type": "domestic",
      "last_played_at": "2025-05-25 15:00:00",
      "category": 1,
      "has_jerseys": false
    },
    "group": null
  },
  {
    "id": 229321,
    "participant_id": 51,
    "sport_id": 1,
    "league_id": 8,
    "season_id": 23614,
    "stage_id": 77471288,
    "group_id": null,
    "round_id": 339273,
    "standing_rule_id": null,
    "position": 12,
    "result": "equal",
    "points": 53,
    "participant": {
      "id": 51,
      "sport_id": 1,
      "country_id": 462,
      "venue_id": 201,
      "gender": "male",
      "name": "Crystal Palace",
      "short_code": "CRY",
      "image_path": "https://cdn.sportmonks.com/images/soccer/teams/19/51.png",
      "founded": 1905,
      "type": "domestic",
      "placeholder": false,
      "last_played_at": "2025-05-25 15:00:00"
    },
    "rule": null,
    "details": [
      {
        "id": 3131200528,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 133,
        "value": 51,
        "type": {
          "id": 133,
          "name": "Overal Goals Scored",
          "code": "overall-goals-for",
          "developer_name": "OVERALL_SCORED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200529,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 134,
        "value": 51,
        "type": {
          "id": 134,
          "name": "Overall Goals Conceded",
          "code": "overall-goals-against",
          "developer_name": "OVERALL_CONCEDED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200547,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 145,
        "value": 27,
        "type": {
          "id": 145,
          "name": "Away Goals Scored",
          "code": "away-scored",
          "developer_name": "AWAY_SCORED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200546,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 186,
        "value": 28,
        "type": {
          "id": 186,
          "name": "Away Points",
          "code": "away-points",
          "developer_name": "AWAY_POINTS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3430924671,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 7939,
        "value": 56,
        "type": {
          "id": 7939,
          "name": "Expected Points (xPTS)",
          "code": "expected-points",
          "developer_name": "EXPECTED_POINTS",
          "model_type": "statistic",
          "stat_group": "offensive"
        }
      },
      {
        "id": 3131200538,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 185,
        "value": 25,
        "type": {
          "id": 185,
          "name": "Home Points",
          "code": "home-points",
          "developer_name": "HOME_POINTS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200539,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 139,
        "value": 24,
        "type": {
          "id": 139,
          "name": "Home Goals Scored",
          "code": "home-scored",
          "developer_name": "HOME_SCORED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200540,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 140,
        "value": 26,
        "type": {
          "id": 140,
          "name": "Home Goals Conceded",
          "code": "home-conceded",
          "developer_name": "HOME_CONCEDED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200541,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 187,
        "value": 53,
        "type": {
          "id": 187,
          "name": "Overall Points",
          "code": "overall-points",
          "developer_name": "TOTAL_POINTS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200530,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 129,
        "value": 38,
        "type": {
          "id": 129,
          "name": "Overall Matches Played",
          "code": "overall-matches-played",
          "developer_name": "OVERALL_MATCHES",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200531,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 130,
        "value": 13,
        "type": {
          "id": 130,
          "name": "Overall Won",
          "code": "overall-won",
          "developer_name": "OVERALL_WINS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200532,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 131,
        "value": 14,
        "type": {
          "id": 131,
          "name": "Overall Draw",
          "code": "overall-draw",
          "developer_name": "OVERALL_DRAWS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200533,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 132,
        "value": 11,
        "type": {
          "id": 132,
          "name": "Overall Lost",
          "code": "overall-lost",
          "developer_name": "OVERALL_LOST",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200534,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 135,
        "value": 19,
        "type": {
          "id": 135,
          "name": "Home Matched Played",
          "code": "home-matches-played",
          "developer_name": "HOME_MATCHES",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200535,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 136,
        "value": 6,
        "type": {
          "id": 136,
          "name": "Home Won",
          "code": "home-won",
          "developer_name": "HOME_WINS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200536,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 137,
        "value": 7,
        "type": {
          "id": 137,
          "name": "Home Draw",
          "code": "home-draw",
          "developer_name": "HOME_DRAWS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200537,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 138,
        "value": 6,
        "type": {
          "id": 138,
          "name": "Home Lost",
          "code": "home-lost",
          "developer_name": "HOME_LOST",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200542,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 141,
        "value": 19,
        "type": {
          "id": 141,
          "name": "Away Matched Played",
          "code": "away-matches-played",
          "developer_name": "AWAY_MATCHES",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200543,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 142,
        "value": 7,
        "type": {
          "id": 142,
          "name": "Away Won",
          "code": "away-won",
          "developer_name": "AWAY_WINS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200544,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 143,
        "value": 7,
        "type": {
          "id": 143,
          "name": "Away Draw",
          "code": "away-draw",
          "developer_name": "AWAY_DRAWS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200545,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 144,
        "value": 5,
        "type": {
          "id": 144,
          "name": "Away Lost",
          "code": "away-lost",
          "developer_name": "AWAY_LOST",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200548,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 146,
        "value": 25,
        "type": {
          "id": 146,
          "name": "Away Goals Conceded",
          "code": "away-conceded",
          "developer_name": "AWAY_CONCEDED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200549,
        "standing_type": "standing",
        "standing_id": 229321,
        "type_id": 179,
        "value": 0,
        "type": {
          "id": 179,
          "name": "Goal Difference",
          "code": "goal-difference",
          "developer_name": "OVERALL_GOAL_DIFFERENCE",
          "model_type": "standings",
          "stat_group": "overall"
        }
      }
    ],
    "form": [
      {
        "id": 2205412707,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134460,
        "form": "L",
        "sort_order": 1
      },
      {
        "id": 2217305478,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134466,
        "form": "L",
        "sort_order": 2
      },
      {
        "id": 2233280654,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134475,
        "form": "D",
        "sort_order": 3
      },
      {
        "id": 2271897276,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134485,
        "form": "D",
        "sort_order": 5
      },
      {
        "id": 2287564401,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134497,
        "form": "L",
        "sort_order": 6
      },
      {
        "id": 2301449422,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134508,
        "form": "L",
        "sort_order": 7
      },
      {
        "id": 2337232573,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134519,
        "form": "L",
        "sort_order": 8
      },
      {
        "id": 2350884657,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134528,
        "form": "W",
        "sort_order": 9
      },
      {
        "id": 2380290877,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134536,
        "form": "L",
        "sort_order": 11
      },
      {
        "id": 2446977865,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134545,
        "form": "D",
        "sort_order": 15
      },
      {
        "id": 2580128348,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134557,
        "form": "W",
        "sort_order": 21
      },
      {
        "id": 2871517999,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134569,
        "form": "W",
        "sort_order": 24
      },
      {
        "id": 3102194783,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134575,
        "form": "L",
        "sort_order": 25
      },
      {
        "id": 3237639182,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134587,
        "form": "W",
        "sort_order": 26
      },
      {
        "id": 2410185786,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134595,
        "form": "D",
        "sort_order": 12
      },
      {
        "id": 2427854191,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134606,
        "form": "D",
        "sort_order": 13
      },
      {
        "id": 2616446750,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134622,
        "form": "W",
        "sort_order": 22
      },
      {
        "id": 2256383863,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134626,
        "form": "D",
        "sort_order": 4
      },
      {
        "id": 2467848865,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134635,
        "form": "W",
        "sort_order": 16
      },
      {
        "id": 2758038587,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134646,
        "form": "L",
        "sort_order": 23
      },
      {
        "id": 2362550318,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134878,
        "form": "D",
        "sort_order": 10
      },
      {
        "id": 2437042349,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134884,
        "form": "W",
        "sort_order": 14
      },
      {
        "id": 2479507919,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134891,
        "form": "L",
        "sort_order": 17
      },
      {
        "id": 2487030357,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134899,
        "form": "D",
        "sort_order": 18
      },
      {
        "id": 2491461518,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134911,
        "form": "W",
        "sort_order": 19
      },
      {
        "id": 2497493751,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134922,
        "form": "D",
        "sort_order": 20
      },
      {
        "id": 3313369153,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134935,
        "form": "W",
        "sort_order": 27
      },
      {
        "id": 3572371967,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134942,
        "form": "W",
        "sort_order": 28
      },
      {
        "id": 4666974178,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134957,
        "form": "L",
        "sort_order": 32
      },
      {
        "id": 4226116422,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134967,
        "form": "D",
        "sort_order": 29
      },
      {
        "id": 4317266857,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134971,
        "form": "W",
        "sort_order": 30
      },
      {
        "id": 4493909106,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134984,
        "form": "L",
        "sort_order": 31
      },
      {
        "id": 4770516899,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19134991,
        "form": "D",
        "sort_order": 33
      },
      {
        "id": 4872165737,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19135000,
        "form": "D",
        "sort_order": 34
      },
      {
        "id": 5201336876,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19135014,
        "form": "D",
        "sort_order": 35
      },
      {
        "id": 5329995809,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19135027,
        "form": "W",
        "sort_order": 36
      },
      {
        "id": 5516111752,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19135034,
        "form": "W",
        "sort_order": 37
      },
      {
        "id": 5619544097,
        "standing_type": "standing",
        "standing_id": 229321,
        "fixture_id": 19135042,
        "form": "D",
        "sort_order": 38
      }
    ],
    "stage": {
      "id": 77471288,
      "sport_id": 1,
      "league_id": 8,
      "season_id": 23614,
      "type_id": 223,
      "name": "Regular Season",
      "sort_order": 1,
      "finished": true,
      "is_current": false,
      "starting_at": "2024-08-16",
      "ending_at": "2025-05-25",
      "games_in_current_week": false,
      "tie_breaker_rule_id": null
    },
    "league": {
      "id": 8,
      "sport_id": 1,
      "country_id": 462,
      "name": "Premier League",
      "active": true,
      "short_code": "UK PL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/leagues/8/8.png",
      "type": "league",
      "sub_type": "domestic",
      "last_played_at": "2025-05-25 15:00:00",
      "category": 1,
      "has_jerseys": false
    },
    "group": null
  },
  {
    "id": 229322,
    "participant_id": 13,
    "sport_id": 1,
    "league_id": 8,
    "season_id": 23614,
    "stage_id": 77471288,
    "group_id": null,
    "round_id": 339273,
    "standing_rule_id": null,
    "position": 13,
    "result": "equal",
    "points": 48,
    "participant": {
      "id": 13,
      "sport_id": 1,
      "country_id": 462,
      "venue_id": 12,
      "gender": "male",
      "name": "Everton",
      "short_code": "EVE",
      "image_path": "https://cdn.sportmonks.com/images/soccer/teams/13/13.png",
      "founded": 1878,
      "type": "domestic",
      "placeholder": false,
      "last_played_at": "2025-05-25 15:00:00"
    },
    "rule": null,
    "details": [
      {
        "id": 3131200563,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 187,
        "value": 48,
        "type": {
          "id": 187,
          "name": "Overall Points",
          "code": "overall-points",
          "developer_name": "TOTAL_POINTS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3424287417,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 7939,
        "value": 45,
        "type": {
          "id": 7939,
          "name": "Expected Points (xPTS)",
          "code": "expected-points",
          "developer_name": "EXPECTED_POINTS",
          "model_type": "statistic",
          "stat_group": "offensive"
        }
      },
      {
        "id": 3131200554,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 131,
        "value": 15,
        "type": {
          "id": 131,
          "name": "Overall Draw",
          "code": "overall-draw",
          "developer_name": "OVERALL_DRAWS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200561,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 139,
        "value": 26,
        "type": {
          "id": 139,
          "name": "Home Goals Scored",
          "code": "home-scored",
          "developer_name": "HOME_SCORED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200553,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 130,
        "value": 11,
        "type": {
          "id": 130,
          "name": "Overall Won",
          "code": "overall-won",
          "developer_name": "OVERALL_WINS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200552,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 129,
        "value": 38,
        "type": {
          "id": 129,
          "name": "Overall Matches Played",
          "code": "overall-matches-played",
          "developer_name": "OVERALL_MATCHES",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200565,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 142,
        "value": 6,
        "type": {
          "id": 142,
          "name": "Away Won",
          "code": "away-won",
          "developer_name": "AWAY_WINS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200569,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 145,
        "value": 16,
        "type": {
          "id": 145,
          "name": "Away Goals Scored",
          "code": "away-scored",
          "developer_name": "AWAY_SCORED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200571,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 179,
        "value": -2,
        "type": {
          "id": 179,
          "name": "Goal Difference",
          "code": "goal-difference",
          "developer_name": "OVERALL_GOAL_DIFFERENCE",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200551,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 134,
        "value": 44,
        "type": {
          "id": 134,
          "name": "Overall Goals Conceded",
          "code": "overall-goals-against",
          "developer_name": "OVERALL_CONCEDED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200564,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 141,
        "value": 19,
        "type": {
          "id": 141,
          "name": "Away Matched Played",
          "code": "away-matches-played",
          "developer_name": "AWAY_MATCHES",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200566,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 143,
        "value": 6,
        "type": {
          "id": 143,
          "name": "Away Draw",
          "code": "away-draw",
          "developer_name": "AWAY_DRAWS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200567,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 144,
        "value": 7,
        "type": {
          "id": 144,
          "name": "Away Lost",
          "code": "away-lost",
          "developer_name": "AWAY_LOST",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200568,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 186,
        "value": 24,
        "type": {
          "id": 186,
          "name": "Away Points",
          "code": "away-points",
          "developer_name": "AWAY_POINTS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200570,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 146,
        "value": 21,
        "type": {
          "id": 146,
          "name": "Away Goals Conceded",
          "code": "away-conceded",
          "developer_name": "AWAY_CONCEDED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200550,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 133,
        "value": 42,
        "type": {
          "id": 133,
          "name": "Overal Goals Scored",
          "code": "overall-goals-for",
          "developer_name": "OVERALL_SCORED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200555,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 132,
        "value": 12,
        "type": {
          "id": 132,
          "name": "Overall Lost",
          "code": "overall-lost",
          "developer_name": "OVERALL_LOST",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200556,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 135,
        "value": 19,
        "type": {
          "id": 135,
          "name": "Home Matched Played",
          "code": "home-matches-played",
          "developer_name": "HOME_MATCHES",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200557,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 136,
        "value": 5,
        "type": {
          "id": 136,
          "name": "Home Won",
          "code": "home-won",
          "developer_name": "HOME_WINS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200558,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 137,
        "value": 9,
        "type": {
          "id": 137,
          "name": "Home Draw",
          "code": "home-draw",
          "developer_name": "HOME_DRAWS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200559,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 138,
        "value": 5,
        "type": {
          "id": 138,
          "name": "Home Lost",
          "code": "home-lost",
          "developer_name": "HOME_LOST",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200560,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 185,
        "value": 24,
        "type": {
          "id": 185,
          "name": "Home Points",
          "code": "home-points",
          "developer_name": "HOME_POINTS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200562,
        "standing_type": "standing",
        "standing_id": 229322,
        "type_id": 140,
        "value": 23,
        "type": {
          "id": 140,
          "name": "Home Goals Conceded",
          "code": "home-conceded",
          "developer_name": "HOME_CONCEDED",
          "model_type": "standings",
          "stat_group": "home"
        }
      }
    ],
    "form": [
      {
        "id": 2203090560,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134456,
        "form": "L",
        "sort_order": 1
      },
      {
        "id": 2217305497,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134471,
        "form": "L",
        "sort_order": 2
      },
      {
        "id": 2231107452,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134476,
        "form": "L",
        "sort_order": 3
      },
      {
        "id": 2271412114,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134487,
        "form": "D",
        "sort_order": 5
      },
      {
        "id": 2287564343,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134497,
        "form": "W",
        "sort_order": 6
      },
      {
        "id": 2303215090,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134509,
        "form": "D",
        "sort_order": 7
      },
      {
        "id": 2330546060,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134515,
        "form": "W",
        "sort_order": 8
      },
      {
        "id": 2347347268,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134529,
        "form": "D",
        "sort_order": 9
      },
      {
        "id": 2380290731,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134541,
        "form": "D",
        "sort_order": 11
      },
      {
        "id": 3036246113,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134546,
        "form": "D",
        "sort_order": 24
      },
      {
        "id": 2580128486,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134555,
        "form": "L",
        "sort_order": 20
      },
      {
        "id": 2832964968,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134567,
        "form": "W",
        "sort_order": 23
      },
      {
        "id": 3102194839,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134575,
        "form": "W",
        "sort_order": 25
      },
      {
        "id": 3211578085,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134586,
        "form": "D",
        "sort_order": 26
      },
      {
        "id": 2410070840,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134596,
        "form": "D",
        "sort_order": 12
      },
      {
        "id": 2432365455,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134608,
        "form": "L",
        "sort_order": 13
      },
      {
        "id": 2652519081,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134616,
        "form": "W",
        "sort_order": 21
      },
      {
        "id": 2256761612,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134624,
        "form": "L",
        "sort_order": 4
      },
      {
        "id": 2463548807,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134634,
        "form": "D",
        "sort_order": 15
      },
      {
        "id": 2721887351,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134645,
        "form": "W",
        "sort_order": 22
      },
      {
        "id": 2362092217,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134876,
        "form": "L",
        "sort_order": 10
      },
      {
        "id": 2438823323,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134882,
        "form": "W",
        "sort_order": 14
      },
      {
        "id": 2481996747,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134892,
        "form": "D",
        "sort_order": 16
      },
      {
        "id": 2486210886,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134904,
        "form": "D",
        "sort_order": 17
      },
      {
        "id": 2491461536,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134912,
        "form": "L",
        "sort_order": 18
      },
      {
        "id": 2497493790,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134919,
        "form": "L",
        "sort_order": 19
      },
      {
        "id": 3322506152,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134929,
        "form": "D",
        "sort_order": 27
      },
      {
        "id": 3591246218,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134948,
        "form": "D",
        "sort_order": 28
      },
      {
        "id": 3772408927,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134952,
        "form": "D",
        "sort_order": 29
      },
      {
        "id": 4226347625,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134968,
        "form": "L",
        "sort_order": 30
      },
      {
        "id": 4274270020,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134972,
        "form": "D",
        "sort_order": 31
      },
      {
        "id": 4541764295,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134986,
        "form": "W",
        "sort_order": 32
      },
      {
        "id": 4770517220,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19134992,
        "form": "L",
        "sort_order": 33
      },
      {
        "id": 4916522937,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19135002,
        "form": "L",
        "sort_order": 34
      },
      {
        "id": 5121496989,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19135015,
        "form": "D",
        "sort_order": 35
      },
      {
        "id": 5285373749,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19135020,
        "form": "W",
        "sort_order": 36
      },
      {
        "id": 5476131248,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19135035,
        "form": "W",
        "sort_order": 37
      },
      {
        "id": 5619883535,
        "standing_type": "standing",
        "standing_id": 229322,
        "fixture_id": 19135044,
        "form": "W",
        "sort_order": 38
      }
    ],
    "stage": {
      "id": 77471288,
      "sport_id": 1,
      "league_id": 8,
      "season_id": 23614,
      "type_id": 223,
      "name": "Regular Season",
      "sort_order": 1,
      "finished": true,
      "is_current": false,
      "starting_at": "2024-08-16",
      "ending_at": "2025-05-25",
      "games_in_current_week": false,
      "tie_breaker_rule_id": null
    },
    "league": {
      "id": 8,
      "sport_id": 1,
      "country_id": 462,
      "name": "Premier League",
      "active": true,
      "short_code": "UK PL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/leagues/8/8.png",
      "type": "league",
      "sub_type": "domestic",
      "last_played_at": "2025-05-25 15:00:00",
      "category": 1,
      "has_jerseys": false
    },
    "group": null
  },
  {
    "id": 229333,
    "participant_id": 1,
    "sport_id": 1,
    "league_id": 8,
    "season_id": 23614,
    "stage_id": 77471288,
    "group_id": null,
    "round_id": 339273,
    "standing_rule_id": null,
    "position": 14,
    "result": "up",
    "points": 43,
    "participant": {
      "id": 1,
      "sport_id": 1,
      "country_id": 462,
      "venue_id": 214,
      "gender": "male",
      "name": "West Ham United",
      "short_code": "WHU",
      "image_path": "https://cdn.sportmonks.com/images/soccer/teams/1/1.png",
      "founded": 1895,
      "type": "domestic",
      "placeholder": false,
      "last_played_at": "2025-05-25 15:00:00"
    },
    "rule": null,
    "details": [
      {
        "id": 3425869151,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 7939,
        "value": 47,
        "type": {
          "id": 7939,
          "name": "Expected Points (xPTS)",
          "code": "expected-points",
          "developer_name": "EXPECTED_POINTS",
          "model_type": "statistic",
          "stat_group": "offensive"
        }
      },
      {
        "id": 3131200800,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 137,
        "value": 5,
        "type": {
          "id": 137,
          "name": "Home Draw",
          "code": "home-draw",
          "developer_name": "HOME_DRAWS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200801,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 138,
        "value": 9,
        "type": {
          "id": 138,
          "name": "Home Lost",
          "code": "home-lost",
          "developer_name": "HOME_LOST",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200799,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 136,
        "value": 5,
        "type": {
          "id": 136,
          "name": "Home Won",
          "code": "home-won",
          "developer_name": "HOME_WINS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200807,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 142,
        "value": 6,
        "type": {
          "id": 142,
          "name": "Away Won",
          "code": "away-won",
          "developer_name": "AWAY_WINS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200798,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 135,
        "value": 19,
        "type": {
          "id": 135,
          "name": "Home Matched Played",
          "code": "home-matches-played",
          "developer_name": "HOME_MATCHES",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200802,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 185,
        "value": 20,
        "type": {
          "id": 185,
          "name": "Home Points",
          "code": "home-points",
          "developer_name": "HOME_POINTS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200803,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 139,
        "value": 23,
        "type": {
          "id": 139,
          "name": "Home Goals Scored",
          "code": "home-scored",
          "developer_name": "HOME_SCORED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200797,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 132,
        "value": 17,
        "type": {
          "id": 132,
          "name": "Overall Lost",
          "code": "overall-lost",
          "developer_name": "OVERALL_LOST",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200808,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 143,
        "value": 5,
        "type": {
          "id": 143,
          "name": "Away Draw",
          "code": "away-draw",
          "developer_name": "AWAY_DRAWS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200809,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 144,
        "value": 8,
        "type": {
          "id": 144,
          "name": "Away Lost",
          "code": "away-lost",
          "developer_name": "AWAY_LOST",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200810,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 186,
        "value": 23,
        "type": {
          "id": 186,
          "name": "Away Points",
          "code": "away-points",
          "developer_name": "AWAY_POINTS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200811,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 145,
        "value": 23,
        "type": {
          "id": 145,
          "name": "Away Goals Scored",
          "code": "away-scored",
          "developer_name": "AWAY_SCORED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200812,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 146,
        "value": 28,
        "type": {
          "id": 146,
          "name": "Away Goals Conceded",
          "code": "away-conceded",
          "developer_name": "AWAY_CONCEDED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200813,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 179,
        "value": -16,
        "type": {
          "id": 179,
          "name": "Goal Difference",
          "code": "goal-difference",
          "developer_name": "OVERALL_GOAL_DIFFERENCE",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200792,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 133,
        "value": 46,
        "type": {
          "id": 133,
          "name": "Overal Goals Scored",
          "code": "overall-goals-for",
          "developer_name": "OVERALL_SCORED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200793,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 134,
        "value": 62,
        "type": {
          "id": 134,
          "name": "Overall Goals Conceded",
          "code": "overall-goals-against",
          "developer_name": "OVERALL_CONCEDED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200794,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 129,
        "value": 38,
        "type": {
          "id": 129,
          "name": "Overall Matches Played",
          "code": "overall-matches-played",
          "developer_name": "OVERALL_MATCHES",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200795,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 130,
        "value": 11,
        "type": {
          "id": 130,
          "name": "Overall Won",
          "code": "overall-won",
          "developer_name": "OVERALL_WINS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200796,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 131,
        "value": 10,
        "type": {
          "id": 131,
          "name": "Overall Draw",
          "code": "overall-draw",
          "developer_name": "OVERALL_DRAWS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200805,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 187,
        "value": 43,
        "type": {
          "id": 187,
          "name": "Overall Points",
          "code": "overall-points",
          "developer_name": "TOTAL_POINTS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200806,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 141,
        "value": 19,
        "type": {
          "id": 141,
          "name": "Away Matched Played",
          "code": "away-matches-played",
          "developer_name": "AWAY_MATCHES",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200804,
        "standing_type": "standing",
        "standing_id": 229333,
        "type_id": 140,
        "value": 34,
        "type": {
          "id": 140,
          "name": "Home Goals Conceded",
          "code": "home-conceded",
          "developer_name": "HOME_CONCEDED",
          "model_type": "standings",
          "stat_group": "home"
        }
      }
    ],
    "form": [
      {
        "id": 2203404390,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134459,
        "form": "L",
        "sort_order": 1
      },
      {
        "id": 2217305290,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134466,
        "form": "W",
        "sort_order": 2
      },
      {
        "id": 2231484473,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134482,
        "form": "L",
        "sort_order": 3
      },
      {
        "id": 2270489063,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134492,
        "form": "L",
        "sort_order": 5
      },
      {
        "id": 2287564307,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134495,
        "form": "D",
        "sort_order": 6
      },
      {
        "id": 2302736985,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134512,
        "form": "W",
        "sort_order": 7
      },
      {
        "id": 2329162298,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134521,
        "form": "L",
        "sort_order": 8
      },
      {
        "id": 2350897380,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134532,
        "form": "W",
        "sort_order": 9
      },
      {
        "id": 2380290413,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134541,
        "form": "D",
        "sort_order": 11
      },
      {
        "id": 2454276755,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134552,
        "form": "W",
        "sort_order": 15
      },
      {
        "id": 2573555903,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134559,
        "form": "W",
        "sort_order": 21
      },
      {
        "id": 2887738352,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134566,
        "form": "L",
        "sort_order": 24
      },
      {
        "id": 3092013409,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134582,
        "form": "L",
        "sort_order": 25
      },
      {
        "id": 3237639448,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134584,
        "form": "W",
        "sort_order": 26
      },
      {
        "id": 2417214156,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134601,
        "form": "W",
        "sort_order": 12
      },
      {
        "id": 2428599570,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134611,
        "form": "L",
        "sort_order": 13
      },
      {
        "id": 2616447147,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134622,
        "form": "L",
        "sort_order": 22
      },
      {
        "id": 2256383728,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134627,
        "form": "D",
        "sort_order": 4
      },
      {
        "id": 2470017335,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134633,
        "form": "D",
        "sort_order": 16
      },
      {
        "id": 2765658601,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134644,
        "form": "D",
        "sort_order": 23
      },
      {
        "id": 2361994356,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134875,
        "form": "L",
        "sort_order": 10
      },
      {
        "id": 2437349697,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134885,
        "form": "L",
        "sort_order": 14
      },
      {
        "id": 2478999133,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134898,
        "form": "D",
        "sort_order": 17
      },
      {
        "id": 2487385440,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134907,
        "form": "W",
        "sort_order": 18
      },
      {
        "id": 2491568517,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134918,
        "form": "L",
        "sort_order": 19
      },
      {
        "id": 2497546490,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134925,
        "form": "L",
        "sort_order": 20
      },
      {
        "id": 3330293775,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134933,
        "form": "W",
        "sort_order": 27
      },
      {
        "id": 3660898351,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134947,
        "form": "L",
        "sort_order": 28
      },
      {
        "id": 3772409060,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134952,
        "form": "D",
        "sort_order": 29
      },
      {
        "id": 4211882425,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134963,
        "form": "L",
        "sort_order": 30
      },
      {
        "id": 4317110855,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134978,
        "form": "D",
        "sort_order": 31
      },
      {
        "id": 4613720821,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134983,
        "form": "L",
        "sort_order": 32
      },
      {
        "id": 4770517628,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19134998,
        "form": "D",
        "sort_order": 33
      },
      {
        "id": 4944298696,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19135001,
        "form": "L",
        "sort_order": 34
      },
      {
        "id": 5169703903,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19135018,
        "form": "D",
        "sort_order": 35
      },
      {
        "id": 5329996301,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19135023,
        "form": "W",
        "sort_order": 36
      },
      {
        "id": 5488635722,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19135038,
        "form": "L",
        "sort_order": 37
      },
      {
        "id": 5619792267,
        "standing_type": "standing",
        "standing_id": 229333,
        "fixture_id": 19135041,
        "form": "W",
        "sort_order": 38
      }
    ],
    "stage": {
      "id": 77471288,
      "sport_id": 1,
      "league_id": 8,
      "season_id": 23614,
      "type_id": 223,
      "name": "Regular Season",
      "sort_order": 1,
      "finished": true,
      "is_current": false,
      "starting_at": "2024-08-16",
      "ending_at": "2025-05-25",
      "games_in_current_week": false,
      "tie_breaker_rule_id": null
    },
    "league": {
      "id": 8,
      "sport_id": 1,
      "country_id": 462,
      "name": "Premier League",
      "active": true,
      "short_code": "UK PL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/leagues/8/8.png",
      "type": "league",
      "sub_type": "domestic",
      "last_played_at": "2025-05-25 15:00:00",
      "category": 1,
      "has_jerseys": false
    },
    "group": null
  },
  {
    "id": 229328,
    "participant_id": 14,
    "sport_id": 1,
    "league_id": 8,
    "season_id": 23614,
    "stage_id": 77471288,
    "group_id": null,
    "round_id": 339273,
    "standing_rule_id": null,
    "position": 15,
    "result": "up",
    "points": 42,
    "participant": {
      "id": 14,
      "sport_id": 1,
      "country_id": 462,
      "venue_id": 206,
      "gender": "male",
      "name": "Manchester United",
      "short_code": "MUN",
      "image_path": "https://cdn.sportmonks.com/images/soccer/teams/14/14.png",
      "founded": 1878,
      "type": "domestic",
      "placeholder": false,
      "last_played_at": "2025-05-30 12:00:00"
    },
    "rule": null,
    "details": [
      {
        "id": 3131200695,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 187,
        "value": 42,
        "type": {
          "id": 187,
          "name": "Overall Points",
          "code": "overall-points",
          "developer_name": "TOTAL_POINTS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200693,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 139,
        "value": 23,
        "type": {
          "id": 139,
          "name": "Home Goals Scored",
          "code": "home-scored",
          "developer_name": "HOME_SCORED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3417350881,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 7939,
        "value": 52,
        "type": {
          "id": 7939,
          "name": "Expected Points (xPTS)",
          "code": "expected-points",
          "developer_name": "EXPECTED_POINTS",
          "model_type": "statistic",
          "stat_group": "offensive"
        }
      },
      {
        "id": 3131200683,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 134,
        "value": 54,
        "type": {
          "id": 134,
          "name": "Overall Goals Conceded",
          "code": "overall-goals-against",
          "developer_name": "OVERALL_CONCEDED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200685,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 130,
        "value": 11,
        "type": {
          "id": 130,
          "name": "Overall Won",
          "code": "overall-won",
          "developer_name": "OVERALL_WINS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200689,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 136,
        "value": 7,
        "type": {
          "id": 136,
          "name": "Home Won",
          "code": "home-won",
          "developer_name": "HOME_WINS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200698,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 143,
        "value": 6,
        "type": {
          "id": 143,
          "name": "Away Draw",
          "code": "away-draw",
          "developer_name": "AWAY_DRAWS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200692,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 185,
        "value": 24,
        "type": {
          "id": 185,
          "name": "Home Points",
          "code": "home-points",
          "developer_name": "HOME_POINTS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200694,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 140,
        "value": 28,
        "type": {
          "id": 140,
          "name": "Home Goals Conceded",
          "code": "home-conceded",
          "developer_name": "HOME_CONCEDED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200697,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 142,
        "value": 4,
        "type": {
          "id": 142,
          "name": "Away Won",
          "code": "away-won",
          "developer_name": "AWAY_WINS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200690,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 137,
        "value": 3,
        "type": {
          "id": 137,
          "name": "Home Draw",
          "code": "home-draw",
          "developer_name": "HOME_DRAWS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200691,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 138,
        "value": 9,
        "type": {
          "id": 138,
          "name": "Home Lost",
          "code": "home-lost",
          "developer_name": "HOME_LOST",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200682,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 133,
        "value": 44,
        "type": {
          "id": 133,
          "name": "Overal Goals Scored",
          "code": "overall-goals-for",
          "developer_name": "OVERALL_SCORED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200700,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 186,
        "value": 18,
        "type": {
          "id": 186,
          "name": "Away Points",
          "code": "away-points",
          "developer_name": "AWAY_POINTS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200701,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 145,
        "value": 21,
        "type": {
          "id": 145,
          "name": "Away Goals Scored",
          "code": "away-scored",
          "developer_name": "AWAY_SCORED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200684,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 129,
        "value": 38,
        "type": {
          "id": 129,
          "name": "Overall Matches Played",
          "code": "overall-matches-played",
          "developer_name": "OVERALL_MATCHES",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200686,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 131,
        "value": 9,
        "type": {
          "id": 131,
          "name": "Overall Draw",
          "code": "overall-draw",
          "developer_name": "OVERALL_DRAWS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200687,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 132,
        "value": 18,
        "type": {
          "id": 132,
          "name": "Overall Lost",
          "code": "overall-lost",
          "developer_name": "OVERALL_LOST",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200688,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 135,
        "value": 19,
        "type": {
          "id": 135,
          "name": "Home Matched Played",
          "code": "home-matches-played",
          "developer_name": "HOME_MATCHES",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200696,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 141,
        "value": 19,
        "type": {
          "id": 141,
          "name": "Away Matched Played",
          "code": "away-matches-played",
          "developer_name": "AWAY_MATCHES",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200699,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 144,
        "value": 9,
        "type": {
          "id": 144,
          "name": "Away Lost",
          "code": "away-lost",
          "developer_name": "AWAY_LOST",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200702,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 146,
        "value": 26,
        "type": {
          "id": 146,
          "name": "Away Goals Conceded",
          "code": "away-conceded",
          "developer_name": "AWAY_CONCEDED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200703,
        "standing_type": "standing",
        "standing_id": 229328,
        "type_id": 179,
        "value": -10,
        "type": {
          "id": 179,
          "name": "Goal Difference",
          "code": "goal-difference",
          "developer_name": "OVERALL_GOAL_DIFFERENCE",
          "model_type": "standings",
          "stat_group": "overall"
        }
      }
    ],
    "form": [
      {
        "id": 2200759467,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134453,
        "form": "W",
        "sort_order": 1
      },
      {
        "id": 2216729210,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134465,
        "form": "L",
        "sort_order": 2
      },
      {
        "id": 2233648270,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134479,
        "form": "L",
        "sort_order": 3
      },
      {
        "id": 2271897242,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134485,
        "form": "D",
        "sort_order": 5
      },
      {
        "id": 2291726640,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134499,
        "form": "L",
        "sort_order": 6
      },
      {
        "id": 2307140660,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134504,
        "form": "D",
        "sort_order": 7
      },
      {
        "id": 2330386230,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134517,
        "form": "W",
        "sort_order": 8
      },
      {
        "id": 2350897416,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134532,
        "form": "L",
        "sort_order": 9
      },
      {
        "id": 2384851904,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134538,
        "form": "W",
        "sort_order": 11
      },
      {
        "id": 2447805646,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134550,
        "form": "L",
        "sort_order": 15
      },
      {
        "id": 2582318269,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134562,
        "form": "W",
        "sort_order": 21
      },
      {
        "id": 2871518073,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134569,
        "form": "L",
        "sort_order": 24
      },
      {
        "id": 3148661991,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134581,
        "form": "L",
        "sort_order": 25
      },
      {
        "id": 3211579697,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134586,
        "form": "D",
        "sort_order": 26
      },
      {
        "id": 2415152617,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134598,
        "form": "D",
        "sort_order": 12
      },
      {
        "id": 2432365065,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134608,
        "form": "W",
        "sort_order": 13
      },
      {
        "id": 2652413019,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134619,
        "form": "L",
        "sort_order": 22
      },
      {
        "id": 2255567261,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134630,
        "form": "W",
        "sort_order": 4
      },
      {
        "id": 2468781005,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134638,
        "form": "W",
        "sort_order": 16
      },
      {
        "id": 2767239287,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134647,
        "form": "W",
        "sort_order": 23
      },
      {
        "id": 2367143836,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134873,
        "form": "D",
        "sort_order": 10
      },
      {
        "id": 2438991852,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134880,
        "form": "L",
        "sort_order": 14
      },
      {
        "id": 2482007284,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134896,
        "form": "L",
        "sort_order": 17
      },
      {
        "id": 2487554168,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134908,
        "form": "L",
        "sort_order": 18
      },
      {
        "id": 2492370617,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134916,
        "form": "L",
        "sort_order": 19
      },
      {
        "id": 2499949333,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134924,
        "form": "D",
        "sort_order": 20
      },
      {
        "id": 3322518238,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134938,
        "form": "W",
        "sort_order": 27
      },
      {
        "id": 3647993177,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134944,
        "form": "D",
        "sort_order": 28
      },
      {
        "id": 3848909822,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134955,
        "form": "W",
        "sort_order": 29
      },
      {
        "id": 4212594648,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134962,
        "form": "L",
        "sort_order": 30
      },
      {
        "id": 4402571685,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134976,
        "form": "D",
        "sort_order": 31
      },
      {
        "id": 4630191629,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134985,
        "form": "L",
        "sort_order": 32
      },
      {
        "id": 4807288606,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134996,
        "form": "L",
        "sort_order": 33
      },
      {
        "id": 4994035597,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19134999,
        "form": "D",
        "sort_order": 34
      },
      {
        "id": 5170320444,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19135011,
        "form": "L",
        "sort_order": 35
      },
      {
        "id": 5329996365,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19135023,
        "form": "L",
        "sort_order": 36
      },
      {
        "id": 5394882172,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19135033,
        "form": "L",
        "sort_order": 37
      },
      {
        "id": 5620027058,
        "standing_type": "standing",
        "standing_id": 229328,
        "fixture_id": 19135043,
        "form": "W",
        "sort_order": 38
      }
    ],
    "stage": {
      "id": 77471288,
      "sport_id": 1,
      "league_id": 8,
      "season_id": 23614,
      "type_id": 223,
      "name": "Regular Season",
      "sort_order": 1,
      "finished": true,
      "is_current": false,
      "starting_at": "2024-08-16",
      "ending_at": "2025-05-25",
      "games_in_current_week": false,
      "tie_breaker_rule_id": null
    },
    "league": {
      "id": 8,
      "sport_id": 1,
      "country_id": 462,
      "name": "Premier League",
      "active": true,
      "short_code": "UK PL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/leagues/8/8.png",
      "type": "league",
      "sub_type": "domestic",
      "last_played_at": "2025-05-25 15:00:00",
      "category": 1,
      "has_jerseys": false
    },
    "group": null
  },
  {
    "id": 229334,
    "participant_id": 29,
    "sport_id": 1,
    "league_id": 8,
    "season_id": 23614,
    "stage_id": 77471288,
    "group_id": null,
    "round_id": 339273,
    "standing_rule_id": null,
    "position": 16,
    "result": "down",
    "points": 42,
    "participant": {
      "id": 29,
      "sport_id": 1,
      "country_id": 462,
      "venue_id": 492,
      "gender": "male",
      "name": "Wolverhampton Wanderers",
      "short_code": "WOL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/teams/29/29.png",
      "founded": 1877,
      "type": "domestic",
      "placeholder": false,
      "last_played_at": "2025-05-25 15:00:00"
    },
    "rule": null,
    "details": [
      {
        "id": 3423872197,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 7939,
        "value": 43,
        "type": {
          "id": 7939,
          "name": "Expected Points (xPTS)",
          "code": "expected-points",
          "developer_name": "EXPECTED_POINTS",
          "model_type": "statistic",
          "stat_group": "offensive"
        }
      },
      {
        "id": 3131200825,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 139,
        "value": 27,
        "type": {
          "id": 139,
          "name": "Home Goals Scored",
          "code": "home-scored",
          "developer_name": "HOME_SCORED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200828,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 141,
        "value": 19,
        "type": {
          "id": 141,
          "name": "Away Matched Played",
          "code": "away-matches-played",
          "developer_name": "AWAY_MATCHES",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200829,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 142,
        "value": 6,
        "type": {
          "id": 142,
          "name": "Away Won",
          "code": "away-won",
          "developer_name": "AWAY_WINS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200835,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 179,
        "value": -15,
        "type": {
          "id": 179,
          "name": "Goal Difference",
          "code": "goal-difference",
          "developer_name": "OVERALL_GOAL_DIFFERENCE",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200834,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 146,
        "value": 37,
        "type": {
          "id": 146,
          "name": "Away Goals Conceded",
          "code": "away-conceded",
          "developer_name": "AWAY_CONCEDED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200814,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 133,
        "value": 54,
        "type": {
          "id": 133,
          "name": "Overal Goals Scored",
          "code": "overall-goals-for",
          "developer_name": "OVERALL_SCORED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200815,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 134,
        "value": 69,
        "type": {
          "id": 134,
          "name": "Overall Goals Conceded",
          "code": "overall-goals-against",
          "developer_name": "OVERALL_CONCEDED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200826,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 140,
        "value": 32,
        "type": {
          "id": 140,
          "name": "Home Goals Conceded",
          "code": "home-conceded",
          "developer_name": "HOME_CONCEDED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200827,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 187,
        "value": 42,
        "type": {
          "id": 187,
          "name": "Overall Points",
          "code": "overall-points",
          "developer_name": "TOTAL_POINTS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200830,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 143,
        "value": 3,
        "type": {
          "id": 143,
          "name": "Away Draw",
          "code": "away-draw",
          "developer_name": "AWAY_DRAWS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200831,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 144,
        "value": 10,
        "type": {
          "id": 144,
          "name": "Away Lost",
          "code": "away-lost",
          "developer_name": "AWAY_LOST",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200817,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 130,
        "value": 12,
        "type": {
          "id": 130,
          "name": "Overall Won",
          "code": "overall-won",
          "developer_name": "OVERALL_WINS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200818,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 131,
        "value": 6,
        "type": {
          "id": 131,
          "name": "Overall Draw",
          "code": "overall-draw",
          "developer_name": "OVERALL_DRAWS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200823,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 138,
        "value": 10,
        "type": {
          "id": 138,
          "name": "Home Lost",
          "code": "home-lost",
          "developer_name": "HOME_LOST",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200819,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 132,
        "value": 20,
        "type": {
          "id": 132,
          "name": "Overall Lost",
          "code": "overall-lost",
          "developer_name": "OVERALL_LOST",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200820,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 135,
        "value": 19,
        "type": {
          "id": 135,
          "name": "Home Matched Played",
          "code": "home-matches-played",
          "developer_name": "HOME_MATCHES",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200824,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 185,
        "value": 21,
        "type": {
          "id": 185,
          "name": "Home Points",
          "code": "home-points",
          "developer_name": "HOME_POINTS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200821,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 136,
        "value": 6,
        "type": {
          "id": 136,
          "name": "Home Won",
          "code": "home-won",
          "developer_name": "HOME_WINS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200822,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 137,
        "value": 3,
        "type": {
          "id": 137,
          "name": "Home Draw",
          "code": "home-draw",
          "developer_name": "HOME_DRAWS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200832,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 186,
        "value": 21,
        "type": {
          "id": 186,
          "name": "Away Points",
          "code": "away-points",
          "developer_name": "AWAY_POINTS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200833,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 145,
        "value": 27,
        "type": {
          "id": 145,
          "name": "Away Goals Scored",
          "code": "away-scored",
          "developer_name": "AWAY_SCORED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200816,
        "standing_type": "standing",
        "standing_id": 229334,
        "type_id": 129,
        "value": 38,
        "type": {
          "id": 129,
          "name": "Overall Matches Played",
          "code": "overall-matches-played",
          "developer_name": "OVERALL_MATCHES",
          "model_type": "standings",
          "stat_group": "overall"
        }
      }
    ],
    "form": [
      {
        "id": 2203040242,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134455,
        "form": "L",
        "sort_order": 1
      },
      {
        "id": 2219847954,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134472,
        "form": "L",
        "sort_order": 2
      },
      {
        "id": 2231136127,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134481,
        "form": "D",
        "sort_order": 3
      },
      {
        "id": 2271549992,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134483,
        "form": "L",
        "sort_order": 5
      },
      {
        "id": 2288076427,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134502,
        "form": "L",
        "sort_order": 6
      },
      {
        "id": 2302737138,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134505,
        "form": "L",
        "sort_order": 7
      },
      {
        "id": 2334859157,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134522,
        "form": "L",
        "sort_order": 8
      },
      {
        "id": 2346793561,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134526,
        "form": "D",
        "sort_order": 9
      },
      {
        "id": 2380376091,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134542,
        "form": "W",
        "sort_order": 11
      },
      {
        "id": 2454276829,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134552,
        "form": "L",
        "sort_order": 15
      },
      {
        "id": 2580176594,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134561,
        "form": "L",
        "sort_order": 21
      },
      {
        "id": 2840806755,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134572,
        "form": "W",
        "sort_order": 24
      },
      {
        "id": 3139698357,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134578,
        "form": "L",
        "sort_order": 25
      },
      {
        "id": 3237537516,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134583,
        "form": "W",
        "sort_order": 26
      },
      {
        "id": 2410185543,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134597,
        "form": "W",
        "sort_order": 12
      },
      {
        "id": 2427909266,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134612,
        "form": "L",
        "sort_order": 13
      },
      {
        "id": 2663045447,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134615,
        "form": "L",
        "sort_order": 22
      },
      {
        "id": 2259242944,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134632,
        "form": "L",
        "sort_order": 4
      },
      {
        "id": 2463548979,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134642,
        "form": "L",
        "sort_order": 16
      },
      {
        "id": 2721178857,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134652,
        "form": "L",
        "sort_order": 23
      },
      {
        "id": 2362550348,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134878,
        "form": "D",
        "sort_order": 10
      },
      {
        "id": 2438823379,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134882,
        "form": "L",
        "sort_order": 14
      },
      {
        "id": 2481996798,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134895,
        "form": "W",
        "sort_order": 17
      },
      {
        "id": 2487554221,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134908,
        "form": "W",
        "sort_order": 18
      },
      {
        "id": 2491509938,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134917,
        "form": "D",
        "sort_order": 19
      },
      {
        "id": 2501390047,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134928,
        "form": "L",
        "sort_order": 20
      },
      {
        "id": 3313369498,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134934,
        "form": "L",
        "sort_order": 27
      },
      {
        "id": 3591246528,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134948,
        "form": "D",
        "sort_order": 28
      },
      {
        "id": 3772409089,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134958,
        "form": "W",
        "sort_order": 29
      },
      {
        "id": 4211882495,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134963,
        "form": "W",
        "sort_order": 30
      },
      {
        "id": 4317111004,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134974,
        "form": "W",
        "sort_order": 31
      },
      {
        "id": 4613720757,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134988,
        "form": "W",
        "sort_order": 32
      },
      {
        "id": 4807288671,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19134996,
        "form": "W",
        "sort_order": 33
      },
      {
        "id": 4945039510,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19135008,
        "form": "W",
        "sort_order": 34
      },
      {
        "id": 5075393079,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19135017,
        "form": "L",
        "sort_order": 35
      },
      {
        "id": 5284812378,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19135028,
        "form": "L",
        "sort_order": 36
      },
      {
        "id": 5516111834,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19135034,
        "form": "L",
        "sort_order": 37
      },
      {
        "id": 5619544172,
        "standing_type": "standing",
        "standing_id": 229334,
        "fixture_id": 19135048,
        "form": "D",
        "sort_order": 38
      }
    ],
    "stage": {
      "id": 77471288,
      "sport_id": 1,
      "league_id": 8,
      "season_id": 23614,
      "type_id": 223,
      "name": "Regular Season",
      "sort_order": 1,
      "finished": true,
      "is_current": false,
      "starting_at": "2024-08-16",
      "ending_at": "2025-05-25",
      "games_in_current_week": false,
      "tie_breaker_rule_id": null
    },
    "league": {
      "id": 8,
      "sport_id": 1,
      "country_id": 462,
      "name": "Premier League",
      "active": true,
      "short_code": "UK PL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/leagues/8/8.png",
      "type": "league",
      "sub_type": "domestic",
      "last_played_at": "2025-05-25 15:00:00",
      "category": 1,
      "has_jerseys": false
    },
    "group": null
  },
  {
    "id": 229332,
    "participant_id": 6,
    "sport_id": 1,
    "league_id": 8,
    "season_id": 23614,
    "stage_id": 77471288,
    "group_id": null,
    "round_id": 339273,
    "standing_rule_id": null,
    "position": 17,
    "result": "equal",
    "points": 38,
    "participant": {
      "id": 6,
      "sport_id": 1,
      "country_id": 462,
      "venue_id": 281313,
      "gender": "male",
      "name": "Tottenham Hotspur",
      "short_code": "TOT",
      "image_path": "https://cdn.sportmonks.com/images/soccer/teams/6/6.png",
      "founded": 1882,
      "type": "domestic",
      "placeholder": false,
      "last_played_at": "2025-05-25 15:00:00"
    },
    "rule": null,
    "details": [
      {
        "id": 3441815626,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 7939,
        "value": 51,
        "type": {
          "id": 7939,
          "name": "Expected Points (xPTS)",
          "code": "expected-points",
          "developer_name": "EXPECTED_POINTS",
          "model_type": "statistic",
          "stat_group": "offensive"
        }
      },
      {
        "id": 3131200791,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 179,
        "value": -1,
        "type": {
          "id": 179,
          "name": "Goal Difference",
          "code": "goal-difference",
          "developer_name": "OVERALL_GOAL_DIFFERENCE",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200776,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 135,
        "value": 19,
        "type": {
          "id": 135,
          "name": "Home Matched Played",
          "code": "home-matches-played",
          "developer_name": "HOME_MATCHES",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200788,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 186,
        "value": 17,
        "type": {
          "id": 186,
          "name": "Away Points",
          "code": "away-points",
          "developer_name": "AWAY_POINTS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200789,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 145,
        "value": 29,
        "type": {
          "id": 145,
          "name": "Away Goals Scored",
          "code": "away-scored",
          "developer_name": "AWAY_SCORED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200772,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 129,
        "value": 38,
        "type": {
          "id": 129,
          "name": "Overall Matches Played",
          "code": "overall-matches-played",
          "developer_name": "OVERALL_MATCHES",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200778,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 137,
        "value": 3,
        "type": {
          "id": 137,
          "name": "Home Draw",
          "code": "home-draw",
          "developer_name": "HOME_DRAWS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200781,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 139,
        "value": 35,
        "type": {
          "id": 139,
          "name": "Home Goals Scored",
          "code": "home-scored",
          "developer_name": "HOME_SCORED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200782,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 140,
        "value": 35,
        "type": {
          "id": 140,
          "name": "Home Goals Conceded",
          "code": "home-conceded",
          "developer_name": "HOME_CONCEDED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200785,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 142,
        "value": 5,
        "type": {
          "id": 142,
          "name": "Away Won",
          "code": "away-won",
          "developer_name": "AWAY_WINS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200790,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 146,
        "value": 30,
        "type": {
          "id": 146,
          "name": "Away Goals Conceded",
          "code": "away-conceded",
          "developer_name": "AWAY_CONCEDED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200770,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 133,
        "value": 64,
        "type": {
          "id": 133,
          "name": "Overal Goals Scored",
          "code": "overall-goals-for",
          "developer_name": "OVERALL_SCORED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200771,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 134,
        "value": 65,
        "type": {
          "id": 134,
          "name": "Overall Goals Conceded",
          "code": "overall-goals-against",
          "developer_name": "OVERALL_CONCEDED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200773,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 130,
        "value": 11,
        "type": {
          "id": 130,
          "name": "Overall Won",
          "code": "overall-won",
          "developer_name": "OVERALL_WINS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200774,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 131,
        "value": 5,
        "type": {
          "id": 131,
          "name": "Overall Draw",
          "code": "overall-draw",
          "developer_name": "OVERALL_DRAWS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200775,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 132,
        "value": 22,
        "type": {
          "id": 132,
          "name": "Overall Lost",
          "code": "overall-lost",
          "developer_name": "OVERALL_LOST",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200777,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 136,
        "value": 6,
        "type": {
          "id": 136,
          "name": "Home Won",
          "code": "home-won",
          "developer_name": "HOME_WINS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200779,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 138,
        "value": 10,
        "type": {
          "id": 138,
          "name": "Home Lost",
          "code": "home-lost",
          "developer_name": "HOME_LOST",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200780,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 185,
        "value": 21,
        "type": {
          "id": 185,
          "name": "Home Points",
          "code": "home-points",
          "developer_name": "HOME_POINTS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200783,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 187,
        "value": 38,
        "type": {
          "id": 187,
          "name": "Overall Points",
          "code": "overall-points",
          "developer_name": "TOTAL_POINTS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200784,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 141,
        "value": 19,
        "type": {
          "id": 141,
          "name": "Away Matched Played",
          "code": "away-matches-played",
          "developer_name": "AWAY_MATCHES",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200786,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 143,
        "value": 2,
        "type": {
          "id": 143,
          "name": "Away Draw",
          "code": "away-draw",
          "developer_name": "AWAY_DRAWS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200787,
        "standing_type": "standing",
        "standing_id": 229332,
        "type_id": 144,
        "value": 12,
        "type": {
          "id": 144,
          "name": "Away Lost",
          "code": "away-lost",
          "developer_name": "AWAY_LOST",
          "model_type": "standings",
          "stat_group": "away"
        }
      }
    ],
    "form": [
      {
        "id": 2208207707,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134462,
        "form": "D",
        "sort_order": 1
      },
      {
        "id": 2217304882,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134471,
        "form": "W",
        "sort_order": 2
      },
      {
        "id": 2233280579,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134480,
        "form": "L",
        "sort_order": 3
      },
      {
        "id": 2271344804,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134491,
        "form": "W",
        "sort_order": 5
      },
      {
        "id": 2291726616,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134499,
        "form": "W",
        "sort_order": 6
      },
      {
        "id": 2307637585,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134506,
        "form": "L",
        "sort_order": 7
      },
      {
        "id": 2329162082,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134521,
        "form": "W",
        "sort_order": 8
      },
      {
        "id": 2350884304,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134528,
        "form": "L",
        "sort_order": 9
      },
      {
        "id": 2384881186,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134540,
        "form": "L",
        "sort_order": 11
      },
      {
        "id": 2452140259,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134551,
        "form": "L",
        "sort_order": 15
      },
      {
        "id": 2580402866,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134553,
        "form": "L",
        "sort_order": 21
      },
      {
        "id": 2871423678,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134565,
        "form": "W",
        "sort_order": 24
      },
      {
        "id": 3148661916,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134581,
        "form": "W",
        "sort_order": 25
      },
      {
        "id": 3237862525,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134588,
        "form": "W",
        "sort_order": 26
      },
      {
        "id": 2410717313,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134600,
        "form": "W",
        "sort_order": 12
      },
      {
        "id": 2432455192,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134610,
        "form": "D",
        "sort_order": 13
      },
      {
        "id": 2652519053,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134616,
        "form": "L",
        "sort_order": 22
      },
      {
        "id": 2258904048,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134631,
        "form": "L",
        "sort_order": 4
      },
      {
        "id": 2468878680,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134641,
        "form": "W",
        "sort_order": 16
      },
      {
        "id": 2758039012,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134651,
        "form": "L",
        "sort_order": 23
      },
      {
        "id": 2366627704,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134877,
        "form": "W",
        "sort_order": 10
      },
      {
        "id": 2440274262,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134879,
        "form": "L",
        "sort_order": 14
      },
      {
        "id": 2482416017,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134897,
        "form": "L",
        "sort_order": 17
      },
      {
        "id": 2487107051,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134906,
        "form": "L",
        "sort_order": 18
      },
      {
        "id": 2491509828,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134917,
        "form": "D",
        "sort_order": 19
      },
      {
        "id": 2496950217,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134927,
        "form": "L",
        "sort_order": 20
      },
      {
        "id": 3322506098,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134932,
        "form": "L",
        "sort_order": 27
      },
      {
        "id": 3637171886,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134946,
        "form": "D",
        "sort_order": 28
      },
      {
        "id": 3829544994,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134953,
        "form": "L",
        "sort_order": 29
      },
      {
        "id": 4231490377,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134964,
        "form": "L",
        "sort_order": 30
      },
      {
        "id": 4386463860,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134977,
        "form": "W",
        "sort_order": 31
      },
      {
        "id": 4613720694,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134988,
        "form": "L",
        "sort_order": 32
      },
      {
        "id": 4854153219,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19134997,
        "form": "L",
        "sort_order": 33
      },
      {
        "id": 5004791663,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19135003,
        "form": "L",
        "sort_order": 34
      },
      {
        "id": 5169703868,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19135018,
        "form": "D",
        "sort_order": 35
      },
      {
        "id": 5329996565,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19135027,
        "form": "L",
        "sort_order": 36
      },
      {
        "id": 5394590895,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19135030,
        "form": "L",
        "sort_order": 37
      },
      {
        "id": 5619636689,
        "standing_type": "standing",
        "standing_id": 229332,
        "fixture_id": 19135047,
        "form": "L",
        "sort_order": 38
      }
    ],
    "stage": {
      "id": 77471288,
      "sport_id": 1,
      "league_id": 8,
      "season_id": 23614,
      "type_id": 223,
      "name": "Regular Season",
      "sort_order": 1,
      "finished": true,
      "is_current": false,
      "starting_at": "2024-08-16",
      "ending_at": "2025-05-25",
      "games_in_current_week": false,
      "tie_breaker_rule_id": null
    },
    "league": {
      "id": 8,
      "sport_id": 1,
      "country_id": 462,
      "name": "Premier League",
      "active": true,
      "short_code": "UK PL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/leagues/8/8.png",
      "type": "league",
      "sub_type": "domestic",
      "last_played_at": "2025-05-25 15:00:00",
      "category": 1,
      "has_jerseys": false
    },
    "group": null
  },
  {
    "id": 229325,
    "participant_id": 42,
    "sport_id": 1,
    "league_id": 8,
    "season_id": 23614,
    "stage_id": 77471288,
    "group_id": null,
    "round_id": 339273,
    "standing_rule_id": 117810,
    "position": 18,
    "result": "equal",
    "points": 25,
    "participant": {
      "id": 42,
      "sport_id": 1,
      "country_id": 462,
      "venue_id": 117,
      "gender": "male",
      "name": "Leicester City",
      "short_code": "LEI",
      "image_path": "https://cdn.sportmonks.com/images/soccer/teams/10/42.png",
      "founded": 1884,
      "type": "domestic",
      "placeholder": false,
      "last_played_at": "2025-05-25 15:00:00"
    },
    "rule": {
      "id": 117810,
      "model_type": "stage",
      "model_id": 77471288,
      "type_id": 182,
      "position": 18,
      "type": {
        "id": 182,
        "name": "Relegation",
        "code": "relegation",
        "developer_name": "RELEGATION",
        "model_type": "standing_rule",
        "stat_group": null
      }
    },
    "details": [
      {
        "id": 3131200616,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 133,
        "value": 33,
        "type": {
          "id": 133,
          "name": "Overal Goals Scored",
          "code": "overall-goals-for",
          "developer_name": "OVERALL_SCORED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200636,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 146,
        "value": 46,
        "type": {
          "id": 146,
          "name": "Away Goals Conceded",
          "code": "away-conceded",
          "developer_name": "AWAY_CONCEDED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200618,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 129,
        "value": 38,
        "type": {
          "id": 129,
          "name": "Overall Matches Played",
          "code": "overall-matches-played",
          "developer_name": "OVERALL_MATCHES",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200623,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 136,
        "value": 4,
        "type": {
          "id": 136,
          "name": "Home Won",
          "code": "home-won",
          "developer_name": "HOME_WINS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3441815627,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 7939,
        "value": 29,
        "type": {
          "id": 7939,
          "name": "Expected Points (xPTS)",
          "code": "expected-points",
          "developer_name": "EXPECTED_POINTS",
          "model_type": "statistic",
          "stat_group": "offensive"
        }
      },
      {
        "id": 3131200620,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 131,
        "value": 7,
        "type": {
          "id": 131,
          "name": "Overall Draw",
          "code": "overall-draw",
          "developer_name": "OVERALL_DRAWS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200617,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 134,
        "value": 80,
        "type": {
          "id": 134,
          "name": "Overall Goals Conceded",
          "code": "overall-goals-against",
          "developer_name": "OVERALL_CONCEDED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200637,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 179,
        "value": -47,
        "type": {
          "id": 179,
          "name": "Goal Difference",
          "code": "goal-difference",
          "developer_name": "OVERALL_GOAL_DIFFERENCE",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200621,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 132,
        "value": 25,
        "type": {
          "id": 132,
          "name": "Overall Lost",
          "code": "overall-lost",
          "developer_name": "OVERALL_LOST",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200619,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 130,
        "value": 6,
        "type": {
          "id": 130,
          "name": "Overall Won",
          "code": "overall-won",
          "developer_name": "OVERALL_WINS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200622,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 135,
        "value": 19,
        "type": {
          "id": 135,
          "name": "Home Matched Played",
          "code": "home-matches-played",
          "developer_name": "HOME_MATCHES",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200635,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 145,
        "value": 18,
        "type": {
          "id": 145,
          "name": "Away Goals Scored",
          "code": "away-scored",
          "developer_name": "AWAY_SCORED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200629,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 187,
        "value": 25,
        "type": {
          "id": 187,
          "name": "Overall Points",
          "code": "overall-points",
          "developer_name": "TOTAL_POINTS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200631,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 142,
        "value": 2,
        "type": {
          "id": 142,
          "name": "Away Won",
          "code": "away-won",
          "developer_name": "AWAY_WINS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200634,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 186,
        "value": 10,
        "type": {
          "id": 186,
          "name": "Away Points",
          "code": "away-points",
          "developer_name": "AWAY_POINTS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200628,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 140,
        "value": 34,
        "type": {
          "id": 140,
          "name": "Home Goals Conceded",
          "code": "home-conceded",
          "developer_name": "HOME_CONCEDED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200624,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 137,
        "value": 3,
        "type": {
          "id": 137,
          "name": "Home Draw",
          "code": "home-draw",
          "developer_name": "HOME_DRAWS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200625,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 138,
        "value": 12,
        "type": {
          "id": 138,
          "name": "Home Lost",
          "code": "home-lost",
          "developer_name": "HOME_LOST",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200626,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 185,
        "value": 15,
        "type": {
          "id": 185,
          "name": "Home Points",
          "code": "home-points",
          "developer_name": "HOME_POINTS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200627,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 139,
        "value": 15,
        "type": {
          "id": 139,
          "name": "Home Goals Scored",
          "code": "home-scored",
          "developer_name": "HOME_SCORED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200630,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 141,
        "value": 19,
        "type": {
          "id": 141,
          "name": "Away Matched Played",
          "code": "away-matches-played",
          "developer_name": "AWAY_MATCHES",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200632,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 143,
        "value": 4,
        "type": {
          "id": 143,
          "name": "Away Draw",
          "code": "away-draw",
          "developer_name": "AWAY_DRAWS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200633,
        "standing_type": "standing",
        "standing_id": 229325,
        "type_id": 144,
        "value": 13,
        "type": {
          "id": 144,
          "name": "Away Lost",
          "code": "away-lost",
          "developer_name": "AWAY_LOST",
          "model_type": "standings",
          "stat_group": "away"
        }
      }
    ],
    "form": [
      {
        "id": 2208207708,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134462,
        "form": "D",
        "sort_order": 1
      },
      {
        "id": 2217305382,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134467,
        "form": "L",
        "sort_order": 2
      },
      {
        "id": 2231106683,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134478,
        "form": "L",
        "sort_order": 3
      },
      {
        "id": 2271411919,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134487,
        "form": "D",
        "sort_order": 5
      },
      {
        "id": 2287651924,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134494,
        "form": "L",
        "sort_order": 6
      },
      {
        "id": 2302737066,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134510,
        "form": "W",
        "sort_order": 7
      },
      {
        "id": 2330386367,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134520,
        "form": "W",
        "sort_order": 8
      },
      {
        "id": 2343063715,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134530,
        "form": "L",
        "sort_order": 9
      },
      {
        "id": 2384852109,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134538,
        "form": "L",
        "sort_order": 11
      },
      {
        "id": 2451305349,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134549,
        "form": "D",
        "sort_order": 15
      },
      {
        "id": 2580128844,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134557,
        "form": "L",
        "sort_order": 21
      },
      {
        "id": 2832965157,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134567,
        "form": "L",
        "sort_order": 24
      },
      {
        "id": 3065958300,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134577,
        "form": "L",
        "sort_order": 25
      },
      {
        "id": 3196139319,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134589,
        "form": "L",
        "sort_order": 26
      },
      {
        "id": 2409033424,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134599,
        "form": "L",
        "sort_order": 12
      },
      {
        "id": 2427854025,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134603,
        "form": "L",
        "sort_order": 13
      },
      {
        "id": 2616447834,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134618,
        "form": "L",
        "sort_order": 22
      },
      {
        "id": 2256383785,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134626,
        "form": "D",
        "sort_order": 4
      },
      {
        "id": 2463548867,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134639,
        "form": "L",
        "sort_order": 16
      },
      {
        "id": 2758039249,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134651,
        "form": "W",
        "sort_order": 23
      },
      {
        "id": 2362092091,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134871,
        "form": "D",
        "sort_order": 10
      },
      {
        "id": 2437349711,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134885,
        "form": "W",
        "sort_order": 14
      },
      {
        "id": 2481996781,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134895,
        "form": "L",
        "sort_order": 17
      },
      {
        "id": 2487677135,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134903,
        "form": "L",
        "sort_order": 18
      },
      {
        "id": 2491342656,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134915,
        "form": "L",
        "sort_order": 19
      },
      {
        "id": 2497547139,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134920,
        "form": "L",
        "sort_order": 20
      },
      {
        "id": 3330293890,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134933,
        "form": "L",
        "sort_order": 27
      },
      {
        "id": 3637840878,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134941,
        "form": "L",
        "sort_order": 28
      },
      {
        "id": 3848910107,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134955,
        "form": "L",
        "sort_order": 29
      },
      {
        "id": 4226041140,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134965,
        "form": "L",
        "sort_order": 30
      },
      {
        "id": 4417548196,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134975,
        "form": "L",
        "sort_order": 31
      },
      {
        "id": 4541771370,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134981,
        "form": "D",
        "sort_order": 32
      },
      {
        "id": 4816057351,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19134995,
        "form": "L",
        "sort_order": 33
      },
      {
        "id": 4945039712,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19135008,
        "form": "L",
        "sort_order": 34
      },
      {
        "id": 5122300412,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19135016,
        "form": "W",
        "sort_order": 35
      },
      {
        "id": 5330073084,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19135025,
        "form": "D",
        "sort_order": 36
      },
      {
        "id": 5490389624,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19135036,
        "form": "W",
        "sort_order": 37
      },
      {
        "id": 5619544471,
        "standing_type": "standing",
        "standing_id": 229325,
        "fixture_id": 19135039,
        "form": "L",
        "sort_order": 38
      }
    ],
    "stage": {
      "id": 77471288,
      "sport_id": 1,
      "league_id": 8,
      "season_id": 23614,
      "type_id": 223,
      "name": "Regular Season",
      "sort_order": 1,
      "finished": true,
      "is_current": false,
      "starting_at": "2024-08-16",
      "ending_at": "2025-05-25",
      "games_in_current_week": false,
      "tie_breaker_rule_id": null
    },
    "league": {
      "id": 8,
      "sport_id": 1,
      "country_id": 462,
      "name": "Premier League",
      "active": true,
      "short_code": "UK PL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/leagues/8/8.png",
      "type": "league",
      "sub_type": "domestic",
      "last_played_at": "2025-05-25 15:00:00",
      "category": 1,
      "has_jerseys": false
    },
    "group": null
  },
  {
    "id": 229324,
    "participant_id": 116,
    "sport_id": 1,
    "league_id": 8,
    "season_id": 23614,
    "stage_id": 77471288,
    "group_id": null,
    "round_id": 339273,
    "standing_rule_id": 117811,
    "position": 19,
    "result": "equal",
    "points": 22,
    "participant": {
      "id": 116,
      "sport_id": 1,
      "country_id": 462,
      "venue_id": 504,
      "gender": "male",
      "name": "Ipswich Town",
      "short_code": "IPS",
      "image_path": "https://cdn.sportmonks.com/images/soccer/teams/20/116.png",
      "founded": 1878,
      "type": "domestic",
      "placeholder": false,
      "last_played_at": "2025-05-25 15:00:00"
    },
    "rule": {
      "id": 117811,
      "model_type": "stage",
      "model_id": 77471288,
      "type_id": 182,
      "position": 19,
      "type": {
        "id": 182,
        "name": "Relegation",
        "code": "relegation",
        "developer_name": "RELEGATION",
        "model_type": "standing_rule",
        "stat_group": null
      }
    },
    "details": [
      {
        "id": 3421579066,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 7939,
        "value": 31,
        "type": {
          "id": 7939,
          "name": "Expected Points (xPTS)",
          "code": "expected-points",
          "developer_name": "EXPECTED_POINTS",
          "model_type": "statistic",
          "stat_group": "offensive"
        }
      },
      {
        "id": 3131200605,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 139,
        "value": 14,
        "type": {
          "id": 139,
          "name": "Home Goals Scored",
          "code": "home-scored",
          "developer_name": "HOME_SCORED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200606,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 140,
        "value": 44,
        "type": {
          "id": 140,
          "name": "Home Goals Conceded",
          "code": "home-conceded",
          "developer_name": "HOME_CONCEDED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200615,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 179,
        "value": -46,
        "type": {
          "id": 179,
          "name": "Goal Difference",
          "code": "goal-difference",
          "developer_name": "OVERALL_GOAL_DIFFERENCE",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200608,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 141,
        "value": 19,
        "type": {
          "id": 141,
          "name": "Away Matched Played",
          "code": "away-matches-played",
          "developer_name": "AWAY_MATCHES",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200609,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 142,
        "value": 3,
        "type": {
          "id": 142,
          "name": "Away Won",
          "code": "away-won",
          "developer_name": "AWAY_WINS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200599,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 132,
        "value": 24,
        "type": {
          "id": 132,
          "name": "Overall Lost",
          "code": "overall-lost",
          "developer_name": "OVERALL_LOST",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200613,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 145,
        "value": 22,
        "type": {
          "id": 145,
          "name": "Away Goals Scored",
          "code": "away-scored",
          "developer_name": "AWAY_SCORED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200607,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 187,
        "value": 22,
        "type": {
          "id": 187,
          "name": "Overall Points",
          "code": "overall-points",
          "developer_name": "TOTAL_POINTS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200602,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 137,
        "value": 4,
        "type": {
          "id": 137,
          "name": "Home Draw",
          "code": "home-draw",
          "developer_name": "HOME_DRAWS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200603,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 138,
        "value": 14,
        "type": {
          "id": 138,
          "name": "Home Lost",
          "code": "home-lost",
          "developer_name": "HOME_LOST",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200594,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 133,
        "value": 36,
        "type": {
          "id": 133,
          "name": "Overal Goals Scored",
          "code": "overall-goals-for",
          "developer_name": "OVERALL_SCORED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200614,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 146,
        "value": 38,
        "type": {
          "id": 146,
          "name": "Away Goals Conceded",
          "code": "away-conceded",
          "developer_name": "AWAY_CONCEDED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200600,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 135,
        "value": 19,
        "type": {
          "id": 135,
          "name": "Home Matched Played",
          "code": "home-matches-played",
          "developer_name": "HOME_MATCHES",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200601,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 136,
        "value": 1,
        "type": {
          "id": 136,
          "name": "Home Won",
          "code": "home-won",
          "developer_name": "HOME_WINS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200604,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 185,
        "value": 7,
        "type": {
          "id": 185,
          "name": "Home Points",
          "code": "home-points",
          "developer_name": "HOME_POINTS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200610,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 143,
        "value": 6,
        "type": {
          "id": 143,
          "name": "Away Draw",
          "code": "away-draw",
          "developer_name": "AWAY_DRAWS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200611,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 144,
        "value": 10,
        "type": {
          "id": 144,
          "name": "Away Lost",
          "code": "away-lost",
          "developer_name": "AWAY_LOST",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200612,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 186,
        "value": 15,
        "type": {
          "id": 186,
          "name": "Away Points",
          "code": "away-points",
          "developer_name": "AWAY_POINTS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200595,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 134,
        "value": 82,
        "type": {
          "id": 134,
          "name": "Overall Goals Conceded",
          "code": "overall-goals-against",
          "developer_name": "OVERALL_CONCEDED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200596,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 129,
        "value": 38,
        "type": {
          "id": 129,
          "name": "Overall Matches Played",
          "code": "overall-matches-played",
          "developer_name": "OVERALL_MATCHES",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200597,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 130,
        "value": 4,
        "type": {
          "id": 130,
          "name": "Overall Won",
          "code": "overall-won",
          "developer_name": "OVERALL_WINS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200598,
        "standing_type": "standing",
        "standing_id": 229324,
        "type_id": 131,
        "value": 10,
        "type": {
          "id": 131,
          "name": "Overall Draw",
          "code": "overall-draw",
          "developer_name": "OVERALL_DRAWS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      }
    ],
    "form": [
      {
        "id": 2202480715,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134454,
        "form": "L",
        "sort_order": 1
      },
      {
        "id": 2217341403,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134469,
        "form": "L",
        "sort_order": 2
      },
      {
        "id": 2231106895,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134477,
        "form": "D",
        "sort_order": 3
      },
      {
        "id": 2271371313,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134490,
        "form": "D",
        "sort_order": 5
      },
      {
        "id": 2291180387,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134498,
        "form": "D",
        "sort_order": 6
      },
      {
        "id": 2302737105,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134512,
        "form": "L",
        "sort_order": 7
      },
      {
        "id": 2330546130,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134515,
        "form": "L",
        "sort_order": 8
      },
      {
        "id": 2346793427,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134525,
        "form": "L",
        "sort_order": 9
      },
      {
        "id": 2384881429,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134540,
        "form": "W",
        "sort_order": 11
      },
      {
        "id": 2451343497,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134548,
        "form": "L",
        "sort_order": 15
      },
      {
        "id": 2582280012,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134556,
        "form": "L",
        "sort_order": 21
      },
      {
        "id": 2832965343,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134568,
        "form": "L",
        "sort_order": 24
      },
      {
        "id": 3091790356,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134573,
        "form": "D",
        "sort_order": 25
      },
      {
        "id": 3237863011,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134588,
        "form": "L",
        "sort_order": 26
      },
      {
        "id": 2415152784,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134598,
        "form": "D",
        "sort_order": 12
      },
      {
        "id": 2427854497,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134609,
        "form": "L",
        "sort_order": 13
      },
      {
        "id": 2658172320,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134617,
        "form": "L",
        "sort_order": 22
      },
      {
        "id": 2256383928,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134625,
        "form": "D",
        "sort_order": 4
      },
      {
        "id": 2463548941,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134642,
        "form": "W",
        "sort_order": 16
      },
      {
        "id": 2721178955,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134648,
        "form": "L",
        "sort_order": 23
      },
      {
        "id": 2362092521,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134871,
        "form": "D",
        "sort_order": 10
      },
      {
        "id": 2437042441,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134884,
        "form": "L",
        "sort_order": 14
      },
      {
        "id": 2478849307,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134894,
        "form": "L",
        "sort_order": 17
      },
      {
        "id": 2488725435,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134900,
        "form": "L",
        "sort_order": 18
      },
      {
        "id": 2492364384,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134914,
        "form": "W",
        "sort_order": 19
      },
      {
        "id": 2499663871,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134923,
        "form": "D",
        "sort_order": 20
      },
      {
        "id": 3322518452,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134938,
        "form": "L",
        "sort_order": 27
      },
      {
        "id": 3572372795,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134942,
        "form": "L",
        "sort_order": 28
      },
      {
        "id": 3772409118,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134954,
        "form": "L",
        "sort_order": 29
      },
      {
        "id": 4226061529,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134959,
        "form": "W",
        "sort_order": 30
      },
      {
        "id": 4317111062,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134974,
        "form": "L",
        "sort_order": 31
      },
      {
        "id": 4614205862,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134982,
        "form": "D",
        "sort_order": 32
      },
      {
        "id": 4807289160,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19134994,
        "form": "L",
        "sort_order": 33
      },
      {
        "id": 4945039678,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19135005,
        "form": "L",
        "sort_order": 34
      },
      {
        "id": 5121497356,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19135015,
        "form": "D",
        "sort_order": 35
      },
      {
        "id": 5284603887,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19135021,
        "form": "L",
        "sort_order": 36
      },
      {
        "id": 5490389661,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19135036,
        "form": "L",
        "sort_order": 37
      },
      {
        "id": 5619792696,
        "standing_type": "standing",
        "standing_id": 229324,
        "fixture_id": 19135041,
        "form": "L",
        "sort_order": 38
      }
    ],
    "stage": {
      "id": 77471288,
      "sport_id": 1,
      "league_id": 8,
      "season_id": 23614,
      "type_id": 223,
      "name": "Regular Season",
      "sort_order": 1,
      "finished": true,
      "is_current": false,
      "starting_at": "2024-08-16",
      "ending_at": "2025-05-25",
      "games_in_current_week": false,
      "tie_breaker_rule_id": null
    },
    "league": {
      "id": 8,
      "sport_id": 1,
      "country_id": 462,
      "name": "Premier League",
      "active": true,
      "short_code": "UK PL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/leagues/8/8.png",
      "type": "league",
      "sub_type": "domestic",
      "last_played_at": "2025-05-25 15:00:00",
      "category": 1,
      "has_jerseys": false
    },
    "group": null
  },
  {
    "id": 229331,
    "participant_id": 65,
    "sport_id": 1,
    "league_id": 8,
    "season_id": 23614,
    "stage_id": 77471288,
    "group_id": null,
    "round_id": 339273,
    "standing_rule_id": 117812,
    "position": 20,
    "result": "equal",
    "points": 12,
    "participant": {
      "id": 65,
      "sport_id": 1,
      "country_id": 462,
      "venue_id": 167,
      "gender": "male",
      "name": "Southampton",
      "short_code": "SOU",
      "image_path": "https://cdn.sportmonks.com/images/soccer/teams/1/65.png",
      "founded": 1885,
      "type": "domestic",
      "placeholder": false,
      "last_played_at": "2025-05-25 15:00:00"
    },
    "rule": {
      "id": 117812,
      "model_type": "stage",
      "model_id": 77471288,
      "type_id": 182,
      "position": 20,
      "type": {
        "id": 182,
        "name": "Relegation",
        "code": "relegation",
        "developer_name": "RELEGATION",
        "model_type": "standing_rule",
        "stat_group": null
      }
    },
    "details": [
      {
        "id": 3424070624,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 7939,
        "value": 27,
        "type": {
          "id": 7939,
          "name": "Expected Points (xPTS)",
          "code": "expected-points",
          "developer_name": "EXPECTED_POINTS",
          "model_type": "statistic",
          "stat_group": "offensive"
        }
      },
      {
        "id": 3131200761,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 187,
        "value": 12,
        "type": {
          "id": 187,
          "name": "Overall Points",
          "code": "overall-points",
          "developer_name": "TOTAL_POINTS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200768,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 146,
        "value": 39,
        "type": {
          "id": 146,
          "name": "Away Goals Conceded",
          "code": "away-conceded",
          "developer_name": "AWAY_CONCEDED",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200769,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 179,
        "value": -60,
        "type": {
          "id": 179,
          "name": "Goal Difference",
          "code": "goal-difference",
          "developer_name": "OVERALL_GOAL_DIFFERENCE",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200754,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 135,
        "value": 19,
        "type": {
          "id": 135,
          "name": "Home Matched Played",
          "code": "home-matches-played",
          "developer_name": "HOME_MATCHES",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200752,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 131,
        "value": 6,
        "type": {
          "id": 131,
          "name": "Overall Draw",
          "code": "overall-draw",
          "developer_name": "OVERALL_DRAWS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200756,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 137,
        "value": 3,
        "type": {
          "id": 137,
          "name": "Home Draw",
          "code": "home-draw",
          "developer_name": "HOME_DRAWS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200759,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 139,
        "value": 13,
        "type": {
          "id": 139,
          "name": "Home Goals Scored",
          "code": "home-scored",
          "developer_name": "HOME_SCORED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200760,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 140,
        "value": 47,
        "type": {
          "id": 140,
          "name": "Home Goals Conceded",
          "code": "home-conceded",
          "developer_name": "HOME_CONCEDED",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200766,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 186,
        "value": 6,
        "type": {
          "id": 186,
          "name": "Away Points",
          "code": "away-points",
          "developer_name": "AWAY_POINTS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200762,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 141,
        "value": 19,
        "type": {
          "id": 141,
          "name": "Away Matched Played",
          "code": "away-matches-played",
          "developer_name": "AWAY_MATCHES",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200763,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 142,
        "value": 1,
        "type": {
          "id": 142,
          "name": "Away Won",
          "code": "away-won",
          "developer_name": "AWAY_WINS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200764,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 143,
        "value": 3,
        "type": {
          "id": 143,
          "name": "Away Draw",
          "code": "away-draw",
          "developer_name": "AWAY_DRAWS",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200748,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 133,
        "value": 26,
        "type": {
          "id": 133,
          "name": "Overal Goals Scored",
          "code": "overall-goals-for",
          "developer_name": "OVERALL_SCORED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200749,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 134,
        "value": 86,
        "type": {
          "id": 134,
          "name": "Overall Goals Conceded",
          "code": "overall-goals-against",
          "developer_name": "OVERALL_CONCEDED",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200750,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 129,
        "value": 38,
        "type": {
          "id": 129,
          "name": "Overall Matches Played",
          "code": "overall-matches-played",
          "developer_name": "OVERALL_MATCHES",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200751,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 130,
        "value": 2,
        "type": {
          "id": 130,
          "name": "Overall Won",
          "code": "overall-won",
          "developer_name": "OVERALL_WINS",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200753,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 132,
        "value": 30,
        "type": {
          "id": 132,
          "name": "Overall Lost",
          "code": "overall-lost",
          "developer_name": "OVERALL_LOST",
          "model_type": "standings",
          "stat_group": "overall"
        }
      },
      {
        "id": 3131200755,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 136,
        "value": 1,
        "type": {
          "id": 136,
          "name": "Home Won",
          "code": "home-won",
          "developer_name": "HOME_WINS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200757,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 138,
        "value": 15,
        "type": {
          "id": 138,
          "name": "Home Lost",
          "code": "home-lost",
          "developer_name": "HOME_LOST",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200758,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 185,
        "value": 6,
        "type": {
          "id": 185,
          "name": "Home Points",
          "code": "home-points",
          "developer_name": "HOME_POINTS",
          "model_type": "standings",
          "stat_group": "home"
        }
      },
      {
        "id": 3131200765,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 144,
        "value": 15,
        "type": {
          "id": 144,
          "name": "Away Lost",
          "code": "away-lost",
          "developer_name": "AWAY_LOST",
          "model_type": "standings",
          "stat_group": "away"
        }
      },
      {
        "id": 3131200767,
        "standing_type": "standing",
        "standing_id": 229331,
        "type_id": 145,
        "value": 13,
        "type": {
          "id": 145,
          "name": "Away Goals Scored",
          "code": "away-scored",
          "developer_name": "AWAY_SCORED",
          "model_type": "standings",
          "stat_group": "away"
        }
      }
    ],
    "form": [
      {
        "id": 2203085921,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134457,
        "form": "L",
        "sort_order": 1
      },
      {
        "id": 2217305463,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134470,
        "form": "L",
        "sort_order": 2
      },
      {
        "id": 2231107218,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134474,
        "form": "L",
        "sort_order": 3
      },
      {
        "id": 2271371522,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134490,
        "form": "D",
        "sort_order": 5
      },
      {
        "id": 2293631155,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134493,
        "form": "L",
        "sort_order": 6
      },
      {
        "id": 2302755823,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134503,
        "form": "L",
        "sort_order": 7
      },
      {
        "id": 2330386634,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134520,
        "form": "L",
        "sort_order": 8
      },
      {
        "id": 2346793610,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134531,
        "form": "L",
        "sort_order": 9
      },
      {
        "id": 2380376257,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134542,
        "form": "L",
        "sort_order": 11
      },
      {
        "id": 2446978639,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134543,
        "form": "L",
        "sort_order": 15
      },
      {
        "id": 2582318436,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134562,
        "form": "L",
        "sort_order": 21
      },
      {
        "id": 2832965425,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134568,
        "form": "W",
        "sort_order": 24
      },
      {
        "id": 3091790472,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134580,
        "form": "L",
        "sort_order": 25
      },
      {
        "id": 3237537925,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134592,
        "form": "L",
        "sort_order": 26
      },
      {
        "id": 2414509244,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134602,
        "form": "L",
        "sort_order": 12
      },
      {
        "id": 2423498525,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134604,
        "form": "D",
        "sort_order": 13
      },
      {
        "id": 2652413797,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134621,
        "form": "L",
        "sort_order": 22
      },
      {
        "id": 2255567296,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134630,
        "form": "L",
        "sort_order": 4
      },
      {
        "id": 2468878850,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134641,
        "form": "L",
        "sort_order": 16
      },
      {
        "id": 2721179251,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134650,
        "form": "L",
        "sort_order": 23
      },
      {
        "id": 2362092631,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134876,
        "form": "W",
        "sort_order": 10
      },
      {
        "id": 2438801279,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134888,
        "form": "L",
        "sort_order": 14
      },
      {
        "id": 2482031857,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134893,
        "form": "D",
        "sort_order": 17
      },
      {
        "id": 2487385803,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134907,
        "form": "L",
        "sort_order": 18
      },
      {
        "id": 2491461610,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134911,
        "form": "L",
        "sort_order": 19
      },
      {
        "id": 2497547267,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134926,
        "form": "L",
        "sort_order": 20
      },
      {
        "id": 3314872990,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134936,
        "form": "L",
        "sort_order": 27
      },
      {
        "id": 3573044154,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134943,
        "form": "L",
        "sort_order": 28
      },
      {
        "id": 3772409175,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134958,
        "form": "L",
        "sort_order": 29
      },
      {
        "id": 4226116816,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134967,
        "form": "D",
        "sort_order": 30
      },
      {
        "id": 4386466126,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134977,
        "form": "L",
        "sort_order": 31
      },
      {
        "id": 4541772612,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134987,
        "form": "L",
        "sort_order": 32
      },
      {
        "id": 4770517917,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19134998,
        "form": "D",
        "sort_order": 33
      },
      {
        "id": 4944298796,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19135007,
        "form": "L",
        "sort_order": 34
      },
      {
        "id": 5122300786,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19135016,
        "form": "L",
        "sort_order": 35
      },
      {
        "id": 5284604252,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19135026,
        "form": "D",
        "sort_order": 36
      },
      {
        "id": 5476133914,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19135035,
        "form": "L",
        "sort_order": 37
      },
      {
        "id": 5619792764,
        "standing_type": "standing",
        "standing_id": 229331,
        "fixture_id": 19135046,
        "form": "L",
        "sort_order": 38
      }
    ],
    "stage": {
      "id": 77471288,
      "sport_id": 1,
      "league_id": 8,
      "season_id": 23614,
      "type_id": 223,
      "name": "Regular Season",
      "sort_order": 1,
      "finished": true,
      "is_current": false,
      "starting_at": "2024-08-16",
      "ending_at": "2025-05-25",
      "games_in_current_week": false,
      "tie_breaker_rule_id": null
    },
    "league": {
      "id": 8,
      "sport_id": 1,
      "country_id": 462,
      "name": "Premier League",
      "active": true,
      "short_code": "UK PL",
      "image_path": "https://cdn.sportmonks.com/images/soccer/leagues/8/8.png",
      "type": "league",
      "sub_type": "domestic",
      "last_played_at": "2025-05-25 15:00:00",
      "category": 1,
      "has_jerseys": false
    },
    "group": null
  }]
    return JsonResponse(data, safe=False)