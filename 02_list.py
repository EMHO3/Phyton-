numbers =[]
for elements in range(1,11):
  numbers.append(elements * 3)

print(numbers)

#comprension e listas
numbers_v2=[elements for elements in range(1,11)]
print(numbers_v2)