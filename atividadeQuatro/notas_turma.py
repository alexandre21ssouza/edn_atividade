# Atividade 2

# Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve
# continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. O
# programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média 
# da turma. Notas = [] -> len(Notas)



notas = []

while True:
    try:
        nota = input("Digite a nota da turma ou fim para terminar: ").lower()

        if nota == "fim":
            break

        notas.append(float(nota))


        
    except ValueError:
        print("operação inválida")


resultado = sum(notas) / len(notas)
print(resultado)