import os #This module provides a portable way of using operating system dependent functionality.

os.system('clear') #Linux #This command clean the console
#os.system('cls') #Windows

name = str(input("Type your name: ")) #The function input stores what the user has typed 
age = int(input("Type your age: "))

if age >= 18:
    print("Wellcome, {}!".format(name))
else:
    print("Sorry, you don't have age for acess this program.")
