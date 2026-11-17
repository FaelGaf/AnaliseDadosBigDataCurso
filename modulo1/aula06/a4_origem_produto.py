# Atividade 4:

'''Nesta atividade o objetivo é imprimir o código
na tela a região de sua procedência'''

print("Pesquisar origem de código: 'exemplo: c1'")
print()

search_code = input("Digite o código: ")

#Busca pelo código correspondente:
match search_code:
    case "c1":
        print("Sul")
    case "c2":
        print("Norte")
    case "c3":
        print("Leste")
    case "c4":
        print("Oeste")
    case "c5" | "c6":
        print("Nordeste")
    case "c7" | "c8" | "c9":
        print("Sudeste")
    case "c10":
        print("Centro-Oeste")
    case "c11":
        print("Noroeste")
    case _:
        print("Importado") 