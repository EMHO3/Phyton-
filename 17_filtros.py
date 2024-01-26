numbers=[5,4,8,7,6,2,10,9]
new_numbers=list(filter(lambda x:x % 2 == 0,numbers))
print(new_numbers)