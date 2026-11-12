# Atividade

'''O objetivo é, dadas as 4 notas de 10 estudantes, calcular 
sua média e, com base nela, emitir a mensagem de status correspondente: 
1. Aprovado: Média estritamente maior que 7;
2. Recuperação: Média entre 5 (inclusive) e 7 (inclusive);
3. Reprovação: Média estritamente abaixo de 5.'''

# Saudação teste inicial
print("Bem-vindo à calculadora de nota")

for i in range(1, 11):
    try:
        print("Estudante", i)

        nota_1 = int(input("Insira sua primeira nota:"))
        nota_2 = int(input("Insira sua segunda nota:"))
        nota_3 = int(input("Insira sua terceira nota:"))
        nota_4 = int(input("Insira sua quarta nota:"))

        media = nota_1 + nota_2 + nota_3 + nota_4
        total = media / 4
        print("Sua média é: ", total)

        if total <= 5:
            print("Reprovado")
        elif total >= 7:
            print("Aprovado")
        elif total > 5 and total < 7:
            print("Em Recuperação")

    except ValueError:
        print("Entrada inválida. Tente novamente.")