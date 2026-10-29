import random

print(random.uniform(0,10))
print(random.random())
print(random.randint(100000000, 999999999))
print(random.randint(0,1))

lista = [1,2,3]
print((random.choices(lista, k=2)))