#3- Conversor de Temperatura
#Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
#O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

temperatura = float(input("Digite a temperatura: "))
print("Digite C para(Celsius), F para(Fahrenheit) e K para(Kelvin) ")
origem = input("Digite a unidade de origem (C, F, K): ").upper()
destino = input("Digite a unidade de destino (C, F, K): ").upper()

resultado = 0  

if origem == destino:
    resultado = temperatura
else:
    if origem == "C":
        if destino == "F":
            resultado = (temperatura * 9/5) + 32
        elif destino == "K":
            resultado = temperatura + 273.15
    elif origem == "F":
        if destino == "C":
            resultado = (temperatura - 32) * 5/9
        elif destino == "K":
            resultado = ((temp - 32) * 5/9) + 273.15
    elif origem == "K":
        if destino == "C":
            resultado = temperatura - 273.15
        elif destino == "F":
            resultado = ((temperatura - 273.15) * 9/5) + 32
    else:
        print("Unidade de origem inválida.")
        exit()

print(f"{temperatura}°{origem} equivalem a {resultado:.2f}°{destino}")
