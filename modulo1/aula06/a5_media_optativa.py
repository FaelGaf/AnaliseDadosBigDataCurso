# Atividade 5:

'''O objetivo é Calcular a média final de um aluno usando duas 
provas e uma prova optativa, considerando que a optativa 
substitui a menor nota das duas provas, caso tenha sido feita. 
Depois, informar se o aluno foi aprovado, reprovado ou ficou em recuperação.'''

# Saudação teste inicial
print("Bem-vindo à calculadora de nota")

nota_01 = float(input("Digite a primeira nota: "))
nota_02 = float(input("Digite a segunda nota: "))
optativa = float(input("Digite a nota optativa (0 se não fez): "))

if optativa == 0:
    media = (nota_01 + nota_02) / 2
elif nota_01 < nota_02:
    media = (optativa + nota_02) / 2
else:
    media = (nota_01 + optativa) / 2

print("Média:", media)

if media >= 6:
    print("Aprovado")
elif media < 3:
    print("Reprovado")
else:
    print("Recuperação")