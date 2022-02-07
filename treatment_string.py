name = " Felipe Ferreira "

print("Name:", name)
print("Size with spaces:", len(name))
print("Size without additional spaces:", len(name.strip())) #Strip method cancels the string spaces 

print(name.strip()[0:6]) #Show length at specific point

print(name.replace("Ferreira", "Silva").strip()) #Replacement one name for another 

name = "Felipe.Ferreira.Silva"
a = name.split(".") #Splited the strings where to find points and creates a list 
print(a[1])


palavra = "felipe"
res = palavra.upper() in name.upper() #Checks if the word is in the string 
res2 = "Ferreira" not in name #Denial
print(res)                    #Upper function makes everything uppercase
print(res2)                   #Lower function makes everything lowercase 

var1 = "Felipe \n\"Ferreira\" \nda \nSilva" #\n make de line break
print(var1)                                 #\" make the impression
                                            #Other methods: \r, \t, \b ...
