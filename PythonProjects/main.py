import requests as re

url = 'https://api.pokemonbattle.ru/v2'
trainer_token = "2ec2b07c289e110ad7dbce758f769b18"
headers = {"Content-Type": "application/json","trainer_token": f"{trainer_token}"}
pokemon_id = "191231"
trainer_id = {"trainer_id":15119}

body_f_create_p = {
    "name": "Angelina",
    "photo_id": -1}

body_rename_p =  {
  "pokemon_id": f"{pokemon_id}",
  "name": "Newname",
  "photo_id": 1}

body_f_add_pokemon = {
  "pokemon_id": f"{pokemon_id}"}

"""Создаем покемона"""
resp_create_pokemon = re.post(url=f'{url}/pokemons',headers=headers,json=body_f_create_p)
print(resp_create_pokemon.status_code)
print(resp_create_pokemon.text)

"""Меняем имя покемона"""
resp_rename_pokemon = re.put(url=f'{url}/pokemons',headers=headers,json=body_rename_p)
print(resp_rename_pokemon.status_code)
print(resp_rename_pokemon.text)

"""Ловим покемона"""
resp_add_pokemon = re.post(url=f'{url}/trainers/add_pokeball',headers=headers,json=body_f_add_pokemon)
print(resp_add_pokemon.status_code)
print(resp_add_pokemon.text)