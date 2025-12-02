#generar placas random
import random
input("Solo inicia el programa para generar placa random")
print("-----------")
print("|", end="")
for cuanto in range(3):
    print(chr(random.randint(65,91)), end= "")
print("-", end="")
for numeroscasillas in range(2):
    print((random.randint(0,9)), end= "")
print("-", end="")
for numeroscasillas in range(2):
    print((random.randint(0,9)), end= "")
print("|")
print("-----------")  
