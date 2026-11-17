# Atividade 3:

'''Nesta atividade o objetivo é calcular
o rendimento de um seu carro na praça..'''

print("Bem-vindo à calculadora de resultado financeiro!")

# Coleta de dados necessários para o cálculo.
odometro_inicial = float(input("Digite a quilometragem inicial: "))
odometro_final = float(input("Digite a quilometragem final: "))
combustivel_gasto = float(input("Digite quantos litros foram gastos: "))
combustivel_preco = 6.15
total_corridas = float(input("Digite quanto foi o rendimento total das corridas: "))
print("")

# Cálculo.
percurso = odometro_final - odometro_inicial
print("O percurso total foi: ", percurso, "Km")
gasto_km = percurso / combustivel_gasto
print("O consumo médio p/ km foi: ", gasto_km, "L")
custo_combustivel = combustivel_gasto * combustivel_preco
print("O gasto em combustível foi: R$", custo_combustivel)
lucro = total_corridas - custo_combustivel
print("O lucro é: R$", lucro)
print("")

# Status de lucro.
if lucro > 0:
    print("Situação: LUCRO")
elif lucro == 0:
    print("Situação: EMPATE, lucro paga o custo")
else:
    print("Situação: PREJUÍZO")