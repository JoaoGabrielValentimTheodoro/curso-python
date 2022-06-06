#!/home/joaogvt/.pyenv/versions/3.10.4/bin/python
palavra = "paralelepipedo"
for letra in palavra:
    print(letra, end=",")
print("Fim")

aprovados = ["Lucas", "Heliton", "Patricia", "Fernando", "João"]
for posicao, nome in enumerate(aprovados):
    print(f"{posicao + 1}) - {nome}")

dias_semana = ["Domingo", "Segunda", "Terça",
               "Quarta", "Quinta", "Sexta", "Sabado"]

for dia in dias_semana:
    print(f"Hoje é {dia}")

for letra in set("Muito Legal"):
    print(letra)

for numero in (1, 2, 3, 4):
    print(numero)
