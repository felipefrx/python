var1 = 1 #Int
var2 = 1.5 #Float
var3 = "Teste" #String
var4 = False #Boolean, True or False

for x in list:
    print("The type of {}: ".format(x), type(x))

r = range(0, 100) #Create a list
set = {7, 1, 1, 6, 4, 7, 1} #Set, it don't repeated values
list = [var1, var2, var3, var4] #List / Array
tuple = (var1, var2, var3, var4) #Tuple, it is not mutable
dict = {
    "nome":"João",
    "sobrenome":"Silva",       #Dictionary, key value
    "idade":"22"
} 
