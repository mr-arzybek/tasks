x1 = float(input("x1 ="))
y1 = float(input("y1 ="))
x2 = float(input("x2 ="))
y2 = float(input("y2 ="))
x3 = float(input("x3 ="))
y3 = float(input("y3 ="))


def triangle_area(*args):
    a = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
    b = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    c = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return (f'{round(s, 3)}')


print(triangle_area(0, 0, 0, 0, 0, 0))
with open('area.txt', 'w') as file:
    file.write(triangle_area())

a = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
b = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
c = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
A = a * a
B = b * b
C = c * c
g = [A, B, C]
for i in g:
    if A == C + B:
        print("да является прямым")
        with open('truefalse.txt', 'w') as file:
            file.write(f"{True}")
    elif B == A + C:
        print("да является прямым")
        with open('truefalse.txt', 'w') as file:
            file.write(f"{True}")
    elif C == A + B:
        print("да является прямым")
        with open('truefalse.txt', 'w') as file:
            file.write(f"{True}")
    else:
        print("не является прямым")
        with open('truefalse.txt', 'w') as file:
            file.write(f"{False}")
            
            
            
            