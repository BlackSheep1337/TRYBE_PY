valores_naturais = input('Insira os valores aqui, separados por espaco: ')

valores_arr = valores_naturais.split(' ')

sum = 0

for valor in valores_arr:
    if not valor.isdigit():
        print(f'Erro aos somar os valores, {valor} nao eh um digito')
    else:
        sum += int(valor)
print(f'A soma dos valores eh {sum}')