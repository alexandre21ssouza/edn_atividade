# Exercício 4

# Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real 
# Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), 
# e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da 
# última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.​

import requests
from datetime import datetime

def obter_cotacao(value):

    url = f"https://economia.awesomeapi.com.br/last/{value}-BRL"

    try:

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        cotacao = data[f"{value}BRL"]

        conversao = f"""
        Moeda: {value} para BRL
        Valor: R$ {float(cotacao["bid"]):.2f}
        Máximo: R$ {float(cotacao["high"]):.2f}
        Mínimo: R$ {float(cotacao["low"]):.2f}
        Data/hora - requisição{datetime.fromtimestamp(int(cotacao["timestamp"]))}
        registro cotação: {cotacao["create_date"]}
        """



        return conversao

    
    except requests.RequestException as e:
        print(f"Erro ao obter a cotação", e) 
    except KeyError:
        return "Moeda não encontrada"

    



moeda = input("Digite o valor da moeda para cotação (ex. USD, EUR, GBP): ").upper()
resultado = obter_cotacao(moeda)

print(resultado)