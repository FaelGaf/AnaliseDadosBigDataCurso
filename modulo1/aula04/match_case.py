
# Uso do match case:

# Antes: IF ELSE

print("##### Atendimento Express #####")

categorias = ["Massas", "Bebidas", "Petiscos", "Doces", "Salgados", "Pizza"
              "Churrasco", "Lanches", "Comida Japonesa", "Pastel"]
print(categorias)

pergunta = input("Escolha uma das opções acima:")

match pergunta:
    case "Massas":
        print("Dia das massas, com rodízio e descontos é toda quarta-feira!")
    case "Bebidas":
        print("Dia das bebidas, com rodízio e descontos é toda quarta-feira!")
    case "Doces":
        print("Dia das doces, com rodízio e descontos é toda quarta-feira!")
    case _:
        print("Categoria não encontrada.")
