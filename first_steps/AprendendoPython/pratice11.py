from json import dump, load

with open('pokemons.json') as file:
    pokemons = load(file)['results']

grass_type = [
    pokemon for pokemon in pokemons if 'Grass' in pokemon['type']
]

with open('grass_pokemons.json', 'w') as file:
    dump(grass_type, file)
