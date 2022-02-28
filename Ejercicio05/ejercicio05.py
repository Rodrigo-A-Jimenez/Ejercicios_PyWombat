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