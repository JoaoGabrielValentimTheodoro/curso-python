#!/home/joaogvt/.pyenv/versions/3.10.4/bin/python
# while True:
#    print("Vai demorar muito")

from random import randint

numero_informado = -1
numero_secreto = randint(0, 9)

while numero_informado != numero_secreto:
    numero_informado = int(input("Informe um número: "))

print(f"Número Secreto {numero_secreto} foi encontrado.")
