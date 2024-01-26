import random
countries=["col","chi","uru","per"]
poblacion_v2={country:random.randint(1,100)for country in countries}

print(poblacion_v2)

result={country:poblacion for(country,poblacion)in poblacion_v2.items()if poblacion >20}

print(result)

text="Hola soy emir"
unique={c:c.upper()for c in text if c in "aeiou"}
print (unique)