def verificar_respostas(respostas_aluno):
    gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
    acertos = sum(1 for i in range(10) if respostas_aluno[i] == gabarito[i])
    return acertos

def main():
    total_alunos = 0
    acertos_alunos = []
    
    while True:
        total_alunos += 1
        respostas_aluno = []
        
        print(f"\nAluno {total_alunos}, responda as 10 questões:")
        
        for i in range(10):
            resposta = input(f"Questão {i + 1}: ").strip().upper()
            respostas_aluno.append(resposta)
        
        acertos = verificar_respostas(respostas_aluno)
        acertos_alunos.append(acertos)
        
        print(f"Total de acertos: {acertos} - Nota: {acertos} pontos.")
        
        continuar = input("Outro aluno vai utilizar o sistema? (s/n): ").strip().lower()
        if continuar != 's':
            break
    
    if total_alunos > 0:
        maior_acerto = max(acertos_alunos)
        menor_acerto = min(acertos_alunos)
        media_notas = sum(acertos_alunos) / total_alunos
        
        print(f"\nResultados Finais:")
        print(f"Maior Acerto: {maior_acerto}")
        print(f"Menor Acerto: {menor_acerto}")
        print(f"Total de Alunos: {total_alunos}")
        print(f"Média das Notas da Turma: {media_notas:.2f}")

if __name__ == "_main_":
    main()