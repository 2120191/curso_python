oracion:str=input("escribe una oracion: ")
contador:int=0
for n in range (0,len(oracion)):
    if oracion[n]==",":
      contador=contador+1
for n in ",":
    print(n)
print(f"la cantidad de letras que tengo es(contador)")
    