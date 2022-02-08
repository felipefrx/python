carros = [
    ["Model", "HRV"],
    ["Manofacturer", "Honda"],
    ["Year", 2016],
]

carros[2][1] = 2019 #Changed value
carros.append(["Color", "Black"]) #Add value

for x, y in carros:
    print(x,"|", y)
