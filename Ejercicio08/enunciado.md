# Calcular el radio de un circulo

Una de las operaciones básicas en matemáticas es sin duda calcular el área de un Circulo. Es por ello que en esta ocasión será necesario que crees un programa el cual nos permita conocer el área de un circulo dado su radio. El programa debe cumplir con los siguientes requerimientos.

El usuario debe ser capaz de ingresar (vía teclado) el radio del circulo.
El programa podrá calcular el área del circulo mediante el radio ingresado por el usuario.
El programa podrá aceptar un radio con o sin punto decimal.
El programa debe mostrar en consola, con el siguiente mensaje: El área del circulo es: x, el resultado dela operación.

## Ejemplo.
```python
Ingresa el radio del circulo: 8.5
El área del circulo es: 226.9800692218775
```

## Ayuda:

Recuerda que la forma de convertir un string a un flotante es mediante la función float.

## Deseado:

Si es posible limita el resultado a solo dos puntos decimales.

## Tu respuesta

```python
from math import pi

def areaCirculo(radio:float):
    return round(pi*radio**2, 2)

rad = float(input('Ingresa el radio del circulo: '))
print('El área del circulo es: {}'.format(areaCirculo(rad)))
```