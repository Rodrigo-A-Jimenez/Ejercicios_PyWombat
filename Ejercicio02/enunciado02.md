# Valores evaluados como falsos en Python

Diga de los siguientes valores, cuales son evaluados como falsos en Python. Argumente su respuesta imprimiendo en consola los valores, demostrando que éstos son falsos.

**Pista**
Son 5 opciones
<ul>
<li>0</li>
<li>""</li>
<li>'False'</li>
<li>"0"</li>
<li>[ ]</li>
<li>False</li>
<li>None</li>
</ul>
<p><strong>Ejemplo:</strong></p>

<div class="codehilite"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="kc">None</span> <span class="ow">or</span> <span class="kc">False</span><span class="p">)</span>  <span class="c1"># False</span>
</pre></div>
        </div>


## Solución

```python
print(0 or False) #False
print("" or False) #False
print('False' or False) #False
print('0' or False) #0
print([] or False) #False
print(False or False) #False
print(None or False) #False
```