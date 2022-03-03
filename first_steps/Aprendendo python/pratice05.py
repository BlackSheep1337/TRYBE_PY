computers = open('computer_pieces.txt', mode='w')
pieces = ['Graphic card', 'Monitor', 'Keyboard', 'Mouse']
formated_pieces = []

for piece in pieces:
    formated_pieces.append(f'{piece}\n')

computers.writelines(formated_pieces)
computers.close()


computers_read = open('computer_pieces.txt', mode='r')
content = computers_read.read()
print(content)
computers_read.close()