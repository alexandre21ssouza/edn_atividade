# Exercício 2

# Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'.
# O programa deve exibir o nome, email e país do usuário gerado."​


from faker import Faker



fake = Faker("pt_BR")

def gerar_usuario():
   

    nome = fake.name()
    email = fake.email()
    cpf = fake.cpf()
    pais = fake.current_country()

    user = f"""
    nome: {nome}
    email: {email}
    cpf: {cpf}
    país: {pais}
    """

    return user


usuario = gerar_usuario()

print(usuario)
