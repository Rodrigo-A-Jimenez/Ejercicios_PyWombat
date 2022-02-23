# Elimina todas las vocales

El usuario desea eliminar todas las vocales de la cadena de caracteres que introduce en consola. En consecuencia debe crear la logia adecuada para imprimir la misma sentencia pero sin vocales.

**Detalles:**

Tenga en cuenta las vocales en mayúscula.

**Ejemplo:**

**Entrada:**

Cadena: Me gusta estudiar en pywombat.com

**Salida:**

M gst stdr n pywmbt.cm

**Entrada:**

Cadena: El lenguaje de Python es multiplataforma

**Salida:**

l lngj d Pythn s mltpltfrm

**Tu respuesta**

```python
cadena = str(input('Ingrese una cadena de texto: '))
vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def eliminar_vocales(cadena, letras_para_eliminar):
    cadena_return = cadena
    for letra in letras_para_eliminar:
        cadena_return = cadena_return.replace(letra, "")
    return cadena_return

print(eliminar_vocales(cadena, vocales))
    
```
