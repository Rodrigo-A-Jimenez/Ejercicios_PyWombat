# Convertir de número binario a número decimal

Miriam necesita de un programa que convierta de número binario a número decimal

**Ejemplo:**

**Entrada:**

Número binario: 1011

**Salida:**

Número decimal: 11

**Entrada:**

Número binario: 111010111

**Salida:**

Número decimal: 471

**Entrada:**

Número binario: 10011001

**Salida:**

Número decimal: 153

## Solución:

```python
def bin_to_dec(num_bin:int):
    number_bin= list(str(num_bin))
    n = 0
    number_dec = 0
    for i in number_bin[::-1]:
        number_dec += int(i) * 2**n
        n += 1
    return number_dec
```