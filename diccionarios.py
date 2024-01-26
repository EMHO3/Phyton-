#creando diccionarios con dict()
diccionaro=dict(nombre="emir",edad="20")
#las listas no pueden ser claves pero las tuplas si
diccionaro={("nombre","rancio"):"jajajja"}

#creando diccionarios con fromkeys()
diccionaro=dict.fromkeys(["nombre","apellido","edad"])
print(diccionaro["nombre"])