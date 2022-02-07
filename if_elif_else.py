import random

a = 3
b = 2
op = random.choices(["+", "-", "/", "**"])

print("The operator is: {}".format(op))

if op == ["+"]:
    res = a + b
    print(res)
elif op == ["-"]:
    res = a - b
    print(res)
elif op == ["/"]:
    res = a / b
    print(res)
else:
    res = a ** b 
    print(res)

print("Finished!")

#Other example

climate = "sol"
money = 50
place = ""

if climate == "sol" and money > 100:
    place = "club"
    print(place)
else:
    place = "cine"
    print(place)