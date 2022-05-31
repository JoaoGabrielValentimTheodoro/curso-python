pessoa = {"nome": "João Gabriel", "idade": 21,
          "cursos": ("Python", "Web Moderno", "Informática")}
# print(type(pessoa))
# print(dir(dict))

print(len(pessoa))
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["cursos"])
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get("idade"))
print(pessoa.get("tag"))
print(pessoa.get("tag", []))
