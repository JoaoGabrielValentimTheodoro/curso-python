lista = []  # mutável -> sequência
print(type(lista))
# print(dir(lista))
print(len(lista))
lista.append(1)
lista.append(2)
print(len(lista))

# Não é boa prática misturar tipos em lista
nova_lista = [1, 2, "João", "Gabriel"]
print(nova_lista)
nova_lista.remove(1)  # removendo elemento 1
print(nova_lista)
nova_lista.reverse()  # reverter ordem da lista
print(nova_lista)
