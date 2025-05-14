def main ():
  alunos = []
  for i in range(5):
    print(f"\naluno {i+1}")
    nome = input("Digite seu nome: ")
    av1 = float(input("Digite sua nota na primeira avaliação: "))
    av2 = float(input("Digite sua nota na segunda avaliação: "))
    media = (av1 + av2)/2
    
    alunos.append([nome, av1, av2, media])
    print("\n---Dados dos Alunos---")
    for aluno in alunos:
        print(f"NOME: {aluno[0]} | AV1:{aluno[1]:.2f} | AV2:{aluno[2]:.2f} | Média: {aluno[3]:.2f}")

if __name__=="__main__":
   main()