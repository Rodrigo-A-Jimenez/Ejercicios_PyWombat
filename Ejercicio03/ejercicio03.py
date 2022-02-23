cadena = str(input('Ingrese una cadena de texto: '))
vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def eliminar_vocales(cadena, letras_para_eliminar):
    cadena_return = cadena
    for letra in letras_para_eliminar:
        cadena_return = cadena_return.replace(letra, "")
    return cadena_return

print(eliminar_vocales(cadena, vocales))
    