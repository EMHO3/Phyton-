try:
  print(0/0)
  
except ZeroDivisionError as error:
  print(error)

try:
 assert 1!=1,"Uno no es igual a 1" 
except AssertionError as error:
  print(error)
try:
 age =10
 if age < 18:
  raise Exception("Es menor de edad no esta permitido")
  
except Exception as error:
  print(error)

print("hola")
