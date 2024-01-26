lista=list(["xddd","olaafe",5,8,9])

#agregando elementos a la lista
add_append=lista.append("ratatoskja")
#agregando elementos a la lista en un indice especifico
lista.insert(2,"54644")
#agregando varios elementos a la lista con []
lista.extend([5,"ñoño","perro"])
#eliminando elementos a la lista por un indice
lista.pop(0)  #-1 pa eliminar el ultimo elemento
#eliminando elementos a la lista por su valor
lista.remove("olaafe")

#eliminando TODOS los elementos de una lista lista.clear()

#ordenando los elementos de una lista por su valor numerico solo en int ascendentemente
#lista.sort()
print(lista)