#Exercício 1

#Crie um programa que gera uma senha aleatória com o módulo random, utilizando 
#caracteres especiais, possibilitando o usuário a informar a quantidade de 
#caracteres dessa senha aleatória. ​

import random
import string


def senha(value):
   
    if value <= 0:
        return "Digite um número positivo"

    caracteres = string.printable

    senha = ''.join(random.choice(caracteres) for _ in range(value))
   
     
  

    return senha

carcteres = int(input("Digite o tamanho da senha que deseja em números: "))
nova_senha = senha(carcteres)

print(nova_senha)
    