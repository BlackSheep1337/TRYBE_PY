cars = open('nice_cars.txt', mode='w')

nice_cars = ['Lamborguine', 'BMW', 'WOLSHWAGEN', 'MITSUBSH']
old_cars = ['Opala\n', 'Fusca\n', 'Dodge\n', 'Gol Quadrado\n']

line_stroke = []

for car in nice_cars:
    line_stroke.append(f'{car}\n')

cars.writelines(line_stroke)

print(old_cars, file=cars)

cars.close()