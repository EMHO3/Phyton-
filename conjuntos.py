#creando un conjunto con set
conjunto=set(["gato1"])

#metiendo un conjunto dentro de otro
conjunto1=frozenset(["perro1","perro2"]) #subconjunto de conjunto 2
conjunto2={conjunto1,"perro3"}      #superconjunto
print(conjunto2)

#teorias de conjuntos
conjunto1={1,2,3,4,5,6,7,8,9,10}
conjunto2={1,2,6}
                #es subconjunto?
reesultado=conjunto2.issubset(conjunto1)
resultado=conjunto2<=conjunto1
print(reesultado)
print(resultado)

                   #es superconjunto?
reesultado=conjunto2.issuperset(conjunto1)
resultado3=conjunto2>conjunto1
print(resultado3)

