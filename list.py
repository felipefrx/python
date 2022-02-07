names = ["João", "Felipe", "Hugo", "Isabela", "Guilherme", "Luiza"]
names[2] = "Paulo"
names.append("Carla") #Add a new name to the list
names.remove("João") #Remove a name from the list
names.pop() #Remove a last name from the list
del names[0] #Remove a name in especifc point

print("Size list:", len(names))
print(names)
print(names[2])
print(names[-1]) #Print left for right 

names.clear() #Clear the list
print(names)

names = ["João", "Felipe", "Hugo", "Isabela", "Guilherme", "Luiza"]
names2 = list(names) #Make the copy for another list
print(names2)

names3 = names + names2 #Join two lists
print(names3)