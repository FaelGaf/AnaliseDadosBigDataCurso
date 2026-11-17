# Atividade 2:

'''Nesta atividade o objetivo é calcular e escrever
a quantidade de caixas de azulejos para se colocar em
todas as suas paredes.'''

print("Bem-vindo à calculadora de pisos!")

# Coleta de dados necessários para o cálculo.
caixa_azulejo = 1.5
comprimento = float(input("Digite o comprimento da parede em metros: "))
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

# Cálculo de quantas caixas são necessárias.
comprimento_c = altura * comprimento
largura_c = altura * largura
area = comprimento_c + largura_c
qtd_azulejos = area / caixa_azulejo

if qtd_azulejos == int(qtd_azulejos):
    print("A quantidade de caixas necessárias são:", qtd_azulejos)
elif qtd_azulejos != int(qtd_azulejos):
    print("A quantidade de caixas necessárias são:", int(qtd_azulejos + 1))
else:
    print("Erro de cálculo. Por favor, tente novamente.")