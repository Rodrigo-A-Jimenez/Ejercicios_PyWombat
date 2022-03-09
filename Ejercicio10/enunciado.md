# Elimina elementos duplicados de una lista.

Dada una lista de números enteros.

**Ejemplo:**

```python
[1, 2, 3, 2, 10, 20, 10, 2, 3, 4, 5, 2, 2] 
```

Desarrolla una función que elimine todos los elementos duplicados dentro de la colección.

La función debe cumplir con los siguientes requerimientos.

- La función debe tener por nombre **simple_list**.
- La función debe recibir como argumento una lista de números enteros.
- La función debe **retornar una lista** con elementos únicos dentro de ella.
- Si dentro de la lista existen 2 o más elementos duplicados, la lista debe **retornar únicamente** un elemento unico.

**Ejemplo.**

```python
lista_a = [1, 2, 3, 2, 10, 20, 10, 2, 3, 4, 5, 2, 2] 
>>> simple_list(lista_a)
[1, 2, 3, 10, 20, 4, 5]

lista_b = [110, 20, 45, 50] 
>>> simple_list(lista_b)
 [110, 20, 45, 50] 

lista_c = [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4] 
>>> simple_list(lista_c)
[1, 2, 3, 4]
```

## Solución:

```python
def simple_list(lista: list):
    lista_final = []
    for i in lista:
        if not i in lista_final:
            lista_final.append(i)
    return lista_final
```