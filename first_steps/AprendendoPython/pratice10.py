from json import load, dumps

with open('pokemons.json') as file:
    pokemons = load(file)['results']

grass_type = [
    pokemon for pokemon in pokemons if 'Grass' in pokemon['type']
]

with open('grass_pokemons.json', 'w') as file:
    grass_pokemons = dumps(
        grass_type
    )
    file.write(grass_pokemons)

