# Aula sobre listas, tuplas, sets e dicionários

lista_compras1 = ["vinagre", "sabonete", "açúcar", "pano de chão"]

print(lista_compras1)

lista_frutas = ["maçã", "banana", "banana", "açúcar"]

print(lista_frutas)

soma_total_lista = lista_compras1 + lista_frutas

print(soma_total_lista)

soma_total_lista += ["bombril"]
print(soma_total_lista)
soma_total_lista.append("goiaba")
print(soma_total_lista)

soma_total_lista.insert(2, "saca de arroz")
soma_total_lista.pop(6)
print(soma_total_lista)

soma_total_lista.remove("açúcar")
print(soma_total_lista)

compras_dezembro=soma_total_lista.copy()
print(compras_dezembro)
print()
print(soma_total_lista)

tupla_compras = tuple(soma_total_lista) 
print(tupla_compras)

print("Socorro")