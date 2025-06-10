import requests
from django.http import JsonResponse
from decouple import config  # Importa o método para carregar variáveis do .env

BASE_URL = 'https://api.sportmonks.com/v3/football'
API_KEY = config('MYSPORTMONKS_API')  # Carrega a chave do .env

def partidas_ao_vivo(request):
    """
    Endpoint para buscar partidas ao vivo na API MySportMonks.
    """
    # url = f"{BASE_URL}/fixtures/19135043?include=participants;league;venue;state;scores;events.type;events.period;events.player;statistics.type;sidelined.sideline.player;sidelined.sideline.type;weatherReport
    # params = {
    #     'api_token': API_KEY,
    # }
    # response = requests.get(url, params=params)
    null = None
    true = True
    false = False
    response = {
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
      "venue": {
        "id": 206,
        "country_id": 462,
        "city_id": 53964,
        "name": "Old Trafford",
        "address": "Sir Matt Busby Way",
        "zipcode": null,
        "latitude": "53.463056",
        "longitude": "-2.291389",
        "capacity": 74879,
        "image_path": "https://cdn.sportmonks.com/images/soccer/venues/14/206.png",
        "city_name": "Manchester",
        "surface": "grass",
        "national_team": false
      },
      "state": {
        "id": 5,
        "state": "FT",
        "name": "Full Time",
        "short_name": "FT",
        "developer_name": "FT"
      },
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
      ],
      "events": [
        {
          "id": 150478194,
          "fixture_id": 19135043,
          "period_id": 6092158,
          "participant_id": 15,
          "type_id": 20,
          "section": "event",
          "player_id": 1343,
          "related_player_id": null,
          "player_name": "Emiliano Martínez",
          "related_player_name": null,
          "result": null,
          "info": "Professional foul last man",
          "addition": "1st Redcard",
          "minute": 45,
          "extra_minute": 1,
          "injured": null,
          "on_bench": false,
          "coach_id": null,
          "sub_type_id": null,
          "detailed_period_id": 6092158,
          "sort_order": 1,
          "type": {
            "id": 20,
            "name": "Redcard",
            "code": "redcard",
            "developer_name": "REDCARD",
            "model_type": "event",
            "stat_group": null
          },
          "period": {
            "id": 6092158,
            "fixture_id": 19135043,
            "type_id": 1,
            "started": 1748185270,
            "ended": 1748188281,
            "counts_from": 0,
            "ticking": false,
            "sort_order": 1,
            "description": "1st-half",
            "time_added": 2,
            "period_length": 45,
            "minutes": 50,
            "seconds": 11,
            "has_timer": false
          },
          "player": {
            "id": 1343,
            "sport_id": 1,
            "country_id": 44,
            "nationality_id": 44,
            "city_id": 54370,
            "position_id": 24,
            "detailed_position_id": 24,
            "type_id": 24,
            "common_name": "D. Martínez",
            "firstname": "Damián Emiliano",
            "lastname": "Martínez",
            "name": "Damián Emiliano Martínez",
            "display_name": "Emiliano Martínez",
            "image_path": "https://cdn.sportmonks.com/images/soccer/players/31/1343.png",
            "height": 195,
            "weight": 88,
            "date_of_birth": "1992-09-02",
            "gender": "male"
          }
        },
        {
          "id": 150477385,
          "fixture_id": 19135043,
          "period_id": 6092158,
          "participant_id": 14,
          "type_id": 18,
          "section": "event",
          "player_id": 164061,
          "related_player_id": 28716,
          "player_name": "Diogo Dalot",
          "related_player_name": "Noussair Mazraoui",
          "result": null,
          "info": null,
          "addition": "1st Substitution",
          "minute": 20,
          "extra_minute": null,
          "injured": null,
          "on_bench": false,
          "coach_id": null,
          "sub_type_id": null,
          "detailed_period_id": 6092158,
          "sort_order": 1,
          "type": {
            "id": 18,
            "name": "Substitution",
            "code": "substitution",
            "developer_name": "SUBSTITUTION",
            "model_type": "event",
            "stat_group": null
          },
          "period": {
            "id": 6092158,
            "fixture_id": 19135043,
            "type_id": 1,
            "started": 1748185270,
            "ended": 1748188281,
            "counts_from": 0,
            "ticking": false,
            "sort_order": 1,
            "description": "1st-half",
            "time_added": 2,
            "period_length": 45,
            "minutes": 50,
            "seconds": 11,
            "has_timer": false
          },
          "player": {
            "id": 164061,
            "sport_id": 1,
            "country_id": 20,
            "nationality_id": 20,
            "city_id": 11564,
            "position_id": 25,
            "detailed_position_id": 154,
            "type_id": 25,
            "common_name": "J. Dalot Teixeira",
            "firstname": "José Diogo",
            "lastname": "Dalot Teixeira",
            "name": "José Diogo Dalot Teixeira",
            "display_name": "Diogo Dalot",
            "image_path": "https://cdn.sportmonks.com/images/soccer/players/29/164061.png",
            "height": 183,
            "weight": null,
            "date_of_birth": "1999-03-18",
            "gender": "male"
          }
        },
        {
          "id": 150478242,
          "fixture_id": 19135043,
          "period_id": 6092158,
          "participant_id": 15,
          "type_id": 18,
          "section": "event",
          "player_id": 84540,
          "related_player_id": 186668,
          "player_name": "Robin Olsen",
          "related_player_name": "Marco Asensio",
          "result": null,
          "info": null,
          "addition": "2nd Substitution",
          "minute": 45,
          "extra_minute": 4,
          "injured": null,
          "on_bench": false,
          "coach_id": null,
          "sub_type_id": null,
          "detailed_period_id": 6092158,
          "sort_order": 2,
          "type": {
            "id": 18,
            "name": "Substitution",
            "code": "substitution",
            "developer_name": "SUBSTITUTION",
            "model_type": "event",
            "stat_group": null
          },
          "period": {
            "id": 6092158,
            "fixture_id": 19135043,
            "type_id": 1,
            "started": 1748185270,
            "ended": 1748188281,
            "counts_from": 0,
            "ticking": false,
            "sort_order": 1,
            "description": "1st-half",
            "time_added": 2,
            "period_length": 45,
            "minutes": 50,
            "seconds": 11,
            "has_timer": false
          },
          "player": {
            "id": 84540,
            "sport_id": 1,
            "country_id": 47,
            "nationality_id": 47,
            "city_id": 53803,
            "position_id": 24,
            "detailed_position_id": 24,
            "type_id": 24,
            "common_name": "R. Olsen",
            "firstname": "Robin",
            "lastname": "Olsen",
            "name": "Robin Olsen",
            "display_name": "Robin Olsen",
            "image_path": "https://cdn.sportmonks.com/images/soccer/players/28/84540.png",
            "height": 196,
            "weight": 89,
            "date_of_birth": "1990-01-08",
            "gender": "male"
          }
        },
        {
          "id": 150478199,
          "fixture_id": 19135043,
          "period_id": 6092158,
          "participant_id": 14,
          "type_id": 19,
          "section": "event",
          "player_id": 37317015,
          "related_player_id": null,
          "player_name": "Amad",
          "related_player_name": null,
          "result": null,
          "info": "Argument",
          "addition": "1st Yellowcard",
          "minute": 45,
          "extra_minute": 1,
          "injured": null,
          "on_bench": false,
          "coach_id": null,
          "sub_type_id": null,
          "detailed_period_id": 6092158,
          "sort_order": 1,
          "type": {
            "id": 19,
            "name": "Yellowcard",
            "code": "yellowcard",
            "developer_name": "YELLOWCARD",
            "model_type": "event",
            "stat_group": null
          },
          "period": {
            "id": 6092158,
            "fixture_id": 19135043,
            "type_id": 1,
            "started": 1748185270,
            "ended": 1748188281,
            "counts_from": 0,
            "ticking": false,
            "sort_order": 1,
            "description": "1st-half",
            "time_added": 2,
            "period_length": 45,
            "minutes": 50,
            "seconds": 11,
            "has_timer": false
          },
          "player": {
            "id": 37317015,
            "sport_id": 1,
            "country_id": 23,
            "nationality_id": 23,
            "city_id": 202,
            "position_id": 27,
            "detailed_position_id": 156,
            "type_id": 27,
            "common_name": "A. Traoré",
            "firstname": "Amad Diallo",
            "lastname": "Traoré",
            "name": "Amad Diallo Traoré",
            "display_name": "Amad",
            "image_path": "https://cdn.sportmonks.com/images/soccer/players/23/37317015.png",
            "height": 173,
            "weight": null,
            "date_of_birth": "2002-07-11",
            "gender": "male"
          }
        },
        {
          "id": 150479300,
          "fixture_id": 19135043,
          "period_id": 6092418,
          "participant_id": 14,
          "type_id": 18,
          "section": "event",
          "player_id": 612,
          "related_player_id": 37676786,
          "player_name": "Jonny Evans",
          "related_player_name": "Ayden Heaven",
          "result": null,
          "info": null,
          "addition": "7th Substitution",
          "minute": 66,
          "extra_minute": null,
          "injured": null,
          "on_bench": false,
          "coach_id": null,
          "sub_type_id": null,
          "detailed_period_id": 6092418,
          "sort_order": 7,
          "type": {
            "id": 18,
            "name": "Substitution",
            "code": "substitution",
            "developer_name": "SUBSTITUTION",
            "model_type": "event",
            "stat_group": null
          },
          "period": {
            "id": 6092418,
            "fixture_id": 19135043,
            "type_id": 2,
            "started": 1748189257,
            "ended": 1748192461,
            "counts_from": 45,
            "ticking": false,
            "sort_order": 2,
            "description": "2nd-half",
            "time_added": 8,
            "period_length": 45,
            "minutes": 98,
            "seconds": 24,
            "has_timer": false
          },
          "player": {
            "id": 612,
            "sport_id": 1,
            "country_id": 491,
            "nationality_id": 491,
            "city_id": null,
            "position_id": 25,
            "detailed_position_id": 148,
            "type_id": 25,
            "common_name": "J. Evans",
            "firstname": "Jonny",
            "lastname": "Evans",
            "name": "Jonny Evans",
            "display_name": "Jonny Evans",
            "image_path": "https://cdn.sportmonks.com/images/soccer/players/4/612.png",
            "height": 188,
            "weight": 77,
            "date_of_birth": "1988-01-03",
            "gender": "male"
          }
        },
        {
          "id": 150479873,
          "fixture_id": 19135043,
          "period_id": 6092418,
          "participant_id": 15,
          "type_id": 19,
          "section": "event",
          "player_id": 4592198,
          "related_player_id": null,
          "player_name": "Morgan Rogers",
          "related_player_name": null,
          "result": null,
          "info": "Argument",
          "addition": "3rd Yellowcard",
          "minute": 80,
          "extra_minute": null,
          "injured": null,
          "on_bench": false,
          "coach_id": null,
          "sub_type_id": null,
          "detailed_period_id": 6092418,
          "sort_order": 3,
          "type": {
            "id": 19,
            "name": "Yellowcard",
            "code": "yellowcard",
            "developer_name": "YELLOWCARD",
            "model_type": "event",
            "stat_group": null
          },
          "period": {
            "id": 6092418,
            "fixture_id": 19135043,
            "type_id": 2,
            "started": 1748189257,
            "ended": 1748192461,
            "counts_from": 45,
            "ticking": false,
            "sort_order": 2,
            "description": "2nd-half",
            "time_added": 8,
            "period_length": 45,
            "minutes": 98,
            "seconds": 24,
            "has_timer": false
          },
          "player": {
            "id": 4592198,
            "sport_id": 1,
            "country_id": 462,
            "nationality_id": 462,
            "city_id": 35315,
            "position_id": 26,
            "detailed_position_id": 150,
            "type_id": 27,
            "common_name": "M. Rogers",
            "firstname": "Morgan",
            "lastname": "Rogers",
            "name": "Morgan Rogers",
            "display_name": "Morgan Rogers",
            "image_path": "https://cdn.sportmonks.com/images/soccer/players/6/4592198.png",
            "height": 187,
            "weight": null,
            "date_of_birth": "2002-07-26",
            "gender": "male"
          }
        },
        {
          "id": 150480017,
          "fixture_id": 19135043,
          "period_id": 6092418,
          "participant_id": 15,
          "type_id": 18,
          "section": "event",
          "player_id": 968,
          "related_player_id": 97626,
          "player_name": "Ross Barkley",
          "related_player_name": "Boubacar Kamara",
          "result": null,
          "info": null,
          "addition": "9th Substitution",
          "minute": 83,
          "extra_minute": null,
          "injured": null,
          "on_bench": false,
          "coach_id": null,
          "sub_type_id": null,
          "detailed_period_id": 6092418,
          "sort_order": 9,
          "type": {
            "id": 18,
            "name": "Substitution",
            "code": "substitution",
            "developer_name": "SUBSTITUTION",
            "model_type": "event",
            "stat_group": null
          },
          "period": {
            "id": 6092418,
            "fixture_id": 19135043,
            "type_id": 2,
            "started": 1748189257,
            "ended": 1748192461,
            "counts_from": 45,
            "ticking": false,
            "sort_order": 2,
            "description": "2nd-half",
            "time_added": 8,
            "period_length": 45,
            "minutes": 98,
            "seconds": 24,
            "has_timer": false
          },
          "player": {
            "id": 968,
            "sport_id": 1,
            "country_id": 462,
            "nationality_id": 462,
            "city_id": 51090,
            "position_id": 26,
            "detailed_position_id": 153,
            "type_id": 26,
            "common_name": "R. Barkley",
            "firstname": "Ross",
            "lastname": "Barkley",
            "name": "Ross Barkley",
            "display_name": "Ross Barkley",
            "image_path": "https://cdn.sportmonks.com/images/soccer/players/8/968.png",
            "height": 189,
            "weight": 76,
            "date_of_birth": "1993-12-05",
            "gender": "male"
          }
        },
        {
          "id": 150479148,
          "fixture_id": 19135043,
          "period_id": 6092418,
          "participant_id": 15,
          "type_id": 18,
          "section": "event",
          "player_id": 62342,
          "related_player_id": 172611,
          "player_name": "Youri Tielemans",
          "related_player_name": "John McGinn",
          "result": null,
          "info": null,
          "addition": "4th Substitution",
          "minute": 62,
          "extra_minute": null,
          "injured": null,
          "on_bench": false,
          "coach_id": null,
          "sub_type_id": null,
          "detailed_period_id": 6092418,
          "sort_order": 4,
          "type": {
            "id": 18,
            "name": "Substitution",
            "code": "substitution",
            "developer_name": "SUBSTITUTION",
            "model_type": "event",
            "stat_group": null
          },
          "period": {
            "id": 6092418,
            "fixture_id": 19135043,
            "type_id": 2,
            "started": 1748189257,
            "ended": 1748192461,
            "counts_from": 45,
            "ticking": false,
            "sort_order": 2,
            "description": "2nd-half",
            "time_added": 8,
            "period_length": 45,
            "minutes": 98,
            "seconds": 24,
            "has_timer": false
          },
          "player": {
            "id": 62342,
            "sport_id": 1,
            "country_id": 556,
            "nationality_id": 556,
            "city_id": 83763,
            "position_id": 26,
            "detailed_position_id": 153,
            "type_id": 26,
            "common_name": "Y. Tielemans",
            "firstname": "Youri",
            "lastname": "Tielemans",
            "name": "Youri Tielemans",
            "display_name": "Youri Tielemans",
            "image_path": "https://cdn.sportmonks.com/images/soccer/players/6/62342.png",
            "height": 177,
            "weight": 72,
            "date_of_birth": "1997-05-07",
            "gender": "male"
          }
        },
        {
          "id": 150479149,
          "fixture_id": 19135043,
          "period_id": 6092418,
          "participant_id": 15,
          "type_id": 18,
          "section": "event",
          "player_id": 11705406,
          "related_player_id": 22878573,
          "player_name": "Jacob Ramsey",
          "related_player_name": "Amadou Onana",
          "result": null,
          "info": null,
          "addition": "5th Substitution",
          "minute": 63,
          "extra_minute": null,
          "injured": null,
          "on_bench": false,
          "coach_id": null,
          "sub_type_id": null,
          "detailed_period_id": 6092418,
          "sort_order": 5,
          "type": {
            "id": 18,
            "name": "Substitution",
            "code": "substitution",
            "developer_name": "SUBSTITUTION",
            "model_type": "event",
            "stat_group": null
          },
          "period": {
            "id": 6092418,
            "fixture_id": 19135043,
            "type_id": 2,
            "started": 1748189257,
            "ended": 1748192461,
            "counts_from": 45,
            "ticking": false,
            "sort_order": 2,
            "description": "2nd-half",
            "time_added": 8,
            "period_length": 45,
            "minutes": 98,
            "seconds": 24,
            "has_timer": false
          },
          "player": {
            "id": 11705406,
            "sport_id": 1,
            "country_id": 462,
            "nationality_id": 462,
            "city_id": 9576,
            "position_id": 26,
            "detailed_position_id": 157,
            "type_id": 26,
            "common_name": "J. Ramsey",
            "firstname": "Jacob",
            "lastname": "Ramsey",
            "name": "Jacob Ramsey",
            "display_name": "Jacob Ramsey",
            "image_path": "https://cdn.sportmonks.com/images/soccer/players/30/11705406.png",
            "height": 180,
            "weight": null,
            "date_of_birth": "2001-05-28",
            "gender": "male"
          }
        },
        {
          "id": 150479573,
          "fixture_id": 19135043,
          "period_id": 6092418,
          "participant_id": 15,
          "type_id": 19,
          "section": "event",
          "player_id": 380970,
          "related_player_id": null,
          "player_name": "Pau Torres",
          "related_player_name": null,
          "result": null,
          "info": "Argument",
          "addition": "2nd Yellowcard",
          "minute": 73,
          "extra_minute": null,
          "injured": null,
          "on_bench": false,
          "coach_id": null,
          "sub_type_id": null,
          "detailed_period_id": 6092418,
          "sort_order": 2,
          "type": {
            "id": 19,
            "name": "Yellowcard",
            "code": "yellowcard",
            "developer_name": "YELLOWCARD",
            "model_type": "event",
            "stat_group": null
          },
          "period": {
            "id": 6092418,
            "fixture_id": 19135043,
            "type_id": 2,
            "started": 1748189257,
            "ended": 1748192461,
            "counts_from": 45,
            "ticking": false,
            "sort_order": 2,
            "description": "2nd-half",
            "time_added": 8,
            "period_length": 45,
            "minutes": 98,
            "seconds": 24,
            "has_timer": false
          },
          "player": {
            "id": 380970,
            "sport_id": 1,
            "country_id": 32,
            "nationality_id": 32,
            "city_id": 102447,
            "position_id": 25,
            "detailed_position_id": 148,
            "type_id": 25,
            "common_name": "P. Francisco Torres",
            "firstname": "Pau",
            "lastname": "Francisco Torres",
            "name": "Pau Francisco Torres",
            "display_name": "Pau Torres",
            "image_path": "https://cdn.sportmonks.com/images/soccer/players/10/380970.png",
            "height": 192,
            "weight": 81,
            "date_of_birth": "1997-01-16",
            "gender": "male"
          }
        },
        {
          "id": 150479702,
          "fixture_id": 19135043,
          "period_id": 6092418,
          "participant_id": 14,
          "type_id": 14,
          "section": "event",
          "player_id": 37317015,
          "related_player_id": 129602,
          "player_name": "Amad",
          "related_player_name": "Bruno Fernandes",
          "result": "1-0",
          "info": "Header",
          "addition": "1st Goal",
          "minute": 76,
          "extra_minute": null,
          "injured": null,
          "on_bench": false,
          "coach_id": null,
          "sub_type_id": 1694,
          "detailed_period_id": 6092418,
          "sort_order": 1,
          "type": {
            "id": 14,
            "name": "Goal",
            "code": "goal",
            "developer_name": "GOAL",
            "model_type": "event",
            "stat_group": null
          },
          "period": {
            "id": 6092418,
            "fixture_id": 19135043,
            "type_id": 2,
            "started": 1748189257,
            "ended": 1748192461,
            "counts_from": 45,
            "ticking": false,
            "sort_order": 2,
            "description": "2nd-half",
            "time_added": 8,
            "period_length": 45,
            "minutes": 98,
            "seconds": 24,
            "has_timer": false
          },
          "player": {
            "id": 37317015,
            "sport_id": 1,
            "country_id": 23,
            "nationality_id": 23,
            "city_id": 202,
            "position_id": 27,
            "detailed_position_id": 156,
            "type_id": 27,
            "common_name": "A. Traoré",
            "firstname": "Amad Diallo",
            "lastname": "Traoré",
            "name": "Amad Diallo Traoré",
            "display_name": "Amad",
            "image_path": "https://cdn.sportmonks.com/images/soccer/players/23/37317015.png",
            "height": 173,
            "weight": null,
            "date_of_birth": "2002-07-11",
            "gender": "male"
          }
        },
        {
          "id": 150478548,
          "fixture_id": 19135043,
          "period_id": 6092418,
          "participant_id": 14,
          "type_id": 18,
          "section": "event",
          "player_id": 37540234,
          "related_player_id": 164061,
          "player_name": "Kobbie Mainoo",
          "related_player_name": "Diogo Dalot",
          "result": null,
          "info": null,
          "addition": "3rd Substitution",
          "minute": 46,
          "extra_minute": null,
          "injured": null,
          "on_bench": false,
          "coach_id": null,
          "sub_type_id": null,
          "detailed_period_id": 6092418,
          "sort_order": 3,
          "type": {
            "id": 18,
            "name": "Substitution",
            "code": "substitution",
            "developer_name": "SUBSTITUTION",
            "model_type": "event",
            "stat_group": null
          },
          "period": {
            "id": 6092418,
            "fixture_id": 19135043,
            "type_id": 2,
            "started": 1748189257,
            "ended": 1748192461,
            "counts_from": 45,
            "ticking": false,
            "sort_order": 2,
            "description": "2nd-half",
            "time_added": 8,
            "period_length": 45,
            "minutes": 98,
            "seconds": 24,
            "has_timer": false
          },
          "player": {
            "id": 37540234,
            "sport_id": 1,
            "country_id": 462,
            "nationality_id": 462,
            "city_id": 86553,
            "position_id": 26,
            "detailed_position_id": 153,
            "type_id": 26,
            "common_name": "K. Mainoo",
            "firstname": "Kobbie",
            "lastname": "Mainoo",
            "name": "Kobbie Mainoo",
            "display_name": "Kobbie Mainoo",
            "image_path": "https://cdn.sportmonks.com/images/soccer/players/10/37540234.png",
            "height": 180,
            "weight": 70,
            "date_of_birth": "2005-04-19",
            "gender": "male"
          }
        },
        {
          "id": 150480044,
          "fixture_id": 19135043,
          "period_id": 6092418,
          "participant_id": 15,
          "type_id": 18,
          "section": "event",
          "player_id": 537758,
          "related_player_id": 4592198,
          "player_name": "Donyell Malen",
          "related_player_name": "Morgan Rogers",
          "result": null,
          "info": null,
          "addition": "10th Substitution",
          "minute": 84,
          "extra_minute": null,
          "injured": null,
          "on_bench": false,
          "coach_id": null,
          "sub_type_id": null,
          "detailed_period_id": 6092418,
          "sort_order": 10,
          "type": {
            "id": 18,
            "name": "Substitution",
            "code": "substitution",
            "developer_name": "SUBSTITUTION",
            "model_type": "event",
            "stat_group": null
          },
          "period": {
            "id": 6092418,
            "fixture_id": 19135043,
            "type_id": 2,
            "started": 1748189257,
            "ended": 1748192461,
            "counts_from": 45,
            "ticking": false,
            "sort_order": 2,
            "description": "2nd-half",
            "time_added": 8,
            "period_length": 45,
            "minutes": 98,
            "seconds": 24,
            "has_timer": false
          },
          "player": {
            "id": 537758,
            "sport_id": 1,
            "country_id": 38,
            "nationality_id": 38,
            "city_id": null,
            "position_id": 27,
            "detailed_position_id": 156,
            "type_id": 27,
            "common_name": "D. Malen",
            "firstname": "Donyell",
            "lastname": "Malen",
            "name": "Donyell Malen",
            "display_name": "Donyell Malen",
            "image_path": "https://cdn.sportmonks.com/images/soccer/players/30/537758.png",
            "height": 176,
            "weight": null,
            "date_of_birth": "1999-01-19",
            "gender": "male"
          }
        },
        {
          "id": 150479278,
          "fixture_id": 19135043,
          "period_id": 6092418,
          "participant_id": 14,
          "type_id": 18,
          "section": "event",
          "player_id": 992,
          "related_player_id": 537121,
          "player_name": "Christian Eriksen",
          "related_player_name": "Mason Mount",
          "result": null,
          "info": null,
          "addition": "6th Substitution",
          "minute": 66,
          "extra_minute": null,
          "injured": null,
          "on_bench": false,
          "coach_id": null,
          "sub_type_id": null,
          "detailed_period_id": 6092418,
          "sort_order": 6,
          "type": {
            "id": 18,
            "name": "Substitution",
            "code": "substitution",
            "developer_name": "SUBSTITUTION",
            "model_type": "event",
            "stat_group": null
          },
          "period": {
            "id": 6092418,
            "fixture_id": 19135043,
            "type_id": 2,
            "started": 1748189257,
            "ended": 1748192461,
            "counts_from": 45,
            "ticking": false,
            "sort_order": 2,
            "description": "2nd-half",
            "time_added": 8,
            "period_length": 45,
            "minutes": 98,
            "seconds": 24,
            "has_timer": false
          },
          "player": {
            "id": 992,
            "sport_id": 1,
            "country_id": 320,
            "nationality_id": 320,
            "city_id": 56926,
            "position_id": 26,
            "detailed_position_id": 153,
            "type_id": 26,
            "common_name": "C. Dannemann Eriksen",
            "firstname": "Christian",
            "lastname": "Dannemann Eriksen",
            "name": "Christian Dannemann Eriksen",
            "display_name": "Christian Eriksen",
            "image_path": "https://cdn.sportmonks.com/images/soccer/players/0/992.png",
            "height": 182,
            "weight": 71,
            "date_of_birth": "1992-02-14",
            "gender": "male"
          }
        },
        {
          "id": 150479926,
          "fixture_id": 19135043,
          "period_id": 6092418,
          "participant_id": 14,
          "type_id": 18,
          "section": "event",
          "player_id": 37723663,
          "related_player_id": 37325012,
          "player_name": "C. Obi",
          "related_player_name": "Rasmus Højlund",
          "result": null,
          "info": null,
          "addition": "8th Substitution",
          "minute": 81,
          "extra_minute": null,
          "injured": null,
          "on_bench": false,
          "coach_id": null,
          "sub_type_id": null,
          "detailed_period_id": 6092418,
          "sort_order": 8,
          "type": {
            "id": 18,
            "name": "Substitution",
            "code": "substitution",
            "developer_name": "SUBSTITUTION",
            "model_type": "event",
            "stat_group": null
          },
          "period": {
            "id": 6092418,
            "fixture_id": 19135043,
            "type_id": 2,
            "started": 1748189257,
            "ended": 1748192461,
            "counts_from": 45,
            "ticking": false,
            "sort_order": 2,
            "description": "2nd-half",
            "time_added": 8,
            "period_length": 45,
            "minutes": 98,
            "seconds": 24,
            "has_timer": false
          },
          "player": {
            "id": 37723663,
            "sport_id": 1,
            "country_id": 320,
            "nationality_id": 320,
            "city_id": 32427,
            "position_id": 27,
            "detailed_position_id": 151,
            "type_id": null,
            "common_name": "C. Obi-Martin",
            "firstname": "Chidozie",
            "lastname": "Obi-Martin",
            "name": "Chidozie Obi-Martin",
            "display_name": "C. Obi",
            "image_path": "https://cdn.sportmonks.com/images/soccer/placeholder.png",
            "height": null,
            "weight": null,
            "date_of_birth": "2007-11-29",
            "gender": "male"
          }
        },
        {
          "id": 150480200,
          "fixture_id": 19135043,
          "period_id": 6092418,
          "participant_id": 14,
          "type_id": 16,
          "section": "event",
          "player_id": 992,
          "related_player_id": null,
          "player_name": "Christian Eriksen",
          "related_player_name": null,
          "result": "2-0",
          "info": "Right foot shot",
          "addition": "1st Penalty",
          "minute": 87,
          "extra_minute": null,
          "injured": null,
          "on_bench": false,
          "coach_id": null,
          "sub_type_id": 1522,
          "detailed_period_id": 6092418,
          "sort_order": 2,
          "type": {
            "id": 16,
            "name": "Penalty",
            "code": "penalty",
            "developer_name": "PENALTY",
            "model_type": "event",
            "stat_group": null
          },
          "period": {
            "id": 6092418,
            "fixture_id": 19135043,
            "type_id": 2,
            "started": 1748189257,
            "ended": 1748192461,
            "counts_from": 45,
            "ticking": false,
            "sort_order": 2,
            "description": "2nd-half",
            "time_added": 8,
            "period_length": 45,
            "minutes": 98,
            "seconds": 24,
            "has_timer": false
          },
          "player": {
            "id": 992,
            "sport_id": 1,
            "country_id": 320,
            "nationality_id": 320,
            "city_id": 56926,
            "position_id": 26,
            "detailed_position_id": 153,
            "type_id": 26,
            "common_name": "C. Dannemann Eriksen",
            "firstname": "Christian",
            "lastname": "Dannemann Eriksen",
            "name": "Christian Dannemann Eriksen",
            "display_name": "Christian Eriksen",
            "image_path": "https://cdn.sportmonks.com/images/soccer/players/0/992.png",
            "height": 182,
            "weight": 71,
            "date_of_birth": "1992-02-14",
            "gender": "male"
          }
        },
        {
          "id": 150480422,
          "fixture_id": 19135043,
          "period_id": 6092418,
          "participant_id": 14,
          "type_id": 19,
          "section": "event",
          "player_id": 159700,
          "related_player_id": null,
          "player_name": "Casemiro",
          "related_player_name": null,
          "result": null,
          "info": "Foul",
          "addition": "4th Yellowcard",
          "minute": 90,
          "extra_minute": 4,
          "injured": null,
          "on_bench": false,
          "coach_id": null,
          "sub_type_id": null,
          "detailed_period_id": 6092418,
          "sort_order": 4,
          "type": {
            "id": 19,
            "name": "Yellowcard",
            "code": "yellowcard",
            "developer_name": "YELLOWCARD",
            "model_type": "event",
            "stat_group": null
          },
          "period": {
            "id": 6092418,
            "fixture_id": 19135043,
            "type_id": 2,
            "started": 1748189257,
            "ended": 1748192461,
            "counts_from": 45,
            "ticking": false,
            "sort_order": 2,
            "description": "2nd-half",
            "time_added": 8,
            "period_length": 45,
            "minutes": 98,
            "seconds": 24,
            "has_timer": false
          },
          "player": {
            "id": 159700,
            "sport_id": 1,
            "country_id": 5,
            "nationality_id": 5,
            "city_id": 80255,
            "position_id": 26,
            "detailed_position_id": 149,
            "type_id": 26,
            "common_name": "C. Casimiro",
            "firstname": "Carlos Henrique",
            "lastname": "Casimiro",
            "name": "Carlos Henrique Casimiro",
            "display_name": "Casemiro",
            "image_path": "https://cdn.sportmonks.com/images/soccer/players/20/159700.png",
            "height": 185,
            "weight": 84,
            "date_of_birth": "1992-02-23",
            "gender": "male"
          }
        }
      ],
      "statistics": [
        {
          "id": 413118283,
          "fixture_id": 19135043,
          "type_id": 59,
          "participant_id": 14,
          "data": {
            "value": 5
          },
          "location": "home",
          "type": {
            "id": 59,
            "name": "Substitutions",
            "code": "substitutions",
            "developer_name": "SUBSTITUTIONS",
            "model_type": "statistic",
            "stat_group": "overall"
          }
        },
        {
          "id": 413122100,
          "fixture_id": 19135043,
          "type_id": 51,
          "participant_id": 15,
          "data": {
            "value": 3
          },
          "location": "away",
          "type": {
            "id": 51,
            "name": "Offsides",
            "code": "offsides",
            "developer_name": "OFFSIDES",
            "model_type": "statistic",
            "stat_group": "offensive"
          }
        },
        {
          "id": 413122099,
          "fixture_id": 19135043,
          "type_id": 51,
          "participant_id": 14,
          "data": {
            "value": 5
          },
          "location": "home",
          "type": {
            "id": 51,
            "name": "Offsides",
            "code": "offsides",
            "developer_name": "OFFSIDES",
            "model_type": "statistic",
            "stat_group": "offensive"
          }
        },
        {
          "id": 413045857,
          "fixture_id": 19135043,
          "type_id": 45,
          "participant_id": 14,
          "data": {
            "value": 67
          },
          "location": "home",
          "type": {
            "id": 45,
            "name": "Ball Possession %",
            "code": "ball-possession",
            "developer_name": "BALL_POSSESSION",
            "model_type": "statistic",
            "stat_group": "overall"
          }
        },
        {
          "id": 413062065,
          "fixture_id": 19135043,
          "type_id": 80,
          "participant_id": 14,
          "data": {
            "value": 606
          },
          "location": "home",
          "type": {
            "id": 80,
            "name": "Passes",
            "code": "passes",
            "developer_name": "PASSES",
            "model_type": "statistic",
            "stat_group": "overall"
          }
        },
        {
          "id": 413045858,
          "fixture_id": 19135043,
          "type_id": 45,
          "participant_id": 15,
          "data": {
            "value": 33
          },
          "location": "away",
          "type": {
            "id": 45,
            "name": "Ball Possession %",
            "code": "ball-possession",
            "developer_name": "BALL_POSSESSION",
            "model_type": "statistic",
            "stat_group": "overall"
          }
        },
        {
          "id": 413064614,
          "fixture_id": 19135043,
          "type_id": 42,
          "participant_id": 15,
          "data": {
            "value": 6
          },
          "location": "away",
          "type": {
            "id": 42,
            "name": "Shots Total",
            "code": "shots-total",
            "developer_name": "SHOTS_TOTAL",
            "model_type": "statistic",
            "stat_group": "offensive"
          }
        },
        {
          "id": 413063843,
          "fixture_id": 19135043,
          "type_id": 56,
          "participant_id": 14,
          "data": {
            "value": 10
          },
          "location": "home",
          "type": {
            "id": 56,
            "name": "Fouls",
            "code": "fouls",
            "developer_name": "FOULS",
            "model_type": "statistic",
            "stat_group": "defensive"
          }
        },
        {
          "id": 413063844,
          "fixture_id": 19135043,
          "type_id": 56,
          "participant_id": 15,
          "data": {
            "value": 10
          },
          "location": "away",
          "type": {
            "id": 56,
            "name": "Fouls",
            "code": "fouls",
            "developer_name": "FOULS",
            "model_type": "statistic",
            "stat_group": "defensive"
          }
        },
        {
          "id": 413063845,
          "fixture_id": 19135043,
          "type_id": 57,
          "participant_id": 14,
          "data": {
            "value": 1
          },
          "location": "home",
          "type": {
            "id": 57,
            "name": "Saves",
            "code": "saves",
            "developer_name": "SAVES",
            "model_type": "statistic",
            "stat_group": "defensive"
          }
        },
        {
          "id": 413063846,
          "fixture_id": 19135043,
          "type_id": 57,
          "participant_id": 15,
          "data": {
            "value": 8
          },
          "location": "away",
          "type": {
            "id": 57,
            "name": "Saves",
            "code": "saves",
            "developer_name": "SAVES",
            "model_type": "statistic",
            "stat_group": "defensive"
          }
        },
        {
          "id": 413064613,
          "fixture_id": 19135043,
          "type_id": 42,
          "participant_id": 14,
          "data": {
            "value": 26
          },
          "location": "home",
          "type": {
            "id": 42,
            "name": "Shots Total",
            "code": "shots-total",
            "developer_name": "SHOTS_TOTAL",
            "model_type": "statistic",
            "stat_group": "offensive"
          }
        },
        {
          "id": 413064608,
          "fixture_id": 19135043,
          "type_id": 86,
          "participant_id": 15,
          "data": {
            "value": 1
          },
          "location": "away",
          "type": {
            "id": 86,
            "name": "Shots On Target",
            "code": "shots-on-target",
            "developer_name": "SHOTS_ON_TARGET",
            "model_type": "statistic",
            "stat_group": "offensive"
          }
        },
        {
          "id": 413062064,
          "fixture_id": 19135043,
          "type_id": 81,
          "participant_id": 15,
          "data": {
            "value": 217
          },
          "location": "away",
          "type": {
            "id": 81,
            "name": "Successful Passes",
            "code": "successful-passes",
            "developer_name": "SUCCESSFUL_PASSES",
            "model_type": "statistic",
            "stat_group": "overall"
          }
        },
        {
          "id": 413064607,
          "fixture_id": 19135043,
          "type_id": 86,
          "participant_id": 14,
          "data": {
            "value": 10
          },
          "location": "home",
          "type": {
            "id": 86,
            "name": "Shots On Target",
            "code": "shots-on-target",
            "developer_name": "SHOTS_ON_TARGET",
            "model_type": "statistic",
            "stat_group": "offensive"
          }
        },
        {
          "id": 413171741,
          "fixture_id": 19135043,
          "type_id": 34,
          "participant_id": 14,
          "data": {
            "value": 4
          },
          "location": "home",
          "type": {
            "id": 34,
            "name": "Corners",
            "code": "corners",
            "developer_name": "CORNERS",
            "model_type": "statistic",
            "stat_group": "offensive"
          }
        },
        {
          "id": 413171742,
          "fixture_id": 19135043,
          "type_id": 34,
          "participant_id": 15,
          "data": {
            "value": 3
          },
          "location": "away",
          "type": {
            "id": 34,
            "name": "Corners",
            "code": "corners",
            "developer_name": "CORNERS",
            "model_type": "statistic",
            "stat_group": "offensive"
          }
        },
        {
          "id": 413234070,
          "fixture_id": 19135043,
          "type_id": 83,
          "participant_id": 15,
          "data": {
            "value": 1
          },
          "location": "away",
          "type": {
            "id": 83,
            "name": "Redcards",
            "code": "redcards",
            "developer_name": "REDCARDS",
            "model_type": "statistic",
            "stat_group": "overall"
          }
        },
        {
          "id": 413237678,
          "fixture_id": 19135043,
          "type_id": 84,
          "participant_id": 15,
          "data": {
            "value": 2
          },
          "location": "away",
          "type": {
            "id": 84,
            "name": "Yellowcards",
            "code": "yellowcards",
            "developer_name": "YELLOWCARDS",
            "model_type": "statistic",
            "stat_group": "overall"
          }
        },
        {
          "id": 413234069,
          "fixture_id": 19135043,
          "type_id": 83,
          "participant_id": 14,
          "data": {
            "value": 0
          },
          "location": "home",
          "type": {
            "id": 83,
            "name": "Redcards",
            "code": "redcards",
            "developer_name": "REDCARDS",
            "model_type": "statistic",
            "stat_group": "overall"
          }
        },
        {
          "id": 413237677,
          "fixture_id": 19135043,
          "type_id": 84,
          "participant_id": 14,
          "data": {
            "value": 2
          },
          "location": "home",
          "type": {
            "id": 84,
            "name": "Yellowcards",
            "code": "yellowcards",
            "developer_name": "YELLOWCARDS",
            "model_type": "statistic",
            "stat_group": "overall"
          }
        },
        {
          "id": 413118284,
          "fixture_id": 19135043,
          "type_id": 59,
          "participant_id": 15,
          "data": {
            "value": 5
          },
          "location": "away",
          "type": {
            "id": 59,
            "name": "Substitutions",
            "code": "substitutions",
            "developer_name": "SUBSTITUTIONS",
            "model_type": "statistic",
            "stat_group": "overall"
          }
        },
        {
          "id": 413062063,
          "fixture_id": 19135043,
          "type_id": 81,
          "participant_id": 14,
          "data": {
            "value": 535
          },
          "location": "home",
          "type": {
            "id": 81,
            "name": "Successful Passes",
            "code": "successful-passes",
            "developer_name": "SUCCESSFUL_PASSES",
            "model_type": "statistic",
            "stat_group": "overall"
          }
        },
        {
          "id": 413062066,
          "fixture_id": 19135043,
          "type_id": 80,
          "participant_id": 15,
          "data": {
            "value": 300
          },
          "location": "away",
          "type": {
            "id": 80,
            "name": "Passes",
            "code": "passes",
            "developer_name": "PASSES",
            "model_type": "statistic",
            "stat_group": "overall"
          }
        }
      ],
      "sidelined": [
        {
          "id": 1153238,
          "fixture_id": 19135043,
          "sideline_id": 697635,
          "participant_id": 14,
          "sideline": {
            "id": 697635,
            "player_id": 2206665,
            "type_id": 557,
            "category": "injury",
            "team_id": 14,
            "season_id": null,
            "start_date": "2025-02-03",
            "end_date": "2026-01-01",
            "games_missed": 25,
            "completed": false,
            "player": {
              "id": 2206665,
              "sport_id": 1,
              "country_id": 44,
              "nationality_id": 44,
              "city_id": 34421,
              "position_id": 25,
              "detailed_position_id": 148,
              "type_id": 25,
              "common_name": "L. Martínez",
              "firstname": "Lisandro",
              "lastname": "Martínez",
              "name": "Lisandro Martínez",
              "display_name": "Lisandro Martínez",
              "image_path": "https://cdn.sportmonks.com/images/soccer/players/9/2206665.png",
              "height": 175,
              "weight": 77,
              "date_of_birth": "1998-01-18",
              "gender": "male"
            },
            "type": {
              "id": 557,
              "name": "Cruciate Ligament Injury",
              "code": "cruciate-ligament-injury",
              "developer_name": "CRUCIATE_LIGAMENT_INJURY",
              "model_type": "injury_suspension",
              "stat_group": null
            }
          }
        },
        {
          "id": 1153239,
          "fixture_id": 19135043,
          "sideline_id": 717447,
          "participant_id": 14,
          "sideline": {
            "id": 717447,
            "player_id": 9605680,
            "type_id": 533,
            "category": "injury",
            "team_id": 14,
            "season_id": null,
            "start_date": "2025-04-14",
            "end_date": "2025-06-01",
            "games_missed": 12,
            "completed": true,
            "player": {
              "id": 9605680,
              "sport_id": 1,
              "country_id": 38,
              "nationality_id": 38,
              "city_id": 80977,
              "position_id": 27,
              "detailed_position_id": 151,
              "type_id": 27,
              "common_name": "J. Zirkzee",
              "firstname": "Joshua",
              "lastname": "Zirkzee",
              "name": "Joshua Zirkzee",
              "display_name": "Joshua Zirkzee",
              "image_path": "https://cdn.sportmonks.com/images/soccer/players/16/9605680.png",
              "height": 193,
              "weight": null,
              "date_of_birth": "2001-05-22",
              "gender": "male"
            },
            "type": {
              "id": 533,
              "name": "Thigh Problems",
              "code": "thigh-problems",
              "developer_name": "THIGH_PROBLEMS",
              "model_type": "injury_suspension",
              "stat_group": null
            }
          }
        }
      ],
      "weatherreport": {
        "id": 610207,
        "fixture_id": 19135043,
        "venue_id": 206,
        "temperature": {
          "day": 15.36,
          "morning": 11.4,
          "evening": 11.94,
          "night": 8.97
        },
        "feels_like": {
          "day": 14.1,
          "morning": 10.87,
          "evening": 11.25,
          "night": 6.49
        },
        "wind": {
          "speed": 8.02,
          "direction": 269
        },
        "humidity": "44%",
        "pressure": 1008,
        "clouds": "36%",
        "description": "light rain",
        "icon": "https://cdn.sportmonks.com/images/weather/10d.png",
        "type": "forecast",
        "metric": "celcius",
        "current": null
      }
    }
    
    # if response.status_code == 200:
    #     data = response.json()  # Retorna os dados da API     
    return JsonResponse(response, safe=False)
    # else:
    #     return JsonResponse({'error': 'Erro ao buscar dados da API'}, status=response.status_code)
