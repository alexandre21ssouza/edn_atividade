#Calculando a gorjeta com função

def calcular_gorjeta(porcentagem_gorjeta, conta):

    gorjeta = (porcentagem_gorjeta / 100)
    total = (gorjeta * conta) + conta

   
    return total


result = calcular_gorjeta(10, 100)

print(result)