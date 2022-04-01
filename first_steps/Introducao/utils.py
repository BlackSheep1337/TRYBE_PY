def biggerInterager(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def arithmetic_median(arr):
    return sum(arr) / len(arr)

def star_game(n):
    if n <= 1:
        print('O numero precisa ser maior que 1')
    else:
        for row in range(n):
            print(n * '*')

def larger_name(names):
    largest_name = names[0]
    for name in names:
        if len(name) > len(largest_name):
            largest_name = name
    return largest_name

def paint_cost(area):
    can_price = 80
    required_litters = area / 3
    require_cans = required_litters // 18
    if required_litters % 18:
        require_cans += 1
    return require_cans, require_cans * can_price

def type_of_triangle(side1, side2, side3):
    is_triangle = (side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2);
    if not is_triangle:
        return 'nao eh um triangulo'
    elif side1 == side2 == side3:
        return 'equilatero' 
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return 'isosceles'
    else:
        return 'escaleno'

def lower_number(list):
    temp_number = list[0]
    for i in list:
        if i < temp_number:
            temp_number = i
    return temp_number

def asterisk_piramid(n):
    if n <= 1:
        return 'A base deve ser maior que 1'
    else:
        for i in range(1, n + 1):
            print(i * '*')

def summation(n):
    total = 0
    for number in range(1, n + 1):
        total += number
    return total


def fuel_price(type, liters):
    if type == "A":
        price = 1.90
        discount = 0.03
        if liters > 20:
            discount = 0.05
    elif type == "G":
        price = 2.50
        discount = 0.04
        if liters > 20:
            discount = 0.06
    total = price * liters
    total -= total * discount
    return total

def max_num(list):
    return max(list)

if __name__ == '__main__':
    print(biggerInterager(100, 30))
    print("{0:.2f}".format(arithmetic_median([1, 2, 3, 4, 5, 20])))
    print(larger_name(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"]))
    print(paint_cost(60))
    print(type_of_triangle(10, 9, 8))
    print(lower_number([5, 9, 3, 19, 70, 8, 100, 2, 35, 27]))
    print(asterisk_piramid(3))
    print(summation(5))
    print(fuel_price('A', 5))
    print(max_num([5, 9, 3, 19, 70, 8, 100, 2, 420]))