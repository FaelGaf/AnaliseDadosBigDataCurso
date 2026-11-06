
### Contexto 1:

'''
Para que eu possa dirigir, eu preciso ter:
- documento (CNH) em posse;
- maioridade (+18 anos);
- não estar alcoolizado.
'''

pergunta1 = input("Você tem os documentos em mãos?")
pergunta2 = int(input("Qual a sua idade?"))
pergunta3 = input("Você consumiu bebida alcoólica antes de dirigir?")

if pergunta1 == "sim" and pergunta2 >= 18:
    print("Pode dirigir.")
elif pergunta1 == "sim" and pergunta3 == "sim":
    print("Não pode dirigir.")

# Contexto 2:
    
    '''
    Para me deslocar até o Senac Nova Iguaçu, posso utilizar:
    - trem;
    - ônibus;
    - metrô.
    '''


    trem = input("Você veio de trem?")
    onibus = input("Você veio de ônibus?")
    metro = input("Você veio de metrô?")


