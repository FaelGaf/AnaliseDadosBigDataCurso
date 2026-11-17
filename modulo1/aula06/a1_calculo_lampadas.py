# Atividade 1:

'''Nesta atividade o objetivo é calcular e imprimir
o número de lâmpadas necessárias para iluminar um determinado 
cômodo de uma residência.'''

print("Bem-vindo à calculadora de lâmpadas!")

# Coleta de dados necessários para o cálculo.
potencia = 3
bocal_m2 = 3
comprimento = float(input("Digite o comprimento em metros: "))
largura = float(input("Digite a largura em metros: "))

# Cálculo de quantas lâmpadas são necessárias.
area = comprimento * largura
qtd_bocais = area / bocal_m2

# Caso de resposta com decimais.
if qtd_bocais == int(qtd_bocais):
    print("A quantidade de lâmpadas necessárias são:", qtd_bocais)
elif qtd_bocais != int(qtd_bocais):
    print("A quantidade de lâmpadas necessárias são:", int(qtd_bocais + 1))
else:
    print("Erro de cálculo. Por favor, tente novamente.")
