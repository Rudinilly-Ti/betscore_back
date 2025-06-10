from decouple import config
from django.http import JsonResponse
import requests

API_KEY = config('MYSPORTMONKS_API')
BASE_URL = 'https://api.sportmonks.com/v3/football'

def get_agenda_time(request, team_id):
#     url = f"{BASE_URL}/schedules/teams/{team_id}" # Exemplo de endpoint para buscar partidas agendadas de um time específico
#     params = {
#         'api_token': API_KEY,
#     }
#     response = requests.get(url, params=params)

#     if response.status_code == 200:
#         data = response.json()
#         return JsonResponse(data, safe=False)
#     else:
#         return JsonResponse({'error': 'Failed to fetch data'}, status=response.status_code)
    
    null = None
    true = True
    false = False
    response = [
  {
    "id": 77476001,
    "sport_id": 1,
    "league_id": 3147,
    "season_id": 25277,
    "type_id": 223,
    "name": "Regular Season",
    "sort_order": 1,
    "finished": false,
    "is_current": false,
    "starting_at": "2025-07-26",
    "ending_at": "2025-08-03",
    "games_in_current_week": false,
    "tie_breaker_rule_id": null,
    "aggregates": [],
    "rounds": [
      {
        "id": 369187,
        "sport_id": 1,
        "league_id": 3147,
        "season_id": 25277,
        "stage_id": 77476001,
        "name": "2",
        "finished": false,
        "is_current": false,
        "starting_at": "2025-07-30",
        "ending_at": "2025-07-31",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19399483,
            "sport_id": 1,
            "league_id": 3147,
            "season_id": 25277,
            "stage_id": 77476001,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 369187,
            "state_id": 1,
            "venue_id": 206,
            "name": "Manchester United vs AFC Bournemouth",
            "starting_at": "2025-07-31 01:30:00",
            "result_info": null,
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": false,
            "has_premium_odds": false,
            "starting_at_timestamp": 1753925400,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": null,
                  "position": null
                }
              },
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": null,
                  "position": null
                }
              }
            ],
            "scores": []
          }
        ]
      },
      {
        "id": 369186,
        "sport_id": 1,
        "league_id": 3147,
        "season_id": 25277,
        "stage_id": 77476001,
        "name": "1",
        "finished": false,
        "is_current": false,
        "starting_at": "2025-07-26",
        "ending_at": "2025-07-26",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19399481,
            "sport_id": 1,
            "league_id": 3147,
            "season_id": 25277,
            "stage_id": 77476001,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 369186,
            "state_id": 1,
            "venue_id": 21826,
            "name": "Manchester United vs West Ham United",
            "starting_at": "2025-07-26 23:00:00",
            "result_info": null,
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": false,
            "has_premium_odds": false,
            "starting_at_timestamp": 1753570800,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": null,
                  "position": null
                }
              },
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": null,
                  "position": null
                }
              }
            ],
            "scores": []
          }
        ]
      },
      {
        "id": 369188,
        "sport_id": 1,
        "league_id": 3147,
        "season_id": 25277,
        "stage_id": 77476001,
        "name": "3",
        "finished": false,
        "is_current": false,
        "starting_at": "2025-08-03",
        "ending_at": "2025-08-03",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19399485,
            "sport_id": 1,
            "league_id": 3147,
            "season_id": 25277,
            "stage_id": 77476001,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 369188,
            "state_id": 1,
            "venue_id": 161191,
            "name": "Manchester United vs Everton",
            "starting_at": "2025-08-03 21:00:00",
            "result_info": null,
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": false,
            "has_premium_odds": false,
            "starting_at_timestamp": 1754254800,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": null,
                  "position": null
                }
              },
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": null,
                  "position": null
                }
              }
            ],
            "scores": []
          }
        ]
      }
    ]
  },
  {
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
    "tie_breaker_rule_id": null,
    "aggregates": [],
    "rounds": [
      {
        "id": 339245,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "11",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-11-09",
        "ending_at": "2024-11-10",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134538,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339245,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs Leicester City",
            "starting_at": "2024-11-10 14:00:00",
            "result_info": "Manchester United won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1731247200,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 14
                }
              },
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 19
                }
              }
            ],
            "scores": [
              {
                "id": 15190569,
                "fixture_id": 19134538,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15190600,
                "fixture_id": 19134538,
                "type_id": 1525,
                "participant_id": 42,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15191305,
                "fixture_id": 19134538,
                "type_id": 2,
                "participant_id": 42,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15190601,
                "fixture_id": 19134538,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15730155,
                "fixture_id": 19134538,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15730156,
                "fixture_id": 19134538,
                "type_id": 48996,
                "participant_id": 42,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15190570,
                "fixture_id": 19134538,
                "type_id": 1,
                "participant_id": 42,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15191304,
                "fixture_id": 19134538,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              }
            ]
          }
        ]
      },
      {
        "id": 339256,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "22",
        "finished": true,
        "is_current": false,
        "starting_at": "2025-01-18",
        "ending_at": "2025-01-20",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134619,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339256,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs Brighton & Hove Albion",
            "starting_at": "2025-01-19 14:00:00",
            "result_info": "Brighton & Hove Albion won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1737295200,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 13
                }
              },
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": true,
                  "position": 9
                }
              }
            ],
            "scores": [
              {
                "id": 15430182,
                "fixture_id": 19134619,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15430183,
                "fixture_id": 19134619,
                "type_id": 1525,
                "participant_id": 78,
                "score": {
                  "goals": 3,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15430186,
                "fixture_id": 19134619,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15430187,
                "fixture_id": 19134619,
                "type_id": 2,
                "participant_id": 78,
                "score": {
                  "goals": 3,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15430184,
                "fixture_id": 19134619,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15430185,
                "fixture_id": 19134619,
                "type_id": 1,
                "participant_id": 78,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15432360,
                "fixture_id": 19134619,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15432361,
                "fixture_id": 19134619,
                "type_id": 48996,
                "participant_id": 78,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      },
      {
        "id": 339251,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "17",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-12-21",
        "ending_at": "2024-12-22",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134896,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339251,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs AFC Bournemouth",
            "starting_at": "2024-12-22 14:00:00",
            "result_info": "AFC Bournemouth won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1734876000,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 13
                }
              },
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": true,
                  "position": 8
                }
              }
            ],
            "scores": [
              {
                "id": 15366103,
                "fixture_id": 19134896,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15366113,
                "fixture_id": 19134896,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15366476,
                "fixture_id": 19134896,
                "type_id": 2,
                "participant_id": 52,
                "score": {
                  "goals": 3,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15730614,
                "fixture_id": 19134896,
                "type_id": 48996,
                "participant_id": 52,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15730613,
                "fixture_id": 19134896,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15366114,
                "fixture_id": 19134896,
                "type_id": 1525,
                "participant_id": 52,
                "score": {
                  "goals": 3,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15366475,
                "fixture_id": 19134896,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15366104,
                "fixture_id": 19134896,
                "type_id": 1,
                "participant_id": 52,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              }
            ]
          }
        ]
      },
      {
        "id": 339268,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "33",
        "finished": true,
        "is_current": false,
        "starting_at": "2025-04-19",
        "ending_at": "2025-04-21",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134996,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339268,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs Wolverhampton Wanderers",
            "starting_at": "2025-04-20 13:00:00",
            "result_info": "Wolverhampton Wanderers won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1745154000,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": true,
                  "position": 15
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 14
                }
              }
            ],
            "scores": [
              {
                "id": 16285384,
                "fixture_id": 19134996,
                "type_id": 48996,
                "participant_id": 29,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16285383,
                "fixture_id": 19134996,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16283974,
                "fixture_id": 19134996,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 16283975,
                "fixture_id": 19134996,
                "type_id": 1,
                "participant_id": 29,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16283973,
                "fixture_id": 19134996,
                "type_id": 1525,
                "participant_id": 29,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 16283976,
                "fixture_id": 19134996,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16283977,
                "fixture_id": 19134996,
                "type_id": 2,
                "participant_id": 29,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16283978,
                "fixture_id": 19134996,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              }
            ]
          }
        ]
      },
      {
        "id": 339242,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "8",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-10-19",
        "ending_at": "2024-10-21",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134517,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339242,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs Brentford",
            "starting_at": "2024-10-19 14:00:00",
            "result_info": "Manchester United won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1729346400,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 11
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 13
                }
              }
            ],
            "scores": [
              {
                "id": 15059231,
                "fixture_id": 19134517,
                "type_id": 1525,
                "participant_id": 236,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15059047,
                "fixture_id": 19134517,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15059049,
                "fixture_id": 19134517,
                "type_id": 1,
                "participant_id": 236,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15730114,
                "fixture_id": 19134517,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15060617,
                "fixture_id": 19134517,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15059233,
                "fixture_id": 19134517,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15060618,
                "fixture_id": 19134517,
                "type_id": 2,
                "participant_id": 236,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15730113,
                "fixture_id": 19134517,
                "type_id": 48996,
                "participant_id": 236,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      },
      {
        "id": 339248,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "14",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-12-03",
        "ending_at": "2024-12-05",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134880,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339248,
            "state_id": 5,
            "venue_id": 204,
            "name": "Arsenal vs Manchester United",
            "starting_at": "2024-12-04 20:15:00",
            "result_info": "Arsenal won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1733343300,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 2
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 14
                }
              }
            ],
            "scores": [
              {
                "id": 15301810,
                "fixture_id": 19134880,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15301811,
                "fixture_id": 19134880,
                "type_id": 1525,
                "participant_id": 19,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15301808,
                "fixture_id": 19134880,
                "type_id": 1,
                "participant_id": 19,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15301895,
                "fixture_id": 19134880,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15301809,
                "fixture_id": 19134880,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15301894,
                "fixture_id": 19134880,
                "type_id": 2,
                "participant_id": 19,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15730581,
                "fixture_id": 19134880,
                "type_id": 48996,
                "participant_id": 19,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15730582,
                "fixture_id": 19134880,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      },
      {
        "id": 339235,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "1",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-08-16",
        "ending_at": "2024-08-19",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134453,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339235,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs Fulham",
            "starting_at": "2024-08-16 19:00:00",
            "result_info": "Manchester United won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1723834800,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 8
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 13
                }
              }
            ],
            "scores": [
              {
                "id": 14731777,
                "fixture_id": 19134453,
                "type_id": 1,
                "participant_id": 11,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 14731919,
                "fixture_id": 19134453,
                "type_id": 2,
                "participant_id": 11,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15729985,
                "fixture_id": 19134453,
                "type_id": 48996,
                "participant_id": 11,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15729986,
                "fixture_id": 19134453,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 14731778,
                "fixture_id": 19134453,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 14731920,
                "fixture_id": 19134453,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 14731779,
                "fixture_id": 19134453,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 14731780,
                "fixture_id": 19134453,
                "type_id": 1525,
                "participant_id": 11,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "CURRENT"
              }
            ]
          }
        ]
      },
      {
        "id": 339249,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "15",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-12-07",
        "ending_at": "2025-02-12",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134550,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339249,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs Nottingham Forest",
            "starting_at": "2024-12-07 17:30:00",
            "result_info": "Nottingham Forest won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1733592600,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 14
                }
              },
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": true,
                  "position": 6
                }
              }
            ],
            "scores": [
              {
                "id": 15312886,
                "fixture_id": 19134550,
                "type_id": 1525,
                "participant_id": 63,
                "score": {
                  "goals": 3,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15312884,
                "fixture_id": 19134550,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15312885,
                "fixture_id": 19134550,
                "type_id": 1,
                "participant_id": 63,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15313558,
                "fixture_id": 19134550,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15313559,
                "fixture_id": 19134550,
                "type_id": 2,
                "participant_id": 63,
                "score": {
                  "goals": 3,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15730178,
                "fixture_id": 19134550,
                "type_id": 48996,
                "participant_id": 63,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15730177,
                "fixture_id": 19134550,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15312887,
                "fixture_id": 19134550,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "CURRENT"
              }
            ]
          }
        ]
      },
      {
        "id": 339241,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "7",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-10-05",
        "ending_at": "2024-10-06",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134504,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339241,
            "state_id": 5,
            "venue_id": 5,
            "name": "Aston Villa vs Manchester United",
            "starting_at": "2024-10-06 13:00:00",
            "result_info": "Game ended in draw.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1728219600,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 7
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 14
                }
              }
            ],
            "scores": [
              {
                "id": 15000370,
                "fixture_id": 19134504,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15000369,
                "fixture_id": 19134504,
                "type_id": 2,
                "participant_id": 15,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15730087,
                "fixture_id": 19134504,
                "type_id": 48996,
                "participant_id": 15,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15730088,
                "fixture_id": 19134504,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 14999174,
                "fixture_id": 19134504,
                "type_id": 1525,
                "participant_id": 15,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 14999170,
                "fixture_id": 19134504,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 14998893,
                "fixture_id": 19134504,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 14998892,
                "fixture_id": 19134504,
                "type_id": 1,
                "participant_id": 15,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              }
            ]
          }
        ]
      },
      {
        "id": 339247,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "13",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-11-29",
        "ending_at": "2024-12-01",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134608,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339247,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs Everton",
            "starting_at": "2024-12-01 13:30:00",
            "result_info": "Manchester United won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1733059800,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 13
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 14
                }
              }
            ],
            "scores": [
              {
                "id": 15730213,
                "fixture_id": 19134608,
                "type_id": 48996,
                "participant_id": 13,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15730214,
                "fixture_id": 19134608,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15288574,
                "fixture_id": 19134608,
                "type_id": 2,
                "participant_id": 13,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15287718,
                "fixture_id": 19134608,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 4,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15287704,
                "fixture_id": 19134608,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15287719,
                "fixture_id": 19134608,
                "type_id": 1525,
                "participant_id": 13,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15287703,
                "fixture_id": 19134608,
                "type_id": 1,
                "participant_id": 13,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15288575,
                "fixture_id": 19134608,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 4,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              }
            ]
          }
        ]
      },
      {
        "id": 339257,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "23",
        "finished": true,
        "is_current": false,
        "starting_at": "2025-01-25",
        "ending_at": "2025-01-26",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134647,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339257,
            "state_id": 5,
            "venue_id": 485,
            "name": "Fulham vs Manchester United",
            "starting_at": "2025-01-26 19:00:00",
            "result_info": "Manchester United won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1737918000,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 10
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": true,
                  "position": 13
                }
              }
            ],
            "scores": [
              {
                "id": 15460234,
                "fixture_id": 19134647,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15460232,
                "fixture_id": 19134647,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15460237,
                "fixture_id": 19134647,
                "type_id": 2,
                "participant_id": 11,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15460235,
                "fixture_id": 19134647,
                "type_id": 1,
                "participant_id": 11,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15460236,
                "fixture_id": 19134647,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15460625,
                "fixture_id": 19134647,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15460624,
                "fixture_id": 19134647,
                "type_id": 48996,
                "participant_id": 11,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15460233,
                "fixture_id": 19134647,
                "type_id": 1525,
                "participant_id": 11,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "CURRENT"
              }
            ]
          }
        ]
      },
      {
        "id": 339246,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "12",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-11-23",
        "ending_at": "2024-11-25",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134598,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339246,
            "state_id": 5,
            "venue_id": 504,
            "name": "Ipswich Town vs Manchester United",
            "starting_at": "2024-11-24 16:30:00",
            "result_info": "Game ended in draw.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1732465800,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 18
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 14
                }
              }
            ],
            "scores": [
              {
                "id": 15730193,
                "fixture_id": 19134598,
                "type_id": 48996,
                "participant_id": 116,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15730194,
                "fixture_id": 19134598,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15260278,
                "fixture_id": 19134598,
                "type_id": 1,
                "participant_id": 116,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15260279,
                "fixture_id": 19134598,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15260283,
                "fixture_id": 19134598,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15260604,
                "fixture_id": 19134598,
                "type_id": 2,
                "participant_id": 116,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15260282,
                "fixture_id": 19134598,
                "type_id": 1525,
                "participant_id": 116,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15260605,
                "fixture_id": 19134598,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              }
            ]
          }
        ]
      },
      {
        "id": 339271,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "36",
        "finished": true,
        "is_current": false,
        "starting_at": "2025-05-10",
        "ending_at": "2025-05-11",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19135023,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339271,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs West Ham United",
            "starting_at": "2025-05-11 13:15:00",
            "result_info": "West Ham United won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1746969300,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 15
                }
              },
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": true,
                  "position": 17
                }
              }
            ],
            "scores": [
              {
                "id": 16401732,
                "fixture_id": 19135023,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16401733,
                "fixture_id": 19135023,
                "type_id": 2,
                "participant_id": 1,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16401728,
                "fixture_id": 19135023,
                "type_id": 1525,
                "participant_id": 1,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 16401731,
                "fixture_id": 19135023,
                "type_id": 1,
                "participant_id": 1,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16401729,
                "fixture_id": 19135023,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16403838,
                "fixture_id": 19135023,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16403839,
                "fixture_id": 19135023,
                "type_id": 48996,
                "participant_id": 1,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16401725,
                "fixture_id": 19135023,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "CURRENT"
              }
            ]
          }
        ]
      },
      {
        "id": 339237,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "3",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-08-31",
        "ending_at": "2024-09-01",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134479,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339237,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs Liverpool",
            "starting_at": "2024-09-01 15:00:00",
            "result_info": "Liverpool won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1725202800,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": true,
                  "position": 1
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 13
                }
              }
            ],
            "scores": [
              {
                "id": 14813731,
                "fixture_id": 19134479,
                "type_id": 1525,
                "participant_id": 8,
                "score": {
                  "goals": 3,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 14814172,
                "fixture_id": 19134479,
                "type_id": 2,
                "participant_id": 8,
                "score": {
                  "goals": 3,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15730038,
                "fixture_id": 19134479,
                "type_id": 48996,
                "participant_id": 8,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15730037,
                "fixture_id": 19134479,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 14813732,
                "fixture_id": 19134479,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 14813687,
                "fixture_id": 19134479,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 14813688,
                "fixture_id": 19134479,
                "type_id": 1,
                "participant_id": 8,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 14814171,
                "fixture_id": 19134479,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              }
            ]
          }
        ]
      },
      {
        "id": 339273,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "38",
        "finished": true,
        "is_current": true,
        "starting_at": "2025-05-25",
        "ending_at": "2025-05-25",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19135043,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339273,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs Aston Villa",
            "starting_at": "2025-05-25 15:00:00",
            "result_info": "Manchester United won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1748185200,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 16
                }
              },
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 6
                }
              }
            ],
            "scores": [
              {
                "id": 16557173,
                "fixture_id": 19135043,
                "type_id": 1,
                "participant_id": 15,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16557168,
                "fixture_id": 19135043,
                "type_id": 1525,
                "participant_id": 15,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 16557164,
                "fixture_id": 19135043,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 16557176,
                "fixture_id": 19135043,
                "type_id": 2,
                "participant_id": 15,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16557175,
                "fixture_id": 19135043,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16558887,
                "fixture_id": 19135043,
                "type_id": 48996,
                "participant_id": 15,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16557171,
                "fixture_id": 19135043,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16558886,
                "fixture_id": 19135043,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      },
      {
        "id": 339267,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "32",
        "finished": true,
        "is_current": false,
        "starting_at": "2025-04-12",
        "ending_at": "2025-04-14",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134985,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339267,
            "state_id": 5,
            "venue_id": 449,
            "name": "Newcastle United vs Manchester United",
            "starting_at": "2025-04-13 15:30:00",
            "result_info": "Newcastle United won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1744558200,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 7
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 13
                }
              }
            ],
            "scores": [
              {
                "id": 16245796,
                "fixture_id": 19134985,
                "type_id": 1525,
                "participant_id": 20,
                "score": {
                  "goals": 4,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 16245800,
                "fixture_id": 19134985,
                "type_id": 2,
                "participant_id": 20,
                "score": {
                  "goals": 4,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16245798,
                "fixture_id": 19134985,
                "type_id": 1,
                "participant_id": 20,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16247566,
                "fixture_id": 19134985,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16245799,
                "fixture_id": 19134985,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16247565,
                "fixture_id": 19134985,
                "type_id": 48996,
                "participant_id": 20,
                "score": {
                  "goals": 3,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16245797,
                "fixture_id": 19134985,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16245795,
                "fixture_id": 19134985,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "CURRENT"
              }
            ]
          }
        ]
      },
      {
        "id": 339244,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "10",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-11-02",
        "ending_at": "2024-11-04",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134873,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339244,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs Chelsea",
            "starting_at": "2024-11-03 16:30:00",
            "result_info": "Game ended in draw.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1730651400,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 13
                }
              },
              {
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
                "last_played_at": "2025-05-28 19:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 4
                }
              }
            ],
            "scores": [
              {
                "id": 15154722,
                "fixture_id": 19134873,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15154728,
                "fixture_id": 19134873,
                "type_id": 1525,
                "participant_id": 18,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15154729,
                "fixture_id": 19134873,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15155056,
                "fixture_id": 19134873,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15730568,
                "fixture_id": 19134873,
                "type_id": 48996,
                "participant_id": 18,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15730567,
                "fixture_id": 19134873,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15155057,
                "fixture_id": 19134873,
                "type_id": 2,
                "participant_id": 18,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15154723,
                "fixture_id": 19134873,
                "type_id": 1,
                "participant_id": 18,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              }
            ]
          }
        ]
      },
      {
        "id": 339262,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "27",
        "finished": true,
        "is_current": false,
        "starting_at": "2025-02-25",
        "ending_at": "2025-02-27",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134938,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339262,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs Ipswich Town",
            "starting_at": "2025-02-26 19:30:00",
            "result_info": "Manchester United won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1740598200,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 14
                }
              },
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 18
                }
              }
            ],
            "scores": [
              {
                "id": 15975597,
                "fixture_id": 19134938,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15975596,
                "fixture_id": 19134938,
                "type_id": 1525,
                "participant_id": 116,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15975595,
                "fixture_id": 19134938,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15976101,
                "fixture_id": 19134938,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15975600,
                "fixture_id": 19134938,
                "type_id": 2,
                "participant_id": 116,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15976102,
                "fixture_id": 19134938,
                "type_id": 48996,
                "participant_id": 116,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15975598,
                "fixture_id": 19134938,
                "type_id": 1,
                "participant_id": 116,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15975599,
                "fixture_id": 19134938,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              }
            ]
          }
        ]
      },
      {
        "id": 339263,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "28",
        "finished": true,
        "is_current": false,
        "starting_at": "2025-03-08",
        "ending_at": "2025-03-10",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134944,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339263,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs Arsenal",
            "starting_at": "2025-03-09 16:30:00",
            "result_info": "Game ended in draw.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1741537800,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 15
                }
              },
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 2
                }
              }
            ],
            "scores": [
              {
                "id": 16040965,
                "fixture_id": 19134944,
                "type_id": 2,
                "participant_id": 19,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16040960,
                "fixture_id": 19134944,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 16042122,
                "fixture_id": 19134944,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16040963,
                "fixture_id": 19134944,
                "type_id": 1,
                "participant_id": 19,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16042123,
                "fixture_id": 19134944,
                "type_id": 48996,
                "participant_id": 19,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16040962,
                "fixture_id": 19134944,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16040961,
                "fixture_id": 19134944,
                "type_id": 1525,
                "participant_id": 19,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 16040964,
                "fixture_id": 19134944,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              }
            ]
          }
        ]
      },
      {
        "id": 339250,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "16",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-12-14",
        "ending_at": "2024-12-16",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134638,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339250,
            "state_id": 5,
            "venue_id": 151,
            "name": "Manchester City vs Manchester United",
            "starting_at": "2024-12-15 16:30:00",
            "result_info": "Manchester United won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1734280200,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 4
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": true,
                  "position": 14
                }
              }
            ],
            "scores": [
              {
                "id": 15347916,
                "fixture_id": 19134638,
                "type_id": 2,
                "participant_id": 9,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15346889,
                "fixture_id": 19134638,
                "type_id": 1525,
                "participant_id": 9,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15346885,
                "fixture_id": 19134638,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15347917,
                "fixture_id": 19134638,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15346888,
                "fixture_id": 19134638,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15346884,
                "fixture_id": 19134638,
                "type_id": 1,
                "participant_id": 9,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15730254,
                "fixture_id": 19134638,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15730253,
                "fixture_id": 19134638,
                "type_id": 48996,
                "participant_id": 9,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      },
      {
        "id": 339270,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "35",
        "finished": true,
        "is_current": false,
        "starting_at": "2025-05-02",
        "ending_at": "2025-05-05",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19135011,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339270,
            "state_id": 5,
            "venue_id": 338817,
            "name": "Brentford vs Manchester United",
            "starting_at": "2025-05-04 13:00:00",
            "result_info": "Brentford won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1746363600,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 11
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 15
                }
              }
            ],
            "scores": [
              {
                "id": 16333221,
                "fixture_id": 19135011,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16333220,
                "fixture_id": 19135011,
                "type_id": 2,
                "participant_id": 236,
                "score": {
                  "goals": 4,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16333216,
                "fixture_id": 19135011,
                "type_id": 1525,
                "participant_id": 236,
                "score": {
                  "goals": 4,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 16333219,
                "fixture_id": 19135011,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16365144,
                "fixture_id": 19135011,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16333218,
                "fixture_id": 19135011,
                "type_id": 1,
                "participant_id": 236,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16365143,
                "fixture_id": 19135011,
                "type_id": 48996,
                "participant_id": 236,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16333217,
                "fixture_id": 19135011,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "away"
                },
                "description": "CURRENT"
              }
            ]
          }
        ]
      },
      {
        "id": 339243,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "9",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-10-25",
        "ending_at": "2024-10-27",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134532,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339243,
            "state_id": 5,
            "venue_id": 214,
            "name": "West Ham United vs Manchester United",
            "starting_at": "2024-10-27 14:00:00",
            "result_info": "West Ham United won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1730037600,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 13
                }
              },
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 16
                }
              }
            ],
            "scores": [
              {
                "id": 15113396,
                "fixture_id": 19134532,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15730144,
                "fixture_id": 19134532,
                "type_id": 48996,
                "participant_id": 1,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15113375,
                "fixture_id": 19134532,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15113376,
                "fixture_id": 19134532,
                "type_id": 1,
                "participant_id": 1,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15113397,
                "fixture_id": 19134532,
                "type_id": 1525,
                "participant_id": 1,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15114118,
                "fixture_id": 19134532,
                "type_id": 2,
                "participant_id": 1,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15114116,
                "fixture_id": 19134532,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15730143,
                "fixture_id": 19134532,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      },
      {
        "id": 339264,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "29",
        "finished": true,
        "is_current": false,
        "starting_at": "2025-02-19",
        "ending_at": "2025-04-16",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134955,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339264,
            "state_id": 5,
            "venue_id": 117,
            "name": "Leicester City vs Manchester United",
            "starting_at": "2025-03-16 19:00:00",
            "result_info": "Manchester United won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1742151600,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 19
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": true,
                  "position": 15
                }
              }
            ],
            "scores": [
              {
                "id": 16082574,
                "fixture_id": 19134955,
                "type_id": 1,
                "participant_id": 42,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16082573,
                "fixture_id": 19134955,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 16082575,
                "fixture_id": 19134955,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16082577,
                "fixture_id": 19134955,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16082572,
                "fixture_id": 19134955,
                "type_id": 1525,
                "participant_id": 42,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 16082576,
                "fixture_id": 19134955,
                "type_id": 2,
                "participant_id": 42,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16083946,
                "fixture_id": 19134955,
                "type_id": 48996,
                "participant_id": 42,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16083947,
                "fixture_id": 19134955,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      },
      {
        "id": 339252,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "18",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-12-26",
        "ending_at": "2024-12-27",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134908,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339252,
            "state_id": 5,
            "venue_id": 492,
            "name": "Wolverhampton Wanderers vs Manchester United",
            "starting_at": "2024-12-26 17:30:00",
            "result_info": "Wolverhampton Wanderers won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1735234200,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 18
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 14
                }
              }
            ],
            "scores": [
              {
                "id": 15372765,
                "fixture_id": 19134908,
                "type_id": 1,
                "participant_id": 29,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15372827,
                "fixture_id": 19134908,
                "type_id": 2,
                "participant_id": 29,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15372767,
                "fixture_id": 19134908,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15372766,
                "fixture_id": 19134908,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15372828,
                "fixture_id": 19134908,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15730638,
                "fixture_id": 19134908,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15372768,
                "fixture_id": 19134908,
                "type_id": 1525,
                "participant_id": 29,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15730637,
                "fixture_id": 19134908,
                "type_id": 48996,
                "participant_id": 29,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      },
      {
        "id": 339240,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "6",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-09-28",
        "ending_at": "2024-09-30",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134499,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339240,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs Tottenham Hotspur",
            "starting_at": "2024-09-29 15:30:00",
            "result_info": "Tottenham Hotspur won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1727623800,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": true,
                  "position": 14
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 13
                }
              }
            ],
            "scores": [
              {
                "id": 15730077,
                "fixture_id": 19134499,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15730078,
                "fixture_id": 19134499,
                "type_id": 48996,
                "participant_id": 6,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 14965151,
                "fixture_id": 19134499,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 14965163,
                "fixture_id": 19134499,
                "type_id": 1525,
                "participant_id": 6,
                "score": {
                  "goals": 3,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 14965160,
                "fixture_id": 19134499,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 14965759,
                "fixture_id": 19134499,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 14965150,
                "fixture_id": 19134499,
                "type_id": 1,
                "participant_id": 6,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 14965758,
                "fixture_id": 19134499,
                "type_id": 2,
                "participant_id": 6,
                "score": {
                  "goals": 3,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              }
            ]
          }
        ]
      },
      {
        "id": 339253,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "19",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-12-29",
        "ending_at": "2025-01-01",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134916,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339253,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs Newcastle United",
            "starting_at": "2024-12-30 20:00:00",
            "result_info": "Newcastle United won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1735588800,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": true,
                  "position": 6
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 13
                }
              }
            ],
            "scores": [
              {
                "id": 15378388,
                "fixture_id": 19134916,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15730653,
                "fixture_id": 19134916,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15730654,
                "fixture_id": 19134916,
                "type_id": 48996,
                "participant_id": 20,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15378387,
                "fixture_id": 19134916,
                "type_id": 1525,
                "participant_id": 20,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15378386,
                "fixture_id": 19134916,
                "type_id": 1,
                "participant_id": 20,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15378385,
                "fixture_id": 19134916,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15378430,
                "fixture_id": 19134916,
                "type_id": 2,
                "participant_id": 20,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15378429,
                "fixture_id": 19134916,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              }
            ]
          }
        ]
      },
      {
        "id": 339266,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "31",
        "finished": true,
        "is_current": false,
        "starting_at": "2025-04-05",
        "ending_at": "2025-04-07",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134976,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339266,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs Manchester City",
            "starting_at": "2025-04-06 15:30:00",
            "result_info": "Game ended in draw.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1743953400,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 13
                }
              },
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 5
                }
              }
            ],
            "scores": [
              {
                "id": 16200606,
                "fixture_id": 19134976,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 16200610,
                "fixture_id": 19134976,
                "type_id": 1525,
                "participant_id": 9,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 16200613,
                "fixture_id": 19134976,
                "type_id": 1,
                "participant_id": 9,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16200611,
                "fixture_id": 19134976,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16200617,
                "fixture_id": 19134976,
                "type_id": 2,
                "participant_id": 9,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16200615,
                "fixture_id": 19134976,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16202171,
                "fixture_id": 19134976,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16202172,
                "fixture_id": 19134976,
                "type_id": 48996,
                "participant_id": 9,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      },
      {
        "id": 339254,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "20",
        "finished": true,
        "is_current": false,
        "starting_at": "2025-01-04",
        "ending_at": "2025-01-06",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134924,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339254,
            "state_id": 5,
            "venue_id": 230,
            "name": "Liverpool vs Manchester United",
            "starting_at": "2025-01-05 16:30:00",
            "result_info": "Game ended in draw.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1736094600,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 13
                }
              },
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 1
                }
              }
            ],
            "scores": [
              {
                "id": 15387630,
                "fixture_id": 19134924,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15387342,
                "fixture_id": 19134924,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15387341,
                "fixture_id": 19134924,
                "type_id": 1,
                "participant_id": 8,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15387344,
                "fixture_id": 19134924,
                "type_id": 1525,
                "participant_id": 8,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15730669,
                "fixture_id": 19134924,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15730670,
                "fixture_id": 19134924,
                "type_id": 48996,
                "participant_id": 8,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15387629,
                "fixture_id": 19134924,
                "type_id": 2,
                "participant_id": 8,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15387343,
                "fixture_id": 19134924,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "CURRENT"
              }
            ]
          }
        ]
      },
      {
        "id": 339259,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "25",
        "finished": true,
        "is_current": false,
        "starting_at": "2025-02-14",
        "ending_at": "2025-02-16",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134581,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339259,
            "state_id": 5,
            "venue_id": 281313,
            "name": "Tottenham Hotspur vs Manchester United",
            "starting_at": "2025-02-16 16:30:00",
            "result_info": "Tottenham Hotspur won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1739723400,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 15
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 14
                }
              }
            ],
            "scores": [
              {
                "id": 15932991,
                "fixture_id": 19134581,
                "type_id": 1525,
                "participant_id": 6,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15932992,
                "fixture_id": 19134581,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15932995,
                "fixture_id": 19134581,
                "type_id": 2,
                "participant_id": 6,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15932994,
                "fixture_id": 19134581,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15932996,
                "fixture_id": 19134581,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15933828,
                "fixture_id": 19134581,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15933827,
                "fixture_id": 19134581,
                "type_id": 48996,
                "participant_id": 6,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15932993,
                "fixture_id": 19134581,
                "type_id": 1,
                "participant_id": 6,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              }
            ]
          }
        ]
      },
      {
        "id": 339238,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "4",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-09-14",
        "ending_at": "2024-09-15",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134630,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339238,
            "state_id": 5,
            "venue_id": 167,
            "name": "Southampton vs Manchester United",
            "starting_at": "2024-09-14 11:30:00",
            "result_info": "Manchester United won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1726313400,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": true,
                  "position": 13
                }
              },
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 20
                }
              }
            ],
            "scores": [
              {
                "id": 14865399,
                "fixture_id": 19134630,
                "type_id": 1525,
                "participant_id": 65,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 14866130,
                "fixture_id": 19134630,
                "type_id": 2,
                "participant_id": 65,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15730237,
                "fixture_id": 19134630,
                "type_id": 48996,
                "participant_id": 65,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15730238,
                "fixture_id": 19134630,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 14866131,
                "fixture_id": 19134630,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 14865398,
                "fixture_id": 19134630,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 14865388,
                "fixture_id": 19134630,
                "type_id": 1,
                "participant_id": 65,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 14865389,
                "fixture_id": 19134630,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              }
            ]
          }
        ]
      },
      {
        "id": 339239,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "5",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-09-21",
        "ending_at": "2024-09-22",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134485,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339239,
            "state_id": 5,
            "venue_id": 201,
            "name": "Crystal Palace vs Manchester United",
            "starting_at": "2024-09-21 16:30:00",
            "result_info": "Game ended in draw.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1726936200,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 12
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 13
                }
              }
            ],
            "scores": [
              {
                "id": 14908302,
                "fixture_id": 19134485,
                "type_id": 1,
                "participant_id": 51,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 14908303,
                "fixture_id": 19134485,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 14908850,
                "fixture_id": 19134485,
                "type_id": 2,
                "participant_id": 51,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15730050,
                "fixture_id": 19134485,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15730049,
                "fixture_id": 19134485,
                "type_id": 48996,
                "participant_id": 51,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 14908851,
                "fixture_id": 19134485,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 14908306,
                "fixture_id": 19134485,
                "type_id": 1525,
                "participant_id": 51,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 14908307,
                "fixture_id": 19134485,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "CURRENT"
              }
            ]
          }
        ]
      },
      {
        "id": 339236,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "2",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-08-24",
        "ending_at": "2024-08-25",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134465,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339236,
            "state_id": 5,
            "venue_id": 480,
            "name": "Brighton & Hove Albion vs Manchester United",
            "starting_at": "2024-08-24 11:30:00",
            "result_info": "Brighton & Hove Albion won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1724499000,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 7
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 13
                }
              }
            ],
            "scores": [
              {
                "id": 14765477,
                "fixture_id": 19134465,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 14766102,
                "fixture_id": 19134465,
                "type_id": 2,
                "participant_id": 78,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 14765480,
                "fixture_id": 19134465,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 14765476,
                "fixture_id": 19134465,
                "type_id": 1,
                "participant_id": 78,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 14766103,
                "fixture_id": 19134465,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 14765481,
                "fixture_id": 19134465,
                "type_id": 1525,
                "participant_id": 78,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15730010,
                "fixture_id": 19134465,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15730009,
                "fixture_id": 19134465,
                "type_id": 48996,
                "participant_id": 78,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      },
      {
        "id": 339269,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "34",
        "finished": true,
        "is_current": false,
        "starting_at": "2025-04-22",
        "ending_at": "2025-05-01",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134999,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339269,
            "state_id": 5,
            "venue_id": 146,
            "name": "AFC Bournemouth vs Manchester United",
            "starting_at": "2025-04-27 13:00:00",
            "result_info": "Game ended in draw.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1745758800,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 10
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 15
                }
              }
            ],
            "scores": [
              {
                "id": 16324356,
                "fixture_id": 19134999,
                "type_id": 48996,
                "participant_id": 52,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16324357,
                "fixture_id": 19134999,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16320832,
                "fixture_id": 19134999,
                "type_id": 1525,
                "participant_id": 52,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 16320835,
                "fixture_id": 19134999,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16320834,
                "fixture_id": 19134999,
                "type_id": 1,
                "participant_id": 52,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16320836,
                "fixture_id": 19134999,
                "type_id": 2,
                "participant_id": 52,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16320837,
                "fixture_id": 19134999,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16320833,
                "fixture_id": 19134999,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "CURRENT"
              }
            ]
          }
        ]
      },
      {
        "id": 339272,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "37",
        "finished": true,
        "is_current": false,
        "starting_at": "2025-05-16",
        "ending_at": "2025-05-20",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19135033,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339272,
            "state_id": 5,
            "venue_id": 321614,
            "name": "Chelsea vs Manchester United",
            "starting_at": "2025-05-16 19:15:00",
            "result_info": "Chelsea won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1747422900,
            "participants": [
              {
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
                "last_played_at": "2025-05-28 19:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 5
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 16
                }
              }
            ],
            "scores": [
              {
                "id": 16420610,
                "fixture_id": 19135033,
                "type_id": 48996,
                "participant_id": 18,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16420611,
                "fixture_id": 19135033,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16420020,
                "fixture_id": 19135033,
                "type_id": 2,
                "participant_id": 18,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16420018,
                "fixture_id": 19135033,
                "type_id": 1,
                "participant_id": 18,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16420017,
                "fixture_id": 19135033,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 16420019,
                "fixture_id": 19135033,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16420021,
                "fixture_id": 19135033,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16420016,
                "fixture_id": 19135033,
                "type_id": 1525,
                "participant_id": 18,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "CURRENT"
              }
            ]
          }
        ]
      },
      {
        "id": 339260,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "26",
        "finished": true,
        "is_current": false,
        "starting_at": "2025-02-21",
        "ending_at": "2025-02-23",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134586,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339260,
            "state_id": 5,
            "venue_id": 12,
            "name": "Everton vs Manchester United",
            "starting_at": "2025-02-22 12:30:00",
            "result_info": "Game ended in draw.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1740227400,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 15
                }
              },
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 14
                }
              }
            ],
            "scores": [
              {
                "id": 15952254,
                "fixture_id": 19134586,
                "type_id": 48996,
                "participant_id": 13,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15949980,
                "fixture_id": 19134586,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15949983,
                "fixture_id": 19134586,
                "type_id": 2,
                "participant_id": 13,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15949982,
                "fixture_id": 19134586,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15949981,
                "fixture_id": 19134586,
                "type_id": 1,
                "participant_id": 13,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15949979,
                "fixture_id": 19134586,
                "type_id": 1525,
                "participant_id": 13,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15952255,
                "fixture_id": 19134586,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15949978,
                "fixture_id": 19134586,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "CURRENT"
              }
            ]
          }
        ]
      },
      {
        "id": 339265,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "30",
        "finished": true,
        "is_current": false,
        "starting_at": "2025-04-01",
        "ending_at": "2025-04-03",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134962,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339265,
            "state_id": 5,
            "venue_id": 542,
            "name": "Nottingham Forest vs Manchester United",
            "starting_at": "2025-04-01 19:00:00",
            "result_info": "Nottingham Forest won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1743534000,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 3
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 13
                }
              }
            ],
            "scores": [
              {
                "id": 16164919,
                "fixture_id": 19134962,
                "type_id": 1,
                "participant_id": 63,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16164917,
                "fixture_id": 19134962,
                "type_id": 1525,
                "participant_id": 63,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 16164922,
                "fixture_id": 19134962,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16164918,
                "fixture_id": 19134962,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 16164921,
                "fixture_id": 19134962,
                "type_id": 2,
                "participant_id": 63,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16164920,
                "fixture_id": 19134962,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16165304,
                "fixture_id": 19134962,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16165303,
                "fixture_id": 19134962,
                "type_id": 48996,
                "participant_id": 63,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      },
      {
        "id": 339258,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "24",
        "finished": true,
        "is_current": false,
        "starting_at": "2025-02-01",
        "ending_at": "2025-02-03",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134569,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339258,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs Crystal Palace",
            "starting_at": "2025-02-02 14:00:00",
            "result_info": "Crystal Palace won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1738504800,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 12
                }
              },
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": true,
                  "position": 13
                }
              }
            ],
            "scores": [
              {
                "id": 15488666,
                "fixture_id": 19134569,
                "type_id": 1525,
                "participant_id": 51,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15488674,
                "fixture_id": 19134569,
                "type_id": 2,
                "participant_id": 51,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15488670,
                "fixture_id": 19134569,
                "type_id": 1,
                "participant_id": 51,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15488672,
                "fixture_id": 19134569,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15488667,
                "fixture_id": 19134569,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15488663,
                "fixture_id": 19134569,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15490978,
                "fixture_id": 19134569,
                "type_id": 48996,
                "participant_id": 51,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15490977,
                "fixture_id": 19134569,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      },
      {
        "id": 339255,
        "sport_id": 1,
        "league_id": 8,
        "season_id": 23614,
        "stage_id": 77471288,
        "name": "21",
        "finished": true,
        "is_current": false,
        "starting_at": "2025-01-14",
        "ending_at": "2025-01-16",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19134562,
            "sport_id": 1,
            "league_id": 8,
            "season_id": 23614,
            "stage_id": 77471288,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 339255,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs Southampton",
            "starting_at": "2025-01-16 20:00:00",
            "result_info": "Manchester United won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1737057600,
            "participants": [
              {
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
                "last_played_at": "2025-05-25 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 20
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 12
                }
              }
            ],
            "scores": [
              {
                "id": 15415498,
                "fixture_id": 19134562,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15415499,
                "fixture_id": 19134562,
                "type_id": 1525,
                "participant_id": 65,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15415501,
                "fixture_id": 19134562,
                "type_id": 1,
                "participant_id": 65,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15415623,
                "fixture_id": 19134562,
                "type_id": 48996,
                "participant_id": 65,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15415500,
                "fixture_id": 19134562,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15415503,
                "fixture_id": 19134562,
                "type_id": 2,
                "participant_id": 65,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15415622,
                "fixture_id": 19134562,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15415502,
                "fixture_id": 19134562,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": 77471034,
    "sport_id": 1,
    "league_id": 23,
    "season_id": 23551,
    "type_id": 224,
    "name": "Final",
    "sort_order": 1,
    "finished": true,
    "is_current": false,
    "starting_at": "2024-08-10",
    "ending_at": "2024-08-10",
    "games_in_current_week": false,
    "tie_breaker_rule_id": null,
    "fixtures": [
      {
        "id": 19127230,
        "sport_id": 1,
        "league_id": 23,
        "season_id": 23551,
        "stage_id": 77471034,
        "group_id": null,
        "aggregate_id": null,
        "round_id": null,
        "state_id": 8,
        "venue_id": 1315,
        "name": "Manchester City vs Manchester United",
        "starting_at": "2024-08-10 14:00:00",
        "result_info": "Manchester City won after penalties.",
        "leg": "1/1",
        "details": null,
        "length": 90,
        "placeholder": false,
        "has_odds": true,
        "has_premium_odds": true,
        "starting_at_timestamp": 1723298400,
        "participants": [
          {
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
            "last_played_at": "2025-05-25 15:00:00",
            "meta": {
              "location": "home",
              "winner": true,
              "position": 1
            }
          },
          {
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
            "last_played_at": "2025-05-30 12:00:00",
            "meta": {
              "location": "away",
              "winner": false,
              "position": 2
            }
          }
        ],
        "scores": [
          {
            "id": 14707763,
            "fixture_id": 19127230,
            "type_id": 1525,
            "participant_id": 9,
            "score": {
              "goals": 1,
              "participant": "home"
            },
            "description": "CURRENT"
          },
          {
            "id": 14707746,
            "fixture_id": 19127230,
            "type_id": 1,
            "participant_id": 9,
            "score": {
              "goals": 0,
              "participant": "home"
            },
            "description": "1ST_HALF"
          },
          {
            "id": 14707747,
            "fixture_id": 19127230,
            "type_id": 1,
            "participant_id": 14,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "1ST_HALF"
          },
          {
            "id": 14707762,
            "fixture_id": 19127230,
            "type_id": 1525,
            "participant_id": 14,
            "score": {
              "goals": 1,
              "participant": "away"
            },
            "description": "CURRENT"
          },
          {
            "id": 14708614,
            "fixture_id": 19127230,
            "type_id": 2,
            "participant_id": 9,
            "score": {
              "goals": 1,
              "participant": "home"
            },
            "description": "2ND_HALF"
          },
          {
            "id": 14709742,
            "fixture_id": 19127230,
            "type_id": 5,
            "participant_id": 9,
            "score": {
              "goals": 7,
              "participant": "home"
            },
            "description": "PENALTY_SHOOTOUT"
          },
          {
            "id": 14709743,
            "fixture_id": 19127230,
            "type_id": 5,
            "participant_id": 14,
            "score": {
              "goals": 6,
              "participant": "away"
            },
            "description": "PENALTY_SHOOTOUT"
          },
          {
            "id": 14708615,
            "fixture_id": 19127230,
            "type_id": 2,
            "participant_id": 14,
            "score": {
              "goals": 1,
              "participant": "away"
            },
            "description": "2ND_HALF"
          },
          {
            "id": 15720143,
            "fixture_id": 19127230,
            "type_id": 48996,
            "participant_id": 9,
            "score": {
              "goals": 1,
              "participant": "home"
            },
            "description": "2ND_HALF_ONLY"
          },
          {
            "id": 15720144,
            "fixture_id": 19127230,
            "type_id": 48996,
            "participant_id": 14,
            "score": {
              "goals": 1,
              "participant": "away"
            },
            "description": "2ND_HALF_ONLY"
          }
        ]
      }
    ],
    "rounds": []
  },
  {
    "id": 77471556,
    "sport_id": 1,
    "league_id": 27,
    "season_id": 23685,
    "type_id": 224,
    "name": "3rd Round",
    "sort_order": 3,
    "finished": true,
    "is_current": false,
    "starting_at": "2024-09-17",
    "ending_at": "2024-10-01",
    "games_in_current_week": false,
    "tie_breaker_rule_id": null,
    "fixtures": [
      {
        "id": 19292987,
        "sport_id": 1,
        "league_id": 27,
        "season_id": 23685,
        "stage_id": 77471556,
        "group_id": null,
        "aggregate_id": null,
        "round_id": null,
        "state_id": 5,
        "venue_id": 206,
        "name": "Manchester United vs Barnsley",
        "starting_at": "2024-09-17 19:00:00",
        "result_info": "Manchester United won after full-time.",
        "leg": "1/1",
        "details": null,
        "length": 90,
        "placeholder": false,
        "has_odds": true,
        "has_premium_odds": true,
        "starting_at_timestamp": 1726599600,
        "participants": [
          {
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
            "last_played_at": "2025-05-30 12:00:00",
            "meta": {
              "location": "home",
              "winner": true,
              "position": 1
            }
          },
          {
            "id": 54,
            "sport_id": 1,
            "country_id": 462,
            "venue_id": 497,
            "gender": "male",
            "name": "Barnsley",
            "short_code": "BRS",
            "image_path": "https://cdn.sportmonks.com/images/soccer/teams/22/54.png",
            "founded": 1887,
            "type": "domestic",
            "placeholder": false,
            "last_played_at": "2025-05-03 14:00:00",
            "meta": {
              "location": "away",
              "winner": false,
              "position": 2
            }
          }
        ],
        "scores": [
          {
            "id": 14892719,
            "fixture_id": 19292987,
            "type_id": 1525,
            "participant_id": 14,
            "score": {
              "goals": 7,
              "participant": "home"
            },
            "description": "CURRENT"
          },
          {
            "id": 14892714,
            "fixture_id": 19292987,
            "type_id": 1,
            "participant_id": 14,
            "score": {
              "goals": 3,
              "participant": "home"
            },
            "description": "1ST_HALF"
          },
          {
            "id": 14892715,
            "fixture_id": 19292987,
            "type_id": 1,
            "participant_id": 54,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "1ST_HALF"
          },
          {
            "id": 14892718,
            "fixture_id": 19292987,
            "type_id": 1525,
            "participant_id": 54,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "CURRENT"
          },
          {
            "id": 14892868,
            "fixture_id": 19292987,
            "type_id": 2,
            "participant_id": 14,
            "score": {
              "goals": 7,
              "participant": "home"
            },
            "description": "2ND_HALF"
          },
          {
            "id": 14892869,
            "fixture_id": 19292987,
            "type_id": 2,
            "participant_id": 54,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "2ND_HALF"
          },
          {
            "id": 15840661,
            "fixture_id": 19292987,
            "type_id": 48996,
            "participant_id": 54,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "2ND_HALF_ONLY"
          },
          {
            "id": 15840660,
            "fixture_id": 19292987,
            "type_id": 48996,
            "participant_id": 14,
            "score": {
              "goals": 4,
              "participant": "home"
            },
            "description": "2ND_HALF_ONLY"
          }
        ]
      }
    ],
    "rounds": []
  },
  {
    "id": 77475193,
    "sport_id": 1,
    "league_id": 2558,
    "season_id": 25008,
    "type_id": 224,
    "name": "Hybrid Friendlies 1",
    "sort_order": 4,
    "finished": true,
    "is_current": false,
    "starting_at": "2025-01-17",
    "ending_at": "2025-05-30",
    "games_in_current_week": false,
    "tie_breaker_rule_id": null,
    "fixtures": [
      {
        "id": 19413880,
        "sport_id": 1,
        "league_id": 2558,
        "season_id": 25008,
        "stage_id": 77475193,
        "group_id": null,
        "aggregate_id": null,
        "round_id": null,
        "state_id": 5,
        "venue_id": 13855,
        "name": "Hong Kong vs Manchester United",
        "starting_at": "2025-05-30 12:00:00",
        "result_info": "Manchester United won after full-time.",
        "leg": "1/1",
        "details": null,
        "length": 90,
        "placeholder": false,
        "has_odds": true,
        "has_premium_odds": true,
        "starting_at_timestamp": 1748606400,
        "participants": [
          {
            "id": 18134,
            "sport_id": 1,
            "country_id": 64306,
            "venue_id": 13845,
            "gender": "male",
            "name": "Hong Kong",
            "short_code": "HKG",
            "image_path": "https://cdn.sportmonks.com/images/soccer/teams/22/18134.png",
            "founded": 1886,
            "type": "national",
            "placeholder": false,
            "last_played_at": "2025-05-30 12:00:00",
            "meta": {
              "location": "home",
              "winner": false,
              "position": 1
            }
          },
          {
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
            "last_played_at": "2025-05-30 12:00:00",
            "meta": {
              "location": "away",
              "winner": true,
              "position": 2
            }
          }
        ],
        "scores": [
          {
            "id": 16569993,
            "fixture_id": 19413880,
            "type_id": 2,
            "participant_id": 18134,
            "score": {
              "goals": 1,
              "participant": "home"
            },
            "description": "2ND_HALF"
          },
          {
            "id": 16569990,
            "fixture_id": 19413880,
            "type_id": 1525,
            "participant_id": 14,
            "score": {
              "goals": 3,
              "participant": "away"
            },
            "description": "CURRENT"
          },
          {
            "id": 16569994,
            "fixture_id": 19413880,
            "type_id": 2,
            "participant_id": 14,
            "score": {
              "goals": 3,
              "participant": "away"
            },
            "description": "2ND_HALF"
          },
          {
            "id": 16569991,
            "fixture_id": 19413880,
            "type_id": 1,
            "participant_id": 18134,
            "score": {
              "goals": 1,
              "participant": "home"
            },
            "description": "1ST_HALF"
          },
          {
            "id": 16569992,
            "fixture_id": 19413880,
            "type_id": 1,
            "participant_id": 14,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "1ST_HALF"
          },
          {
            "id": 16569989,
            "fixture_id": 19413880,
            "type_id": 1525,
            "participant_id": 18134,
            "score": {
              "goals": 1,
              "participant": "home"
            },
            "description": "CURRENT"
          },
          {
            "id": 16570348,
            "fixture_id": 19413880,
            "type_id": 48996,
            "participant_id": 18134,
            "score": {
              "goals": 0,
              "participant": "home"
            },
            "description": "2ND_HALF_ONLY"
          },
          {
            "id": 16570349,
            "fixture_id": 19413880,
            "type_id": 48996,
            "participant_id": 14,
            "score": {
              "goals": 3,
              "participant": "away"
            },
            "description": "2ND_HALF_ONLY"
          }
        ]
      },
      {
        "id": 19413879,
        "sport_id": 1,
        "league_id": 2558,
        "season_id": 25008,
        "stage_id": 77475193,
        "group_id": null,
        "aggregate_id": null,
        "round_id": null,
        "state_id": 5,
        "venue_id": 14417,
        "name": "ASEAN All-Stars vs Manchester United",
        "starting_at": "2025-05-28 12:45:00",
        "result_info": "ASEAN All-Stars won after full-time.",
        "leg": "1/1",
        "details": null,
        "length": 90,
        "placeholder": false,
        "has_odds": true,
        "has_premium_odds": true,
        "starting_at_timestamp": 1748436300,
        "participants": [
          {
            "id": 276475,
            "sport_id": 1,
            "country_id": 99474,
            "venue_id": null,
            "gender": "male",
            "name": "ASEAN All-Stars",
            "short_code": null,
            "image_path": "https://cdn.sportmonks.com/images/soccer/teams/27/276475.png",
            "founded": null,
            "type": "domestic",
            "placeholder": false,
            "last_played_at": "2025-05-28 12:45:00",
            "meta": {
              "location": "home",
              "winner": true,
              "position": 1
            }
          },
          {
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
            "last_played_at": "2025-05-30 12:00:00",
            "meta": {
              "location": "away",
              "winner": false,
              "position": 2
            }
          }
        ],
        "scores": [
          {
            "id": 16565542,
            "fixture_id": 19413879,
            "type_id": 2,
            "participant_id": 14,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "2ND_HALF"
          },
          {
            "id": 16565540,
            "fixture_id": 19413879,
            "type_id": 1,
            "participant_id": 14,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "1ST_HALF"
          },
          {
            "id": 16565537,
            "fixture_id": 19413879,
            "type_id": 1525,
            "participant_id": 276475,
            "score": {
              "goals": 1,
              "participant": "home"
            },
            "description": "CURRENT"
          },
          {
            "id": 16565538,
            "fixture_id": 19413879,
            "type_id": 1525,
            "participant_id": 14,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "CURRENT"
          },
          {
            "id": 16565539,
            "fixture_id": 19413879,
            "type_id": 1,
            "participant_id": 276475,
            "score": {
              "goals": 0,
              "participant": "home"
            },
            "description": "1ST_HALF"
          },
          {
            "id": 16565541,
            "fixture_id": 19413879,
            "type_id": 2,
            "participant_id": 276475,
            "score": {
              "goals": 1,
              "participant": "home"
            },
            "description": "2ND_HALF"
          }
        ]
      }
    ],
    "rounds": []
  },
  {
    "id": 77474824,
    "sport_id": 1,
    "league_id": 1101,
    "season_id": 24894,
    "type_id": 224,
    "name": "Club Friendlies 1",
    "sort_order": 4,
    "finished": false,
    "is_current": true,
    "starting_at": "2025-01-05",
    "ending_at": "2025-08-09",
    "games_in_current_week": false,
    "tie_breaker_rule_id": null,
    "fixtures": [
      {
        "id": 19418347,
        "sport_id": 1,
        "league_id": 1101,
        "season_id": 24894,
        "stage_id": 77474824,
        "group_id": null,
        "aggregate_id": null,
        "round_id": null,
        "state_id": 1,
        "venue_id": 206,
        "name": "Manchester United vs Fiorentina",
        "starting_at": "2025-08-09 11:45:00",
        "result_info": null,
        "leg": "1/1",
        "details": null,
        "length": 90,
        "placeholder": false,
        "has_odds": false,
        "has_premium_odds": false,
        "starting_at_timestamp": 1754739900,
        "participants": [
          {
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
            "last_played_at": "2025-05-30 12:00:00",
            "meta": {
              "location": "home",
              "winner": null,
              "position": null
            }
          },
          {
            "id": 109,
            "sport_id": 1,
            "country_id": 251,
            "venue_id": 7223,
            "gender": "male",
            "name": "Fiorentina",
            "short_code": "FIO",
            "image_path": "https://cdn.sportmonks.com/images/soccer/teams/13/109.png",
            "founded": 1926,
            "type": "domestic",
            "placeholder": false,
            "last_played_at": "2025-05-25 18:45:00",
            "meta": {
              "location": "away",
              "winner": null,
              "position": null
            }
          }
        ],
        "scores": []
      },
      {
        "id": 19405079,
        "sport_id": 1,
        "league_id": 1101,
        "season_id": 24894,
        "stage_id": 77474824,
        "group_id": null,
        "aggregate_id": null,
        "round_id": null,
        "state_id": 1,
        "venue_id": 206,
        "name": "Manchester United vs Leeds United",
        "starting_at": "2025-07-19 13:00:00",
        "result_info": null,
        "leg": "1/1",
        "details": null,
        "length": 90,
        "placeholder": false,
        "has_odds": false,
        "has_premium_odds": false,
        "starting_at_timestamp": 1752930000,
        "participants": [
          {
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
            "last_played_at": "2025-05-30 12:00:00",
            "meta": {
              "location": "home",
              "winner": null,
              "position": null
            }
          },
          {
            "id": 71,
            "sport_id": 1,
            "country_id": 462,
            "venue_id": 488,
            "gender": "male",
            "name": "Leeds United",
            "short_code": "LEE",
            "image_path": "https://cdn.sportmonks.com/images/soccer/teams/7/71.png",
            "founded": 1919,
            "type": "domestic",
            "placeholder": false,
            "last_played_at": "2025-05-03 11:30:00",
            "meta": {
              "location": "away",
              "winner": null,
              "position": null
            }
          }
        ],
        "scores": []
      }
    ],
    "rounds": []
  },
  {
    "id": 77471555,
    "sport_id": 1,
    "league_id": 27,
    "season_id": 23685,
    "type_id": 224,
    "name": "Round of 16",
    "sort_order": 4,
    "finished": true,
    "is_current": false,
    "starting_at": "2024-10-29",
    "ending_at": "2024-10-30",
    "games_in_current_week": false,
    "tie_breaker_rule_id": null,
    "fixtures": [
      {
        "id": 19314297,
        "sport_id": 1,
        "league_id": 27,
        "season_id": 23685,
        "stage_id": 77471555,
        "group_id": null,
        "aggregate_id": null,
        "round_id": null,
        "state_id": 5,
        "venue_id": 206,
        "name": "Manchester United vs Leicester City",
        "starting_at": "2024-10-30 19:45:00",
        "result_info": "Manchester United won after full-time.",
        "leg": "1/1",
        "details": null,
        "length": 90,
        "placeholder": false,
        "has_odds": true,
        "has_premium_odds": true,
        "starting_at_timestamp": 1730317500,
        "participants": [
          {
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
            "last_played_at": "2025-05-25 15:00:00",
            "meta": {
              "location": "away",
              "winner": false,
              "position": 2
            }
          },
          {
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
            "last_played_at": "2025-05-30 12:00:00",
            "meta": {
              "location": "home",
              "winner": true,
              "position": 1
            }
          }
        ],
        "scores": [
          {
            "id": 15128513,
            "fixture_id": 19314297,
            "type_id": 1525,
            "participant_id": 14,
            "score": {
              "goals": 5,
              "participant": "home"
            },
            "description": "CURRENT"
          },
          {
            "id": 15128504,
            "fixture_id": 19314297,
            "type_id": 1,
            "participant_id": 14,
            "score": {
              "goals": 4,
              "participant": "home"
            },
            "description": "1ST_HALF"
          },
          {
            "id": 15128505,
            "fixture_id": 19314297,
            "type_id": 1,
            "participant_id": 42,
            "score": {
              "goals": 2,
              "participant": "away"
            },
            "description": "1ST_HALF"
          },
          {
            "id": 15128512,
            "fixture_id": 19314297,
            "type_id": 1525,
            "participant_id": 42,
            "score": {
              "goals": 2,
              "participant": "away"
            },
            "description": "CURRENT"
          },
          {
            "id": 15128860,
            "fixture_id": 19314297,
            "type_id": 2,
            "participant_id": 14,
            "score": {
              "goals": 5,
              "participant": "home"
            },
            "description": "2ND_HALF"
          },
          {
            "id": 15128861,
            "fixture_id": 19314297,
            "type_id": 2,
            "participant_id": 42,
            "score": {
              "goals": 2,
              "participant": "away"
            },
            "description": "2ND_HALF"
          },
          {
            "id": 15857958,
            "fixture_id": 19314297,
            "type_id": 48996,
            "participant_id": 42,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "2ND_HALF_ONLY"
          },
          {
            "id": 15857959,
            "fixture_id": 19314297,
            "type_id": 48996,
            "participant_id": 14,
            "score": {
              "goals": 1,
              "participant": "home"
            },
            "description": "2ND_HALF_ONLY"
          }
        ]
      }
    ],
    "rounds": []
  },
  {
    "id": 77471554,
    "sport_id": 1,
    "league_id": 27,
    "season_id": 23685,
    "type_id": 224,
    "name": "Quarter-finals",
    "sort_order": 5,
    "finished": true,
    "is_current": false,
    "starting_at": "2024-12-18",
    "ending_at": "2024-12-19",
    "games_in_current_week": false,
    "tie_breaker_rule_id": null,
    "fixtures": [
      {
        "id": 19325600,
        "sport_id": 1,
        "league_id": 27,
        "season_id": 23685,
        "stage_id": 77471554,
        "group_id": null,
        "aggregate_id": null,
        "round_id": null,
        "state_id": 5,
        "venue_id": 281313,
        "name": "Tottenham Hotspur vs Manchester United",
        "starting_at": "2024-12-19 20:00:00",
        "result_info": "Tottenham Hotspur won after full-time.",
        "leg": "1/1",
        "details": null,
        "length": 90,
        "placeholder": false,
        "has_odds": true,
        "has_premium_odds": true,
        "starting_at_timestamp": 1734638400,
        "participants": [
          {
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
            "last_played_at": "2025-05-25 15:00:00",
            "meta": {
              "location": "home",
              "winner": true,
              "position": 1
            }
          },
          {
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
            "last_played_at": "2025-05-30 12:00:00",
            "meta": {
              "location": "away",
              "winner": false,
              "position": 2
            }
          }
        ],
        "scores": [
          {
            "id": 15355836,
            "fixture_id": 19325600,
            "type_id": 1,
            "participant_id": 6,
            "score": {
              "goals": 1,
              "participant": "home"
            },
            "description": "1ST_HALF"
          },
          {
            "id": 15355834,
            "fixture_id": 19325600,
            "type_id": 1525,
            "participant_id": 6,
            "score": {
              "goals": 4,
              "participant": "home"
            },
            "description": "CURRENT"
          },
          {
            "id": 15355838,
            "fixture_id": 19325600,
            "type_id": 2,
            "participant_id": 6,
            "score": {
              "goals": 4,
              "participant": "home"
            },
            "description": "2ND_HALF"
          },
          {
            "id": 15355837,
            "fixture_id": 19325600,
            "type_id": 1,
            "participant_id": 14,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "1ST_HALF"
          },
          {
            "id": 15355839,
            "fixture_id": 19325600,
            "type_id": 2,
            "participant_id": 14,
            "score": {
              "goals": 3,
              "participant": "away"
            },
            "description": "2ND_HALF"
          },
          {
            "id": 15355905,
            "fixture_id": 19325600,
            "type_id": 1525,
            "participant_id": 14,
            "score": {
              "goals": 3,
              "participant": "away"
            },
            "description": "CURRENT"
          },
          {
            "id": 15867440,
            "fixture_id": 19325600,
            "type_id": 48996,
            "participant_id": 6,
            "score": {
              "goals": 3,
              "participant": "home"
            },
            "description": "2ND_HALF_ONLY"
          },
          {
            "id": 15867441,
            "fixture_id": 19325600,
            "type_id": 48996,
            "participant_id": 14,
            "score": {
              "goals": 3,
              "participant": "away"
            },
            "description": "2ND_HALF_ONLY"
          }
        ]
      }
    ],
    "rounds": []
  },
  {
    "id": 77471327,
    "sport_id": 1,
    "league_id": 5,
    "season_id": 23620,
    "type_id": 223,
    "name": "League Stage",
    "sort_order": 5,
    "finished": true,
    "is_current": false,
    "starting_at": "2024-09-25",
    "ending_at": "2025-01-30",
    "games_in_current_week": false,
    "tie_breaker_rule_id": null,
    "aggregates": [],
    "rounds": [
      {
        "id": 357253,
        "sport_id": 1,
        "league_id": 5,
        "season_id": 23620,
        "stage_id": 77471327,
        "name": "5",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-11-28",
        "ending_at": "2024-11-28",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19296452,
            "sport_id": 1,
            "league_id": 5,
            "season_id": 23620,
            "stage_id": 77471327,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 357253,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs Bodø / Glimt",
            "starting_at": "2024-11-28 20:00:00",
            "result_info": "Manchester United won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1732824000,
            "participants": [
              {
                "id": 1668,
                "sport_id": 1,
                "country_id": 1578,
                "venue_id": 814,
                "gender": "male",
                "name": "Bodø / Glimt",
                "short_code": null,
                "image_path": "https://cdn.sportmonks.com/images/soccer/teams/4/1668.png",
                "founded": 1916,
                "type": "domestic",
                "placeholder": false,
                "last_played_at": "2025-06-01 15:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 13
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 17
                }
              }
            ],
            "scores": [
              {
                "id": 15271601,
                "fixture_id": 19296452,
                "type_id": 1525,
                "participant_id": 1668,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15271598,
                "fixture_id": 19296452,
                "type_id": 1,
                "participant_id": 1668,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15271638,
                "fixture_id": 19296452,
                "type_id": 2,
                "participant_id": 1668,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15271599,
                "fixture_id": 19296452,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15271600,
                "fixture_id": 19296452,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15271639,
                "fixture_id": 19296452,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15843476,
                "fixture_id": 19296452,
                "type_id": 48996,
                "participant_id": 1668,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15843477,
                "fixture_id": 19296452,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      },
      {
        "id": 357261,
        "sport_id": 1,
        "league_id": 5,
        "season_id": 23620,
        "stage_id": 77471327,
        "name": "7",
        "finished": true,
        "is_current": false,
        "starting_at": "2025-01-21",
        "ending_at": "2025-01-23",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19296632,
            "sport_id": 1,
            "league_id": 5,
            "season_id": 23620,
            "stage_id": 77471327,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 357261,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs Rangers",
            "starting_at": "2025-01-23 20:00:00",
            "result_info": "Manchester United won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1737662400,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 10
                }
              },
              {
                "id": 62,
                "sport_id": 1,
                "country_id": 1161,
                "venue_id": 8914,
                "gender": "male",
                "name": "Rangers",
                "short_code": "RAN",
                "image_path": "https://cdn.sportmonks.com/images/soccer/teams/30/62.png",
                "founded": 1873,
                "type": "domestic",
                "placeholder": false,
                "last_played_at": "2025-05-17 11:30:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 13
                }
              }
            ],
            "scores": [
              {
                "id": 15441494,
                "fixture_id": 19296632,
                "type_id": 1525,
                "participant_id": 62,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15441498,
                "fixture_id": 19296632,
                "type_id": 2,
                "participant_id": 62,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15441497,
                "fixture_id": 19296632,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15441496,
                "fixture_id": 19296632,
                "type_id": 1,
                "participant_id": 62,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15441495,
                "fixture_id": 19296632,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15441499,
                "fixture_id": 19296632,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15441681,
                "fixture_id": 19296632,
                "type_id": 48996,
                "participant_id": 62,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15441680,
                "fixture_id": 19296632,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      },
      {
        "id": 357262,
        "sport_id": 1,
        "league_id": 5,
        "season_id": 23620,
        "stage_id": 77471327,
        "name": "8",
        "finished": true,
        "is_current": true,
        "starting_at": "2025-01-30",
        "ending_at": "2025-01-30",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19296641,
            "sport_id": 1,
            "league_id": 5,
            "season_id": 23620,
            "stage_id": 77471327,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 357262,
            "state_id": 5,
            "venue_id": 2010,
            "name": "FCSB vs Manchester United",
            "starting_at": "2025-01-30 20:00:00",
            "result_info": "Manchester United won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1738267200,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": true,
                  "position": 4
                }
              },
              {
                "id": 3444,
                "sport_id": 1,
                "country_id": 155,
                "venue_id": 2010,
                "gender": "male",
                "name": "FCSB",
                "short_code": null,
                "image_path": "https://cdn.sportmonks.com/images/soccer/teams/20/3444.png",
                "founded": 1947,
                "type": "domestic",
                "placeholder": false,
                "last_played_at": "2025-05-23 17:30:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 8
                }
              }
            ],
            "scores": [
              {
                "id": 15471445,
                "fixture_id": 19296641,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15471446,
                "fixture_id": 19296641,
                "type_id": 2,
                "participant_id": 3444,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15471443,
                "fixture_id": 19296641,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15471447,
                "fixture_id": 19296641,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15471444,
                "fixture_id": 19296641,
                "type_id": 1,
                "participant_id": 3444,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15471442,
                "fixture_id": 19296641,
                "type_id": 1525,
                "participant_id": 3444,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15471638,
                "fixture_id": 19296641,
                "type_id": 48996,
                "participant_id": 3444,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15471639,
                "fixture_id": 19296641,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      },
      {
        "id": 357260,
        "sport_id": 1,
        "league_id": 5,
        "season_id": 23620,
        "stage_id": 77471327,
        "name": "6",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-12-11",
        "ending_at": "2024-12-12",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19296608,
            "sport_id": 1,
            "league_id": 5,
            "season_id": 23620,
            "stage_id": 77471327,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 357260,
            "state_id": 5,
            "venue_id": 2067,
            "name": "Viktoria Plzeň vs Manchester United",
            "starting_at": "2024-12-12 17:45:00",
            "result_info": "Manchester United won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1734025500,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": true,
                  "position": 12
                }
              },
              {
                "id": 3545,
                "sport_id": 1,
                "country_id": 245,
                "venue_id": 2067,
                "gender": "male",
                "name": "Viktoria Plzeň",
                "short_code": "VPL",
                "image_path": "https://cdn.sportmonks.com/images/soccer/teams/25/3545.png",
                "founded": 1911,
                "type": "domestic",
                "placeholder": false,
                "last_played_at": "2025-05-24 14:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 13
                }
              }
            ],
            "scores": [
              {
                "id": 15331834,
                "fixture_id": 19296608,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15331827,
                "fixture_id": 19296608,
                "type_id": 1,
                "participant_id": 3545,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15331826,
                "fixture_id": 19296608,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15331951,
                "fixture_id": 19296608,
                "type_id": 2,
                "participant_id": 3545,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15331950,
                "fixture_id": 19296608,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15331835,
                "fixture_id": 19296608,
                "type_id": 1525,
                "participant_id": 3545,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15843789,
                "fixture_id": 19296608,
                "type_id": 48996,
                "participant_id": 3545,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15843788,
                "fixture_id": 19296608,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      },
      {
        "id": 357250,
        "sport_id": 1,
        "league_id": 5,
        "season_id": 23620,
        "stage_id": 77471327,
        "name": "2",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-10-03",
        "ending_at": "2024-10-03",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19296398,
            "sport_id": 1,
            "league_id": 5,
            "season_id": 23620,
            "stage_id": 77471327,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 357250,
            "state_id": 5,
            "venue_id": 165,
            "name": "Porto vs Manchester United",
            "starting_at": "2024-10-03 19:00:00",
            "result_info": "Game ended in draw.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1727982000,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 22
                }
              },
              {
                "id": 652,
                "sport_id": 1,
                "country_id": 20,
                "venue_id": 165,
                "gender": "male",
                "name": "Porto",
                "short_code": "POR",
                "image_path": "https://cdn.sportmonks.com/images/soccer/teams/12/652.png",
                "founded": 1893,
                "type": "domestic",
                "placeholder": false,
                "last_played_at": "2025-05-31 16:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 28
                }
              }
            ],
            "scores": [
              {
                "id": 14979093,
                "fixture_id": 19296398,
                "type_id": 1525,
                "participant_id": 652,
                "score": {
                  "goals": 3,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 14979091,
                "fixture_id": 19296398,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 14979092,
                "fixture_id": 19296398,
                "type_id": 1,
                "participant_id": 652,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 14979094,
                "fixture_id": 19296398,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 14979141,
                "fixture_id": 19296398,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 14979142,
                "fixture_id": 19296398,
                "type_id": 2,
                "participant_id": 652,
                "score": {
                  "goals": 3,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15843369,
                "fixture_id": 19296398,
                "type_id": 48996,
                "participant_id": 652,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15843368,
                "fixture_id": 19296398,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      },
      {
        "id": 357251,
        "sport_id": 1,
        "league_id": 5,
        "season_id": 23620,
        "stage_id": 77471327,
        "name": "3",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-10-23",
        "ending_at": "2024-10-24",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19296416,
            "sport_id": 1,
            "league_id": 5,
            "season_id": 23620,
            "stage_id": 77471327,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 357251,
            "state_id": 5,
            "venue_id": 9695,
            "name": "Fenerbahçe vs Manchester United",
            "starting_at": "2024-10-24 19:00:00",
            "result_info": "Game ended in draw.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1729796400,
            "participants": [
              {
                "id": 88,
                "sport_id": 1,
                "country_id": 404,
                "venue_id": 9695,
                "gender": "male",
                "name": "Fenerbahçe",
                "short_code": "FEN",
                "image_path": "https://cdn.sportmonks.com/images/soccer/teams/24/88.png",
                "founded": 1907,
                "type": "domestic",
                "placeholder": false,
                "last_played_at": "2025-05-31 13:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 14
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 25
                }
              }
            ],
            "scores": [
              {
                "id": 15091515,
                "fixture_id": 19296416,
                "type_id": 1,
                "participant_id": 88,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15091516,
                "fixture_id": 19296416,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15091519,
                "fixture_id": 19296416,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15091520,
                "fixture_id": 19296416,
                "type_id": 1525,
                "participant_id": 88,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15091557,
                "fixture_id": 19296416,
                "type_id": 2,
                "participant_id": 88,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15091558,
                "fixture_id": 19296416,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15843405,
                "fixture_id": 19296416,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15843404,
                "fixture_id": 19296416,
                "type_id": 48996,
                "participant_id": 88,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      },
      {
        "id": 357252,
        "sport_id": 1,
        "league_id": 5,
        "season_id": 23620,
        "stage_id": 77471327,
        "name": "4",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-11-06",
        "ending_at": "2024-11-07",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19296436,
            "sport_id": 1,
            "league_id": 5,
            "season_id": 23620,
            "stage_id": 77471327,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 357252,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs PAOK",
            "starting_at": "2024-11-07 20:00:00",
            "result_info": "Manchester United won after full-time.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1731009600,
            "participants": [
              {
                "id": 649,
                "sport_id": 1,
                "country_id": 125,
                "venue_id": 164,
                "gender": "male",
                "name": "PAOK",
                "short_code": null,
                "image_path": "https://cdn.sportmonks.com/images/soccer/teams/9/649.png",
                "founded": 1926,
                "type": "domestic",
                "placeholder": false,
                "last_played_at": "2025-05-11 17:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 32
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 24
                }
              }
            ],
            "scores": [
              {
                "id": 15168308,
                "fixture_id": 19296436,
                "type_id": 1,
                "participant_id": 649,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15168314,
                "fixture_id": 19296436,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 15168309,
                "fixture_id": 19296436,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 15168315,
                "fixture_id": 19296436,
                "type_id": 1525,
                "participant_id": 649,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 15168374,
                "fixture_id": 19296436,
                "type_id": 2,
                "participant_id": 649,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15168375,
                "fixture_id": 19296436,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15843444,
                "fixture_id": 19296436,
                "type_id": 48996,
                "participant_id": 649,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15843445,
                "fixture_id": 19296436,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      },
      {
        "id": 357249,
        "sport_id": 1,
        "league_id": 5,
        "season_id": 23620,
        "stage_id": 77471327,
        "name": "1",
        "finished": true,
        "is_current": false,
        "starting_at": "2024-09-25",
        "ending_at": "2024-09-26",
        "games_in_current_week": false,
        "fixtures": [
          {
            "id": 19296374,
            "sport_id": 1,
            "league_id": 5,
            "season_id": 23620,
            "stage_id": 77471327,
            "group_id": null,
            "aggregate_id": null,
            "round_id": 357249,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs FC Twente",
            "starting_at": "2024-09-25 19:00:00",
            "result_info": "Game ended in draw.",
            "leg": "1/1",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1727290800,
            "participants": [
              {
                "id": 593,
                "sport_id": 1,
                "country_id": 38,
                "venue_id": 132,
                "gender": "male",
                "name": "FC Twente",
                "short_code": "TWE",
                "image_path": "https://cdn.sportmonks.com/images/soccer/teams/17/593.png",
                "founded": 1965,
                "type": "domestic",
                "placeholder": false,
                "last_played_at": "2025-05-25 16:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 10
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 19
                }
              }
            ],
            "scores": [
              {
                "id": 14936871,
                "fixture_id": 19296374,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 14936867,
                "fixture_id": 19296374,
                "type_id": 1,
                "participant_id": 593,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 14936868,
                "fixture_id": 19296374,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 14936872,
                "fixture_id": 19296374,
                "type_id": 1525,
                "participant_id": 593,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 14937017,
                "fixture_id": 19296374,
                "type_id": 2,
                "participant_id": 593,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 14937018,
                "fixture_id": 19296374,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 15843320,
                "fixture_id": 19296374,
                "type_id": 48996,
                "participant_id": 593,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 15843321,
                "fixture_id": 19296374,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": 77471325,
    "sport_id": 1,
    "league_id": 5,
    "season_id": 23620,
    "type_id": 224,
    "name": "Round of 16",
    "sort_order": 7,
    "finished": true,
    "is_current": false,
    "starting_at": "2025-03-06",
    "ending_at": "2025-03-13",
    "games_in_current_week": false,
    "tie_breaker_rule_id": null,
    "aggregates": [
      {
        "id": 58610,
        "league_id": 5,
        "season_id": 23620,
        "stage_id": 77471325,
        "name": "Real Sociedad vs Manchester United",
        "fixture_ids": [
          19380921,
          19380922
        ],
        "result": "2-5",
        "detail": "After Full Time",
        "winner_participant_id": 14,
        "fixtures": [
          {
            "id": 19380921,
            "sport_id": 1,
            "league_id": 5,
            "season_id": 23620,
            "stage_id": 77471325,
            "group_id": null,
            "aggregate_id": 58610,
            "round_id": null,
            "state_id": 5,
            "venue_id": 133,
            "name": "Real Sociedad vs Manchester United",
            "starting_at": "2025-03-06 17:45:00",
            "result_info": "Game ended in draw.",
            "leg": "1/2",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1741283100,
            "participants": [
              {
                "id": 594,
                "sport_id": 1,
                "country_id": 32,
                "venue_id": 133,
                "gender": "male",
                "name": "Real Sociedad",
                "short_code": "RSO",
                "image_path": "https://cdn.sportmonks.com/images/soccer/teams/18/594.png",
                "founded": 1909,
                "type": "domestic",
                "placeholder": false,
                "last_played_at": "2025-05-24 14:15:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 1
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 2
                }
              }
            ],
            "scores": [
              {
                "id": 16012530,
                "fixture_id": 19380921,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16012532,
                "fixture_id": 19380921,
                "type_id": 2,
                "participant_id": 594,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16012528,
                "fixture_id": 19380921,
                "type_id": 1,
                "participant_id": 594,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16012533,
                "fixture_id": 19380921,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16012517,
                "fixture_id": 19380921,
                "type_id": 1525,
                "participant_id": 594,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 16012969,
                "fixture_id": 19380921,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16012968,
                "fixture_id": 19380921,
                "type_id": 48996,
                "participant_id": 594,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16012525,
                "fixture_id": 19380921,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "CURRENT"
              }
            ]
          },
          {
            "id": 19380922,
            "sport_id": 1,
            "league_id": 5,
            "season_id": 23620,
            "stage_id": 77471325,
            "group_id": null,
            "aggregate_id": 58610,
            "round_id": null,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs Real Sociedad",
            "starting_at": "2025-03-13 20:00:00",
            "result_info": "Manchester United won after full-time.",
            "leg": "2/2",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1741896000,
            "participants": [
              {
                "id": 594,
                "sport_id": 1,
                "country_id": 32,
                "venue_id": 133,
                "gender": "male",
                "name": "Real Sociedad",
                "short_code": "RSO",
                "image_path": "https://cdn.sportmonks.com/images/soccer/teams/18/594.png",
                "founded": 1909,
                "type": "domestic",
                "placeholder": false,
                "last_played_at": "2025-05-24 14:15:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 1
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 2
                }
              }
            ],
            "scores": [
              {
                "id": 16053656,
                "fixture_id": 19380922,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 4,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16053654,
                "fixture_id": 19380922,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16053648,
                "fixture_id": 19380922,
                "type_id": 1525,
                "participant_id": 594,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 16053652,
                "fixture_id": 19380922,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 4,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 16053655,
                "fixture_id": 19380922,
                "type_id": 2,
                "participant_id": 594,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16053653,
                "fixture_id": 19380922,
                "type_id": 1,
                "participant_id": 594,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16053897,
                "fixture_id": 19380922,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16053898,
                "fixture_id": 19380922,
                "type_id": 48996,
                "participant_id": 594,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      }
    ],
    "rounds": []
  },
  {
    "id": 77471324,
    "sport_id": 1,
    "league_id": 5,
    "season_id": 23620,
    "type_id": 224,
    "name": "Quarter-finals",
    "sort_order": 8,
    "finished": true,
    "is_current": false,
    "starting_at": "2025-04-10",
    "ending_at": "2025-04-17",
    "games_in_current_week": false,
    "tie_breaker_rule_id": null,
    "aggregates": [
      {
        "id": 58762,
        "league_id": 5,
        "season_id": 23620,
        "stage_id": 77471324,
        "name": "Olympique Lyonnais vs Manchester United",
        "fixture_ids": [
          19391333,
          19391334
        ],
        "result": "6-7",
        "detail": "After Extra Time",
        "winner_participant_id": 14,
        "fixtures": [
          {
            "id": 19391333,
            "sport_id": 1,
            "league_id": 5,
            "season_id": 23620,
            "stage_id": 77471324,
            "group_id": null,
            "aggregate_id": 58762,
            "round_id": null,
            "state_id": 5,
            "venue_id": 6161,
            "name": "Olympique Lyonnais vs Manchester United",
            "starting_at": "2025-04-10 19:00:00",
            "result_info": "Game ended in draw.",
            "leg": "1/2",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1744311600,
            "participants": [
              {
                "id": 79,
                "sport_id": 1,
                "country_id": 17,
                "venue_id": 6161,
                "gender": "male",
                "name": "Olympique Lyonnais",
                "short_code": "LYO",
                "image_path": "https://cdn.sportmonks.com/images/soccer/teams/15/79.png",
                "founded": 1950,
                "type": "domestic",
                "placeholder": false,
                "last_played_at": "2025-05-17 19:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 1
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 2
                }
              }
            ],
            "scores": [
              {
                "id": 16214095,
                "fixture_id": 19391333,
                "type_id": 1525,
                "participant_id": 79,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 16214098,
                "fixture_id": 19391333,
                "type_id": 1,
                "participant_id": 79,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16214100,
                "fixture_id": 19391333,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16214103,
                "fixture_id": 19391333,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16214096,
                "fixture_id": 19391333,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 16214102,
                "fixture_id": 19391333,
                "type_id": 2,
                "participant_id": 79,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16214424,
                "fixture_id": 19391333,
                "type_id": 48996,
                "participant_id": 79,
                "score": {
                  "goals": 1,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16214425,
                "fixture_id": 19391333,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          },
          {
            "id": 19391334,
            "sport_id": 1,
            "league_id": 5,
            "season_id": 23620,
            "stage_id": 77471324,
            "group_id": null,
            "aggregate_id": 58762,
            "round_id": null,
            "state_id": 7,
            "venue_id": 206,
            "name": "Manchester United vs Olympique Lyonnais",
            "starting_at": "2025-04-17 19:00:00",
            "result_info": "Manchester United won after extra-time.",
            "leg": "2/2",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1744916400,
            "participants": [
              {
                "id": 79,
                "sport_id": 1,
                "country_id": 17,
                "venue_id": 6161,
                "gender": "male",
                "name": "Olympique Lyonnais",
                "short_code": "LYO",
                "image_path": "https://cdn.sportmonks.com/images/soccer/teams/15/79.png",
                "founded": 1950,
                "type": "domestic",
                "placeholder": false,
                "last_played_at": "2025-05-17 19:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 1
                }
              },
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 2
                }
              }
            ],
            "scores": [
              {
                "id": 16261728,
                "fixture_id": 19391334,
                "type_id": 1525,
                "participant_id": 79,
                "score": {
                  "goals": 4,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 16261729,
                "fixture_id": 19391334,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 5,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 16261731,
                "fixture_id": 19391334,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16261730,
                "fixture_id": 19391334,
                "type_id": 1,
                "participant_id": 79,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16262029,
                "fixture_id": 19391334,
                "type_id": 48996,
                "participant_id": 79,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16262028,
                "fixture_id": 19391334,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16262306,
                "fixture_id": 19391334,
                "type_id": 39,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "home"
                },
                "description": "ET_2ND_HALF"
              },
              {
                "id": 16262294,
                "fixture_id": 19391334,
                "type_id": 3,
                "participant_id": 79,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "ET"
              },
              {
                "id": 16262295,
                "fixture_id": 19391334,
                "type_id": 3,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "home"
                },
                "description": "ET"
              },
              {
                "id": 16262302,
                "fixture_id": 19391334,
                "type_id": 5314,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "ET_1ST_HALF"
              },
              {
                "id": 16262307,
                "fixture_id": 19391334,
                "type_id": 39,
                "participant_id": 79,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "ET_2ND_HALF"
              },
              {
                "id": 16262303,
                "fixture_id": 19391334,
                "type_id": 5314,
                "participant_id": 79,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "ET_1ST_HALF"
              },
              {
                "id": 16261733,
                "fixture_id": 19391334,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 2,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16261732,
                "fixture_id": 19391334,
                "type_id": 2,
                "participant_id": 79,
                "score": {
                  "goals": 2,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              }
            ]
          }
        ]
      }
    ],
    "rounds": []
  },
  {
    "id": 77471323,
    "sport_id": 1,
    "league_id": 5,
    "season_id": 23620,
    "type_id": 224,
    "name": "Semi-finals",
    "sort_order": 9,
    "finished": true,
    "is_current": false,
    "starting_at": "2025-05-01",
    "ending_at": "2025-05-08",
    "games_in_current_week": false,
    "tie_breaker_rule_id": null,
    "aggregates": [
      {
        "id": 58758,
        "league_id": 5,
        "season_id": 23620,
        "stage_id": 77471323,
        "name": "Athletic Club vs Manchester United",
        "fixture_ids": [
          19391325,
          19391326
        ],
        "result": "1-7",
        "detail": "After Full Time",
        "winner_participant_id": 14,
        "fixtures": [
          {
            "id": 19391325,
            "sport_id": 1,
            "league_id": 5,
            "season_id": 23620,
            "stage_id": 77471323,
            "group_id": null,
            "aggregate_id": 58758,
            "round_id": null,
            "state_id": 5,
            "venue_id": 9162,
            "name": "Athletic Club vs Manchester United",
            "starting_at": "2025-05-01 19:00:00",
            "result_info": "Manchester United won after full-time.",
            "leg": "1/2",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1746126000,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "away",
                  "winner": true,
                  "position": 1
                }
              },
              {
                "id": 13258,
                "sport_id": 1,
                "country_id": 32,
                "venue_id": 9162,
                "gender": "male",
                "name": "Athletic Club",
                "short_code": "ATH",
                "image_path": "https://cdn.sportmonks.com/images/soccer/teams/10/13258.png",
                "founded": 1898,
                "type": "domestic",
                "placeholder": false,
                "last_played_at": "2025-05-25 19:00:00",
                "meta": {
                  "location": "home",
                  "winner": false,
                  "position": 2
                }
              }
            ],
            "scores": [
              {
                "id": 16339341,
                "fixture_id": 19391325,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16339340,
                "fixture_id": 19391325,
                "type_id": 1525,
                "participant_id": 13258,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 16339344,
                "fixture_id": 19391325,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16339711,
                "fixture_id": 19391325,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16339338,
                "fixture_id": 19391325,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 3,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 16339346,
                "fixture_id": 19391325,
                "type_id": 2,
                "participant_id": 13258,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16339710,
                "fixture_id": 19391325,
                "type_id": 48996,
                "participant_id": 13258,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16339343,
                "fixture_id": 19391325,
                "type_id": 1,
                "participant_id": 13258,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              }
            ]
          },
          {
            "id": 19391326,
            "sport_id": 1,
            "league_id": 5,
            "season_id": 23620,
            "stage_id": 77471323,
            "group_id": null,
            "aggregate_id": 58758,
            "round_id": null,
            "state_id": 5,
            "venue_id": 206,
            "name": "Manchester United vs Athletic Club",
            "starting_at": "2025-05-08 19:00:00",
            "result_info": "Manchester United won after full-time.",
            "leg": "2/2",
            "details": null,
            "length": 90,
            "placeholder": false,
            "has_odds": true,
            "has_premium_odds": true,
            "starting_at_timestamp": 1746730800,
            "participants": [
              {
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
                "last_played_at": "2025-05-30 12:00:00",
                "meta": {
                  "location": "home",
                  "winner": true,
                  "position": 1
                }
              },
              {
                "id": 13258,
                "sport_id": 1,
                "country_id": 32,
                "venue_id": 9162,
                "gender": "male",
                "name": "Athletic Club",
                "short_code": "ATH",
                "image_path": "https://cdn.sportmonks.com/images/soccer/teams/10/13258.png",
                "founded": 1898,
                "type": "domestic",
                "placeholder": false,
                "last_played_at": "2025-05-25 19:00:00",
                "meta": {
                  "location": "away",
                  "winner": false,
                  "position": 2
                }
              }
            ],
            "scores": [
              {
                "id": 16379998,
                "fixture_id": 19391326,
                "type_id": 1525,
                "participant_id": 14,
                "score": {
                  "goals": 4,
                  "participant": "home"
                },
                "description": "CURRENT"
              },
              {
                "id": 16380001,
                "fixture_id": 19391326,
                "type_id": 1,
                "participant_id": 13258,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16379999,
                "fixture_id": 19391326,
                "type_id": 1525,
                "participant_id": 13258,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "CURRENT"
              },
              {
                "id": 16380000,
                "fixture_id": 19391326,
                "type_id": 1,
                "participant_id": 14,
                "score": {
                  "goals": 0,
                  "participant": "home"
                },
                "description": "1ST_HALF"
              },
              {
                "id": 16380002,
                "fixture_id": 19391326,
                "type_id": 2,
                "participant_id": 14,
                "score": {
                  "goals": 4,
                  "participant": "home"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16380003,
                "fixture_id": 19391326,
                "type_id": 2,
                "participant_id": 13258,
                "score": {
                  "goals": 1,
                  "participant": "away"
                },
                "description": "2ND_HALF"
              },
              {
                "id": 16380246,
                "fixture_id": 19391326,
                "type_id": 48996,
                "participant_id": 14,
                "score": {
                  "goals": 4,
                  "participant": "home"
                },
                "description": "2ND_HALF_ONLY"
              },
              {
                "id": 16380247,
                "fixture_id": 19391326,
                "type_id": 48996,
                "participant_id": 13258,
                "score": {
                  "goals": 0,
                  "participant": "away"
                },
                "description": "2ND_HALF_ONLY"
              }
            ]
          }
        ]
      }
    ],
    "rounds": []
  },
  {
    "id": 77471322,
    "sport_id": 1,
    "league_id": 5,
    "season_id": 23620,
    "type_id": 224,
    "name": "Final",
    "sort_order": 10,
    "finished": true,
    "is_current": false,
    "starting_at": "2025-05-21",
    "ending_at": "2025-05-21",
    "games_in_current_week": false,
    "tie_breaker_rule_id": null,
    "fixtures": [
      {
        "id": 19391322,
        "sport_id": 1,
        "league_id": 5,
        "season_id": 23620,
        "stage_id": 77471322,
        "group_id": null,
        "aggregate_id": null,
        "round_id": null,
        "state_id": 5,
        "venue_id": 9162,
        "name": "Tottenham Hotspur vs Manchester United",
        "starting_at": "2025-05-21 19:00:00",
        "result_info": "Tottenham Hotspur won after full-time.",
        "leg": "1/1",
        "details": null,
        "length": 90,
        "placeholder": false,
        "has_odds": true,
        "has_premium_odds": true,
        "starting_at_timestamp": 1747854000,
        "participants": [
          {
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
            "last_played_at": "2025-05-25 15:00:00",
            "meta": {
              "location": "home",
              "winner": true,
              "position": 1
            }
          },
          {
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
            "last_played_at": "2025-05-30 12:00:00",
            "meta": {
              "location": "away",
              "winner": false,
              "position": 2
            }
          }
        ],
        "scores": [
          {
            "id": 16535343,
            "fixture_id": 19391322,
            "type_id": 2,
            "participant_id": 6,
            "score": {
              "goals": 1,
              "participant": "home"
            },
            "description": "2ND_HALF"
          },
          {
            "id": 16535344,
            "fixture_id": 19391322,
            "type_id": 2,
            "participant_id": 14,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "2ND_HALF"
          },
          {
            "id": 16535340,
            "fixture_id": 19391322,
            "type_id": 1525,
            "participant_id": 14,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "CURRENT"
          },
          {
            "id": 16535341,
            "fixture_id": 19391322,
            "type_id": 1,
            "participant_id": 6,
            "score": {
              "goals": 1,
              "participant": "home"
            },
            "description": "1ST_HALF"
          },
          {
            "id": 16535339,
            "fixture_id": 19391322,
            "type_id": 1525,
            "participant_id": 6,
            "score": {
              "goals": 1,
              "participant": "home"
            },
            "description": "CURRENT"
          },
          {
            "id": 16535342,
            "fixture_id": 19391322,
            "type_id": 1,
            "participant_id": 14,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "1ST_HALF"
          },
          {
            "id": 16535668,
            "fixture_id": 19391322,
            "type_id": 48996,
            "participant_id": 14,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "2ND_HALF_ONLY"
          },
          {
            "id": 16535667,
            "fixture_id": 19391322,
            "type_id": 48996,
            "participant_id": 6,
            "score": {
              "goals": 0,
              "participant": "home"
            },
            "description": "2ND_HALF_ONLY"
          }
        ]
      }
    ],
    "rounds": []
  },
  {
    "id": 77471891,
    "sport_id": 1,
    "league_id": 24,
    "season_id": 23787,
    "type_id": 224,
    "name": "3rd Round",
    "sort_order": 15,
    "finished": true,
    "is_current": false,
    "starting_at": "2025-01-09",
    "ending_at": "2025-01-14",
    "games_in_current_week": false,
    "tie_breaker_rule_id": null,
    "fixtures": [
      {
        "id": 19335065,
        "sport_id": 1,
        "league_id": 24,
        "season_id": 23787,
        "stage_id": 77471891,
        "group_id": null,
        "aggregate_id": null,
        "round_id": null,
        "state_id": 8,
        "venue_id": 204,
        "name": "Arsenal vs Manchester United",
        "starting_at": "2025-01-12 15:00:00",
        "result_info": "Manchester United won after penalties.",
        "leg": "1/1",
        "details": null,
        "length": 90,
        "placeholder": false,
        "has_odds": true,
        "has_premium_odds": true,
        "starting_at_timestamp": 1736694000,
        "participants": [
          {
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
            "last_played_at": "2025-05-25 15:00:00",
            "meta": {
              "location": "home",
              "winner": false,
              "position": 1
            }
          },
          {
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
            "last_played_at": "2025-05-30 12:00:00",
            "meta": {
              "location": "away",
              "winner": true,
              "position": 2
            }
          }
        ],
        "scores": [
          {
            "id": 15404627,
            "fixture_id": 19335065,
            "type_id": 1,
            "participant_id": 14,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "1ST_HALF"
          },
          {
            "id": 15404626,
            "fixture_id": 19335065,
            "type_id": 1,
            "participant_id": 19,
            "score": {
              "goals": 0,
              "participant": "home"
            },
            "description": "1ST_HALF"
          },
          {
            "id": 15404624,
            "fixture_id": 19335065,
            "type_id": 1525,
            "participant_id": 19,
            "score": {
              "goals": 1,
              "participant": "home"
            },
            "description": "CURRENT"
          },
          {
            "id": 15404629,
            "fixture_id": 19335065,
            "type_id": 2,
            "participant_id": 14,
            "score": {
              "goals": 1,
              "participant": "away"
            },
            "description": "2ND_HALF"
          },
          {
            "id": 15404628,
            "fixture_id": 19335065,
            "type_id": 2,
            "participant_id": 19,
            "score": {
              "goals": 1,
              "participant": "home"
            },
            "description": "2ND_HALF"
          },
          {
            "id": 15404625,
            "fixture_id": 19335065,
            "type_id": 1525,
            "participant_id": 14,
            "score": {
              "goals": 1,
              "participant": "away"
            },
            "description": "CURRENT"
          },
          {
            "id": 15406315,
            "fixture_id": 19335065,
            "type_id": 48996,
            "participant_id": 14,
            "score": {
              "goals": 1,
              "participant": "away"
            },
            "description": "2ND_HALF_ONLY"
          },
          {
            "id": 15406314,
            "fixture_id": 19335065,
            "type_id": 48996,
            "participant_id": 19,
            "score": {
              "goals": 1,
              "participant": "home"
            },
            "description": "2ND_HALF_ONLY"
          },
          {
            "id": 15406758,
            "fixture_id": 19335065,
            "type_id": 5,
            "participant_id": 19,
            "score": {
              "goals": 3,
              "participant": "home"
            },
            "description": "PENALTY_SHOOTOUT"
          },
          {
            "id": 15406759,
            "fixture_id": 19335065,
            "type_id": 5,
            "participant_id": 14,
            "score": {
              "goals": 5,
              "participant": "away"
            },
            "description": "PENALTY_SHOOTOUT"
          },
          {
            "id": 15406756,
            "fixture_id": 19335065,
            "type_id": 3,
            "participant_id": 19,
            "score": {
              "goals": 0,
              "participant": "home"
            },
            "description": "ET"
          },
          {
            "id": 15406757,
            "fixture_id": 19335065,
            "type_id": 3,
            "participant_id": 14,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "ET"
          }
        ]
      }
    ],
    "rounds": []
  },
  {
    "id": 77471890,
    "sport_id": 1,
    "league_id": 24,
    "season_id": 23787,
    "type_id": 224,
    "name": "4th Round",
    "sort_order": 16,
    "finished": true,
    "is_current": false,
    "starting_at": "2025-02-07",
    "ending_at": "2025-02-11",
    "games_in_current_week": false,
    "tie_breaker_rule_id": null,
    "fixtures": [
      {
        "id": 19368185,
        "sport_id": 1,
        "league_id": 24,
        "season_id": 23787,
        "stage_id": 77471890,
        "group_id": null,
        "aggregate_id": null,
        "round_id": null,
        "state_id": 5,
        "venue_id": 206,
        "name": "Manchester United vs Leicester City",
        "starting_at": "2025-02-07 20:00:00",
        "result_info": "Manchester United won after full-time.",
        "leg": "1/1",
        "details": null,
        "length": 90,
        "placeholder": false,
        "has_odds": true,
        "has_premium_odds": true,
        "starting_at_timestamp": 1738958400,
        "participants": [
          {
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
            "last_played_at": "2025-05-25 15:00:00",
            "meta": {
              "location": "away",
              "winner": false,
              "position": 2
            }
          },
          {
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
            "last_played_at": "2025-05-30 12:00:00",
            "meta": {
              "location": "home",
              "winner": true,
              "position": 1
            }
          }
        ],
        "scores": [
          {
            "id": 15879844,
            "fixture_id": 19368185,
            "type_id": 1,
            "participant_id": 14,
            "score": {
              "goals": 0,
              "participant": "home"
            },
            "description": "1ST_HALF"
          },
          {
            "id": 15879845,
            "fixture_id": 19368185,
            "type_id": 1,
            "participant_id": 42,
            "score": {
              "goals": 1,
              "participant": "away"
            },
            "description": "1ST_HALF"
          },
          {
            "id": 15879842,
            "fixture_id": 19368185,
            "type_id": 1525,
            "participant_id": 14,
            "score": {
              "goals": 2,
              "participant": "home"
            },
            "description": "CURRENT"
          },
          {
            "id": 15879843,
            "fixture_id": 19368185,
            "type_id": 1525,
            "participant_id": 42,
            "score": {
              "goals": 1,
              "participant": "away"
            },
            "description": "CURRENT"
          },
          {
            "id": 15879846,
            "fixture_id": 19368185,
            "type_id": 2,
            "participant_id": 14,
            "score": {
              "goals": 2,
              "participant": "home"
            },
            "description": "2ND_HALF"
          },
          {
            "id": 15880138,
            "fixture_id": 19368185,
            "type_id": 48996,
            "participant_id": 14,
            "score": {
              "goals": 2,
              "participant": "home"
            },
            "description": "2ND_HALF_ONLY"
          },
          {
            "id": 15880139,
            "fixture_id": 19368185,
            "type_id": 48996,
            "participant_id": 42,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "2ND_HALF_ONLY"
          },
          {
            "id": 15879847,
            "fixture_id": 19368185,
            "type_id": 2,
            "participant_id": 42,
            "score": {
              "goals": 1,
              "participant": "away"
            },
            "description": "2ND_HALF"
          }
        ]
      }
    ],
    "rounds": []
  },
  {
    "id": 77471889,
    "sport_id": 1,
    "league_id": 24,
    "season_id": 23787,
    "type_id": 224,
    "name": "5th Round",
    "sort_order": 17,
    "finished": true,
    "is_current": false,
    "starting_at": "2025-02-28",
    "ending_at": "2025-03-03",
    "games_in_current_week": false,
    "tie_breaker_rule_id": null,
    "fixtures": [
      {
        "id": 19385059,
        "sport_id": 1,
        "league_id": 24,
        "season_id": 23787,
        "stage_id": 77471889,
        "group_id": null,
        "aggregate_id": null,
        "round_id": null,
        "state_id": 8,
        "venue_id": 206,
        "name": "Manchester United vs Fulham",
        "starting_at": "2025-03-02 16:30:00",
        "result_info": "Fulham won after penalties.",
        "leg": "1/1",
        "details": null,
        "length": 90,
        "placeholder": false,
        "has_odds": true,
        "has_premium_odds": true,
        "starting_at_timestamp": 1740933000,
        "participants": [
          {
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
            "last_played_at": "2025-05-25 15:00:00",
            "meta": {
              "location": "away",
              "winner": true,
              "position": 2
            }
          },
          {
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
            "last_played_at": "2025-05-30 12:00:00",
            "meta": {
              "location": "home",
              "winner": false,
              "position": 1
            }
          }
        ],
        "scores": [
          {
            "id": 16003642,
            "fixture_id": 19385059,
            "type_id": 3,
            "participant_id": 11,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "ET"
          },
          {
            "id": 16003643,
            "fixture_id": 19385059,
            "type_id": 3,
            "participant_id": 14,
            "score": {
              "goals": 0,
              "participant": "home"
            },
            "description": "ET"
          },
          {
            "id": 16004405,
            "fixture_id": 19385059,
            "type_id": 5314,
            "participant_id": 11,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "ET_1ST_HALF"
          },
          {
            "id": 16002395,
            "fixture_id": 19385059,
            "type_id": 2,
            "participant_id": 14,
            "score": {
              "goals": 1,
              "participant": "home"
            },
            "description": "2ND_HALF"
          },
          {
            "id": 16004692,
            "fixture_id": 19385059,
            "type_id": 39,
            "participant_id": 14,
            "score": {
              "goals": 0,
              "participant": "home"
            },
            "description": "ET_2ND_HALF"
          },
          {
            "id": 16004693,
            "fixture_id": 19385059,
            "type_id": 39,
            "participant_id": 11,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "ET_2ND_HALF"
          },
          {
            "id": 16004729,
            "fixture_id": 19385059,
            "type_id": 5,
            "participant_id": 14,
            "score": {
              "goals": 3,
              "participant": "home"
            },
            "description": "PENALTY_SHOOTOUT"
          },
          {
            "id": 16004728,
            "fixture_id": 19385059,
            "type_id": 5,
            "participant_id": 11,
            "score": {
              "goals": 4,
              "participant": "away"
            },
            "description": "PENALTY_SHOOTOUT"
          },
          {
            "id": 16002392,
            "fixture_id": 19385059,
            "type_id": 1,
            "participant_id": 11,
            "score": {
              "goals": 1,
              "participant": "away"
            },
            "description": "1ST_HALF"
          },
          {
            "id": 16002390,
            "fixture_id": 19385059,
            "type_id": 1525,
            "participant_id": 11,
            "score": {
              "goals": 1,
              "participant": "away"
            },
            "description": "CURRENT"
          },
          {
            "id": 16002394,
            "fixture_id": 19385059,
            "type_id": 2,
            "participant_id": 11,
            "score": {
              "goals": 1,
              "participant": "away"
            },
            "description": "2ND_HALF"
          },
          {
            "id": 16002391,
            "fixture_id": 19385059,
            "type_id": 1525,
            "participant_id": 14,
            "score": {
              "goals": 1,
              "participant": "home"
            },
            "description": "CURRENT"
          },
          {
            "id": 16002393,
            "fixture_id": 19385059,
            "type_id": 1,
            "participant_id": 14,
            "score": {
              "goals": 0,
              "participant": "home"
            },
            "description": "1ST_HALF"
          },
          {
            "id": 16003401,
            "fixture_id": 19385059,
            "type_id": 48996,
            "participant_id": 11,
            "score": {
              "goals": 0,
              "participant": "away"
            },
            "description": "2ND_HALF_ONLY"
          },
          {
            "id": 16003400,
            "fixture_id": 19385059,
            "type_id": 48996,
            "participant_id": 14,
            "score": {
              "goals": 1,
              "participant": "home"
            },
            "description": "2ND_HALF_ONLY"
          },
          {
            "id": 16004404,
            "fixture_id": 19385059,
            "type_id": 5314,
            "participant_id": 14,
            "score": {
              "goals": 0,
              "participant": "home"
            },
            "description": "ET_1ST_HALF"
          }
        ]
      }
    ],
    "rounds": []
  }
]

    all_fixtures = []
    for schedule in response:
        rounds = schedule.get("rounds")

        if rounds and len(rounds) > 0:
            for round_item in rounds:
                fixtures = round_item.get("fixtures", [])
                all_fixtures.extend(fixtures)

        elif schedule.get("aggregates") and len(schedule["aggregates"]) > 0:
            aggregates = schedule["aggregates"]
            fixtures = aggregates[0].get("fixtures", [])
            all_fixtures.extend(fixtures)

        elif schedule.get("fixtures"):
            fixtures = schedule.get("fixtures", [])
            all_fixtures.extend(fixtures)

    # Ordena pelo starting_at
    all_fixtures.sort(key=lambda x: x["starting_at"])
    return JsonResponse(all_fixtures, safe=False)