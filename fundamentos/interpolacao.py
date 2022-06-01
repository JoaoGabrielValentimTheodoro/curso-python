from string import Template
nome, idade = "João", 21
# Mais antiga, menos recomendada
# print("nome: %s, idade: %d" % (nome, idade))
print("Nome: {0}, Idade: {1}".format(nome, idade))  # Recomandado - < 3.6
print(f"Nome: {nome}, Idade: {idade} {2 ** 8 + 1}")  # 3.6

s = Template("Nome: $nome, Idade: $idade")
print(s.substitute(nome=nome, idade=idade))
