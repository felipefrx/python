#Booleans values: True or False

var1 = True
var2 = False

op = 10>15
print(op) #Result False

op = 10<15
print(op) #Result True

test = 0
print(bool(test)) #Return False

test = 1
print(bool(test)) #Return True

test = "Test"
print(bool(test)) #Return True

test = ""
print(bool(test)) #Return False, because the string is empty

test =  ["", ""]
print(bool(test)) #Return True

test = []
print(bool(test)) #Return False