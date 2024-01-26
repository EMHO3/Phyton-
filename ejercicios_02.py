otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_prom = 4
dalto_curso = 1.5

dif_con_minutos = 100 - dalto_curso / otros_cursos_min * 100
dif_con_max = 100 - dalto_curso*1000 // otros_cursos_max / 10
dif_con_promedio = 100 - dalto_curso / otros_cursos_prom * 100
print("-------------")
print("el curso de dalto dura: ")
print("-el curso de dalto dura un {}% menos que el mas rapido".format(
    dif_con_minutos))
print("-el curso de dalto dura un {}% menos que el mas lento".format(
    dif_con_max))
print("-el curso de dalto dura un {}% menos que el promedio".format(
    dif_con_promedio))
print("_____-------------")


#Mostrandop dif si los cursos duraran 10h
print ("el curso de dalto equivale a: ")
print("-ver este curso equivale a ver {} horas de otros cursos".format(otros_cursos_prom*100//dalto_curso/10))

print("-ver otros equivale a ver {} horas de este curso".format(dalto_curso*100//otros_cursos_prom/10))
