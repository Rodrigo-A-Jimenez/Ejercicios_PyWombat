# Formato de fechas

Desarrolla un programa que nos permita conocer la fecha actual. El salida de la fecha debe cumplir con el siguiente formato.

```python
<Día>-<Mes>-<Año> <Hora>:<Minutos>:<Segundos>
```

- El día, el mes y el año debe encontrarse separador por un guion (-).
- La hora, los minutos y los segundos debe encontrarse separador por 2 puntos (:).

**Ejemplo.**

```python
2021-04-15 10:21:20'

2020-12-31 11:59:59'
```

**Ayuda**: Recuerda, para conocer la fecha actual, puedes hacer uso de módulo datetime.

## Solución:

```python
import datetime

def fecha_actual():
    return datetime.datetime.today()
```