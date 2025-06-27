# Atividade 3

# Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 
# 8 caracteres e conter pelo menos um número. O programa deve continuar pedindo senhas até 
# que uma válida seja inserida ou o usuário digite 'sair'.


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





