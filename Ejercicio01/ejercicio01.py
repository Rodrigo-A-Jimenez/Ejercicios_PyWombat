n = int(input('Longitud de la lista: '))

list = []
par = []

for i in range(n):
    list.append(int(input('Ingresa un elemento: ')))

for i in list:
    if (i%2 == 0):
        par.append(i)

print(max(par))