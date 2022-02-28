# Contador de vocales dentro de un string

Define una función que nos permita conocer la cantidad de vocales que posea un string.

El programa deberá cumplir con los siguientes requerimientos.

- La función debe tener por nombre **vowel_counter**.
- La función debe recibir como argumento un **string**.
- La función debe retornar, mediante un número entero, la cantidad de vocales que posee el string ingresado.


## Ejemplo.
```python
>>> vowel_counter('Hola mundo')
4

>>> vowel_counter('Eduardo Ismael')
7

>>> vowel_counter('PyWombat')
2

```

**Ayuda:** Para no complicarte con el tema de mayúsculas o minúsculas, te recomiendo convertir todas las letras a minúsculas.

## Solución

```python
def vowel_counter(cadena: str):
    if not isinstance(cadena, str):
        raise TypeError ("Se necesita una cadena!")

    contador = 0
    vocales = ['a', 'e', 'i', 'o', 'u']

    for i in cadena.lower():
        if i in vocales:
            contador += 1
    return contador

print(vowel_counter('Hola mundo')) # 4
print(vowel_counter('Eduardo Ismael')) # 7
print(vowel_counter('PyWombat')) # 2

```