def bin_to_dec(num_bin:int):
    number_bin= list(str(num_bin))
    n = 0
    number_dec = 0
    for i in number_bin[::-1]:
        number_dec += int(i) * 2**n
        n += 1
    return number_dec
'''
# mas efectivo
def bin_to_dec(num_bin:int):
    return int(str(num_bin), 2)
'''
def bin_to_dec(num_bin:int):
    return int(str(num_bin), 2)

print(bin_to_dec(1011))
#11

print(bin_to_dec(111010111))
#471

print(bin_to_dec(10011001))
#153