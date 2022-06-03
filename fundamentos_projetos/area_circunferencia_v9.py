#!/home/joaogvt/.pyenv/versions/3.10.4/bin/python
from math import pi


def circulo(raio):
    area_circunferencia = pi * float(raio) ** 2
    return area_circunferencia


if __name__ == "__main__":
    raio = input("Informe o Raio: ")
    area_circunferencia = circulo(raio)
    print(f"Área da Circunferencia: {area_circunferencia}")
