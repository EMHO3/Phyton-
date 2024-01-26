"""
dict={}
for i in range(1,11):
  dict[i]=i*2

print (dict)

dict_v2={i : i*2 for i in range(10,11)}
print (dict_v2)


countries=["col","peru","mex","chi"]
poblacion={}
for country in countries:
  poblacion[country]= random.randint(1,100)

print(poblacion)
"""

names=["brenda","yasuri","rosario"]
ages=["19","20","21"]
print(list(zip(names,ages)))