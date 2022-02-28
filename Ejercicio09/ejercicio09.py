
def colorSelect(colors: list):
    n = len(colors)
    print('Primer color: {}'.format(colors[0]))
    print('Penúltimo color: {}'.format(colors[n-2]))
    print('Último color: {}'.format(colors[n-1]))

lista = ['Azul', 'Verde', 'Amarillo', 'Rojo', 'Morado', 'Negro', 'Blanco', 'Gris']

colorSelect(lista)