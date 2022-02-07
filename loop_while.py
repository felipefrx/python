import os

os.system('clear')
cont = 0

while cont < 11:
    print("Value of i:", cont)
    cont += 1
    if cont >= 6:
        break
print("Finished!")

print("")

names = ["Felipe", "Luisa", "Cassio", "Brenda"]
tam = len(names)
cont = 0

while cont <= tam:
    print(names[cont])
    cont += 1
    if cont >= tam:
        break
print("Finished!")

print("")

carros = []
carro = str(input("Type name of the new car: "))

while carro != '.':
    carros.append(carro)
    carro = str(input("Type name of the new car: "))

os.system('clear')

cont = 1
for x in carros:
    print("Car {}: ".format(cont), x)
    cont += 1
print("Finished!")