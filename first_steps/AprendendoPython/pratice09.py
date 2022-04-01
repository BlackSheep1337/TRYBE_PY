import json

with open('pokemons.json') as pokemon_list:
    pokemons = json.load(pokemon_list)['results']

print(pokemons[0])