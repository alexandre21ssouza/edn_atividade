# Exercício 3

# Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário,
# utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes 
# ao CEP consultado.​


import requests


def consultar_cep(value):
    URL = f"https://viacep.com.br/ws/{value}/json/"

    print(value)

    response = requests.get(URL)

    dados = response.json()
    end = f"""
    logradouro: {dados["logradouro"]}
    bairro: {dados["bairro"]}
    cidade: {dados["localidade"]}
    estado: {dados["estado"]}
    """

    return end


cep = input("Digite seu cep: ").replace("-","")

result = consultar_cep(cep)

print(result)