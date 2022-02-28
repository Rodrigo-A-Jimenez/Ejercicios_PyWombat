from math import pi

def areaCirculo(radio:float):
    return round(pi*radio**2, 2)

rad = float(input('Ingresa el radio del circulo: '))
print('El área del circulo es: {}'.format(areaCirculo(rad)))