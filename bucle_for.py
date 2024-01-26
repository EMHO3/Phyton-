animales=["perro","gato","rata","loro"]
numeros=[10,15,41,87]
#iterando listas y tuplas
#se ejecuta tantas vecs como variables haya
for animal in animales:
  print("Ahora la variable animal es igual a : {}".format(animal))


for tuco in numeros:
  result=tuco*10
  print(result)

#interando 2 listas del mismo tamaño al mismo tiempo con for...,.. in zip()
for animal,tuco in zip(animales,numeros):
  print("recorriendo lista 1: {}".format(animal))
  print("recorriendo lista 2: {}".format(tuco))

for ace in range(1,11):
  print(ace)

#forma correcta de recorrer una lista por su indice
for num in enumerate(numeros):
  print(num)

#usando el else
for numero in numeros:
  print(f"ejecutando el ultimo bucle,valor actual : {numero}")
else:
  print("el bucle termino")