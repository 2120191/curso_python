# tipos de datos estructurados (TDA .tipos de datos abstractos)
## metodos
### 3. eliminar elementos de lista

#python 
### 5. comprarcion de listas
# podemos hace usiode los operadores de compararcionpara comparar listas
#python
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
#python
lista=[1,2,3,4]
copia_lista=lista[0]=2
print(copia_lista)
#[2,3,4,5,6]
#modificando lista con diccionario
alumnos= [

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

#yo como dueño  de mis mascota
# dseso ver una lista de mi mascota
# para tener un resumen o control de ellos.


# yo como dueño  de mis mascota
# dseso actualizar la edad de mi mascota
# para tener una lista correcta de mi mascota.

import json

def ingresar_notas():
    notas = {}
    while True:
        nombre = input("Ingrese el nombre del estudiante (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        nota = float(input("Ingrese la nota del estudiante: "))
        notas[nombre] = nota
    guardar_notas(notas)

def guardar_notas(notas):
    with open('notas.json', 'w') as file:
        json.dump(notas, file)
    print("Las notas han sido guardadas exitosamente.")

def main():
    try:
        with open('notas.json') as file:
            notas = json.load(file)
            print("Las notas ya han sido ingresadas y no pueden ser modificadas.")
    except FileNotFoundError:
        print("Bienvenido al sistema de ingreso de notas.")
        ingresar_notas()

if _name_ == "_main_":
    main()



```python
# un empresario de alquiler de autos desea guaradar en una base de datos la informacion de de sus vehiculos,
# proceso que desea automizar con un sistema informatico,las acciones que puede realizar el empresrio son ver 
# las lista de auto que tiene ,podre tambien actualizar la lista y agregar un nuevo vehiculo
###

# yo como dueño
# quiero mejorar la atencion de alquiler de autos
# para que el proceso de alquiler sea mas rapido


# Diccionario para almacenar la información de los vehículos
vehiculos = {}

# Función para ver la lista de autos
def ver_lista_autos():
    if vehiculos:
        for id, info in vehiculos.items():
            print(f"ID: {id}, Marca: {info['marca']}, Modelo: {info['modelo']}, Año: {info['año']}, Precio: {info['precio']}")
    else:
        print("No hay vehículos en la lista.")

# Función para actualizar la lista de autos
def actualizar_lista_auto():
    ver_lista_autos()
    id_actualizar = int(input("Ingrese el ID del vehículo que desea actualizar: "))
    if id_actualizar in vehiculos:
        nuevo_precio = float(input("Ingrese el nuevo precio del vehículo: "))
        vehiculos[id_actualizar]["precio"] = nuevo_precio
        print("Lista de autos actualizada.")
    else:
        print("ID de vehículo no encontrado.")

# Función para agregar un nuevo vehículo
def agregar_nuevo_auto():
    marca = input("Ingrese la marca del vehículo: ")
    modelo = input("Ingrese el modelo del vehículo: ")
    año = int(input("Ingrese el año del vehículo: "))
    precio = float(input("Ingrese el precio del vehículo: "))
    
    nuevo_id = max(vehiculos.keys(), default=0) + 1
    vehiculos[nuevo_id] = {"marca": marca, "modelo": modelo, "año": año, "precio": precio}
    print("Nuevo vehículo agregado.")

# Menú de opciones
while True:
    print("\nMenú de opciones:")
    print("1. Ver lista de autos")
    print("2. Actualizar lista de autos")
    print("3. Agregar un nuevo vehículo")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ver_lista_autos()
    elif opcion == "2":
        actualizar_lista_auto()
    elif opcion == "3":
        agregar_nuevo_auto()
    elif opcion == "4":
        print("Saliendo del sistema.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")