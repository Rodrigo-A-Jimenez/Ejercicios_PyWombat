length = input('Longitud de la lista: ')

new_list = [  int(input('ingresa un valor: ')) for _ in range(int(length)) ]

pair_list = [val for val in new_list if val % 2 == 0]

if pair_list:
    pair_list.sort(reverse=True)
    print(pair_list[0])