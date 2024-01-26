animales={"perro","gato","rata","loro"}
numeros={10,15,41,87}
#iterando conjuntos y tuplas
#se ejecuta tantas vecs como variables haya
for animal in animales:
  print("Ahora la variable animal es igual a : {}".format(animal))


for tuco in numeros:
  result=tuco*10
  print(result)

#interando 2 conjuntos del mismo tamaño al mismo tiempo con for...,.. in zip()
for animal,tuco in zip(animales,numeros):
  print("recorriendo conjunto 1: {}".format(animal))
  print("recorriendo conjunto 2: {}".format(tuco))

for ace in range(1,11):
  print(ace)

#forma correcta de recorrer una conjunto por su indice
for num in enumerate(numeros):
  print(num)

#usando el else
for numero in numeros:
  print(f"ejecutando el ultimo bucle,valor actual : {numero}")
else:
  print("el bucle termino")