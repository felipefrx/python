n1 = 10
n2 = 5

def sum(): #Defines a function
    r = n1 + n2
    print("Sum of {} + {} = {}\n".format(n1, n2, r))

def subtraction(n3, n4):
    r = n3 - n4
    print("Subtraction of {} - {} = {}\n".format(n3, n4, r))

subtraction(50, 30)
sum()

def calculations():
    subtraction(90, 60)
    sum()

calculations()

def text(*txt):
    for t in txt:
        print(t)

text("cat", "dog", "bird", "cock", "whale")

def car(c = "Golf"):
    print(c)

car() #if you don't pass an argument, it prints the default argument.
car("Camaro")


list = ["Golf", "Camaro", "HRV"]
def car2(num):
    for n in num:
        print(n)

car2(list)
