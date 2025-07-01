#Forma para achar palavras que são escritas da mesma maneira no sentido inverso(Palíndromo):
#EXEMPLO: arara, asa, etc ...


def is_palindromo(texto):
    
    texto_limpo = ''.join(char.lower() 
                          for char in texto 
                          if char.isalnum())
  
    return texto_limpo == texto_limpo[::-1]


frase = "O lobo ama o bolo"
resultado = is_palindromo(frase)

if resultado == True:
    resposta = "Sim"
else:
    resposta = "Não"

print(f"'{frase}' é um palíndromo? {resposta}")
