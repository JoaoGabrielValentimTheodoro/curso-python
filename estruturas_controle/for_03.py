produto = {"nome": "Notebook Top", "preco": 12530.99,
           "importado": True, "estoque": 242}

for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(f"{chave} : {valor}")

print(chave, valor)  # valores são disponiveis fora do laço
