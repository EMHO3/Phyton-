#creando una fuyncion con parametros
def saludar(nombre,genero):
  genero=genero.lower()
  if(genero=="mujer"):
    adjetivo="reina"
  elif (genero=="hombre"):
    adjetivo="rey"
  print(f"hola {nombre} como andas {adjetivo}?")  
saludar("brenda","MUJER")
saludar("YASURI","MUJER")
saludar("rosario","MUJER")

