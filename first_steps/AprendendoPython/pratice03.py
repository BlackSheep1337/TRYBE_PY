characters_file = open('favorite-characters.txt', mode='w')

characters_file.write('Batman\n')
characters_file.write('Homem Aranha\n')
characters_file.write('Homer Simpson\n')

print('Wolverine', file=characters_file)

more_characters = ['Flash\n', 'Homem Magnifico\n']

characters_file.writelines(more_characters)

characters_file.close()