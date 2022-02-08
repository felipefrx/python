carros = [
    ["Modelo", "HRV"],
    ["Fabricante", "Honda"],
    ["Ano", 2016],
]

carros[2][1] = 2019 #Changed value
carros.append(["Cor", "Preto"]) #Add value

for x, y in carros:
    print(x,"|", y)