# tipos de datos estructurados (TDA .tipos de datos abstractos)
## metodos
### 3. eliminar elementos de lista

``` python 
### 5. comprarcion de listas
podemoshace usiode los operadores de compararcionpara comparar listas
```python
compara=[1,2,3]>[1,2,3]
# 1 no por que sonh iguales en amabas listas
# 2 no por que son iguaqles en las mismas listas
# 3 evalua que es menor de 4
# entonces la primera lista es menor que la segunda lista
print(compara)

# salida:

### 6. cuidado con las copias
## DATO ESTRUCUTRADO
lista_original[1,2,3,4]
copia_lista=lista_original

lista_original[-1]=15
print(copia_lista)

## 7.fe de erratas (actualizar listas)
```python
lista=[1,2,3,4]
copia_lista=lista[0]=2
print(copia_lista)
#[2,3,4,5,6]
#modificando lista con diccionario
alumnos=[

    "nombre":"abel,"
    "edad":15


    "nombre":"anthony",
    "edad".29
alumnos[0]["edad"]=30
alumnos[0]=("nombre":"mafer","edad":15)
print(alumnos)

## crear un programa que reciba una lista desordenada y muestre por terminal la lista ordenada y la previa aser ordenada

lista=[4,76,1,3,4,5,8]
lista.sort()
print(lista)

lista=[4,76,1,3,4,5,8]
copia_lista=lista.copy()
copia_lista.sort()
print(lista)
print(copia_lista)

## 2. crear una lista con 3 dicionarios donde tendran los datos de susu mascotas (nombre,edad, sexo,raza)

##tareas
# mostrar la lista con os 4 diccionarios
# editar registro y cambiarle la edad sin modificar la lista original.
# mostrar la lista original y luego la lista con elregistro modificado
