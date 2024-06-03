# controles de flujo
todos los programas trabajan a traves de instruccione ordenadas.
existen maneras de romper con el flujo normal de los prgramas creando         `bifurcacuiones` o creando  `repeticiones`
## decisiones
## la sentencia if
la sentencia de decicion en phyton es `if` , en sun escritura debemos añadir una  **expresionde compraracion**
terminando con el `:` al final de la linea.
< ejemplo:

``` python
if true:
    print("es verdad")
## ciclos
son os controles de flujo que repiten
ejemplo for
```python
for n inrange(1.21):
    if n%
``` python

edad:int=int(input)
# p'rimer ejemplo if estrucuturado
edad:int=int(input("escribe tu edad: "))
if edad>=18:
    print("eres mayor")
else:
    print("eres menor de edad")
# ejemplo de if almacenamiento en variable
edad_dos:int=int(input("ingresa tu edad: "))
respuesta:str="eres mayor" if edad_dos>=18 else "eres menor"
print(respuesta)

for i in range(1,6):
  print("tabla de multiplicar de ",i)
for j in range(1,6):
 resultado=i*j
 print( i,"*",j,"=", resultado)
print()

### while
es un mecaniusmo que usa python para repetir instrucciones, la semantica de ewsta sentencia es: `mientras se cumpla la condicion has algo`
```python
while():
    print("hola")
# un byucle infinito
while False:
    print("hola")

while condicion:
    print("!hola")
    condicion=False
    print("hola")  
while condicion:
    eval=input("desea continuar [s/n]:")
    if eval=="s":
        print("continuas en el bucle")
        continue
    else
    print("se termina el programa")
    break
contador=0
while contador<=5:
    print(contador)
    contador+=1
