def posicionPar(lista):
    listReturn = []
    for i in range(len(lista)):
        if (i%2 == 0):
            listReturn.append(lista[i])
    return listReturn

lista_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(posicionPar(lista_a)) #[1, 3, 5, 7, 9]

lista_b = [100, 78, 90, 5, 12, 134, 56, 78, 90, 9]
print(posicionPar(lista_b)) #[100, 90, 12, 56, 90]

lista_c = [80, 90, 100, 200, 300, 400, 500, 600]
print(posicionPar(lista_c)) #[80, 100, 300, 500] 