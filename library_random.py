import random

ran = random.randrange(0, 100) #The library choose a random number in range of 0 to 100

print(ran) 

list_random = [random.randrange(0, 100), random.randrange(0, 100), random.randrange(0, 100)]

z = 1
for x in list_random:
    print("Valor {}:".format(z), x)
    z += 1
