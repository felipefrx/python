#key - Value
car = {
    "Manofacturer": "Honda",
    "Model": "HRV",
    "Year": 2016,
    "Color":"Black"
}

car["Year"] = 2020 #Change value
print(car["Year"])

car["Rim"] = 18 #Add value

car.pop("Color") #Remove value
        #or
del car["Year"]

mod = car.get("Model") #Get key value
print(mod)

print(car["Model"])

for x in car:
    print(x,"|", car[x]) #Print key and value
            #or 
for x, y in car.items():
    print(x, ":", y)

car.clear() #Clear dictionary
print(car)

cars = {
    "car1": {
        "Manofacturer": "Volkswagem",
        "Model": "Golf"
    },
    "car2":{
        "Manofacturer": "Honda",
        "Model": "HRV"
    }
}

print(cars["car2"]["Model"])

car1 = {
        "Manofacturer": "Volkswagem",
        "Model": "Golf"
    }
car2 = {
        "Manofacturer": "Honda",
        "Model": "HRV"
    }

carros = {
    "c1": car1,
    "c2": car2
}

print(carros["c1"])
print(carros["c2"]["Model"])