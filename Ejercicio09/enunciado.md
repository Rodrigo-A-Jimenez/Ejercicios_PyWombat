# Colores

Dada la siguiente lista de colores

```python
['Azul', 'Verde', 'Amarillo', 'Rojo', 'Morado', 'Negro', 'Blanco', 'Gris']
```

Desarrolla un programa que nos permita conocer:

- El primer color de la lista.
- El penúltimo color de la lista.
- El último color de la lista.

## Ejemplo.

```python
Primer color: Azul
Penúltimo color: Blanco
Último color: Gris
```

## Ayuda:

- Recuerda, en Python, las lista comienzan en el índice 0.
- Es posible utilizar números negativos en los índices.


## Tu respuesta:

```python
def colorSelect(colors: list):
    n = len(colors)
    print('Primer color: {}'.format(colors[0]))
    print('Penúltimo color: {}'.format(colors[n-2]))
    print('Último color: {}'.format(colors[n-1]))

lista = ['Azul', 'Verde', 'Amarillo', 'Rojo', 'Morado', 'Negro', 'Blanco', 'Gris']

colorSelect(lista)
```