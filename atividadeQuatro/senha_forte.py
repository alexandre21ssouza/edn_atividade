

notas = []
while True:
    try:
        senha = input("Digite uma senha ou 'fim' para terminar: ")

        if senha.lower() == "fim":
            break

        if len(senha) < 8:
            print("Sua senha deve ter pelo menos 8 caracteres.")
            continue

        if  not any(caracter.isdigit() for caracter in senha):
            print("Senha fraca")
            continue

        print("Senha válida!")
        

    except ValueError:
        print("Operação inválida.")





