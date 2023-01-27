import math

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x,
    else:
        return None

a = float(input("Inserisci il coefficiente a: "))
b = float(input("Inserisci il coefficiente b: "))
c = float(input("Inserisci il coefficiente c: "))

x = solve_quadratic_equation(a, b, c)

if x:
    if len(x) == 1:
        print("La soluzione dell'equazione è x =", x[0])
    else:
        print("Le soluzioni dell'equazione sono x1 =", x[0], "e x2 =", x[1])
else:
    print("L'equazione non ha soluzioni reali")
