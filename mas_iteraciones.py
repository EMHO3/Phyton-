frutas=["platano","manzana","uva","sandia","durazno"]
cadena="holacomoestas"
numero=[1,2,3,4,5,6]

for x in frutas:
  if x=="uva":
    continue #se saltea el valor que tenga mi variable x, pero el #bucle continua
  print(f"me voa comer una {x}")  

for x in frutas:
  print(f"me voa comer una {x}")
  if x=="uva":
    break #se rompe el bucle
print("fin")

#recorrer una cadena de ttexto
for letra in cadena:
  print(letra)

#for en una linea de codigo
numero_duplicado=[x*2 for x in numero]
print(numero_duplicado)