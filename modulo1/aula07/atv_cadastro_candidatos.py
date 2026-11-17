print("Bem-Vindo ao Cadastro de Candidatos")
print()

nome_candidato = (input("Por favor, informe seu primeiro nome: "))
idade = int(input("Agora, informe sua idade: "))

for i in range(1, 13):
    print(f"Olá, {nome_candidato}", i)

if idade < 18:
    print("Você não pode participar.")
else:
    telefone = input("Telefone: ")
    email = input("Email: ")

    print("Cadastro realizado.")