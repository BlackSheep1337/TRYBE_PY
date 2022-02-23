PI = 3.14

def square(side):
    return print(side * side + PI)


def rectangle(length, width):
    return print(length * width / PI)

def circle(radius):
    return print(PI * radius * radius)

square(10)
rectangle(30, 30)
circle(30)
