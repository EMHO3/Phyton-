frase = input("diga algo y te calculo cuanto tiempo te tardarias en decirlo")

palabras_separadas = frase.split(" ")
cant_palabras = len(palabras_separadas)

print("dijiste {} palabras, y tardaras en decirlas {}s en decirlo".format(
    cant_palabras, cant_palabras / 2))

print("dalto lo diria en {}s".format(cant_palabras *100// 2*1.3))
