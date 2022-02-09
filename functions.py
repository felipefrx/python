n1 = 10
n2 = 5

def sum(): #Defines a function
    r = n1 + n2
    
    return r #Returns the result

print(sum())

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


#Lambda Function = Simple function

soma = lambda a, b : a + b
print(soma(4, 4))

print((lambda r, y : r + y)(6, 3))

r = lambda x, func : x + func(x)
res = r(2, lambda x : x * x)
print(res)