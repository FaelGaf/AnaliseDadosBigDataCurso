
#Atividade 1:

'''
O objetivo é, recebidos 3 números inteiros, criar um programa que os mostre
ordenados em ordem crescente.
'''
#Comando inicial
print("Tangobalangodango")

'''Para que a ordem seja crescente, preciso que:
- o primeiro dígito seja menor que o segundo e o terceiro;
- o segundo dígito seja maior que o primeiro e igual ou menor que o terceiro
- o terceiro dígito seja maior que o primeiro e o segundo'''

digit_1 = int(input("Insira seu primeiro número"))
digit_2 = int(input("Insira seu segundo número"))
digit_3 = int(input("Insira seu terceiro número"))

if digit_1 <= digit_2 and digit_1 <= digit_3 and digit_2 <= digit_3:
    print(digit_1, digit_2, digit_3)
elif digit_1 <= digit_3 and digit_1 <= digit_2 and digit_3 <= digit_2:
    print(digit_1, digit_3, digit_2)
if digit_2 <= digit_2 and digit_1 <= digit_3 and digit_2 <= digit_3:
    print(digit_1, digit_2, digit_3)
elif digit_2 <= digit_3 and digit_1 <= digit_2 and digit_3 <= digit_2:
    print(digit_1, digit_3, digit_2)
if digit_3 <= digit_2 and digit_1 <= digit_3 and digit_2 <= digit_3:
    print(digit_1, digit_2, digit_3)
elif digit_3 <= digit_3 and digit_1 <= digit_2 and digit_3 <= digit_2:
    print(digit_1, digit_3, digit_2)