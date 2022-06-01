pessoa = {"nome": "João Gabriel", "idade": 21,
          "cursos": ["Python", "Web Moderno", "Informática"]}
pessoa["idade"] = 22
pessoa["cursos"].append("Scala")
print(pessoa)
pessoa.pop("idade")
print(pessoa)
pessoa.update({"idade": 22, "sexo": "M"})
print(pessoa)
del pessoa["cursos"]
print(pessoa)
pessoa.clear()
print(pessoa)
