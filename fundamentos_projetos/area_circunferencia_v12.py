#!/home/joaogvt/.pyenv/versions/3.10.4/bin/python
from math import pi
import sys


def help():
    print("É necessaŕio informar o raio do circulo.")
    print(f"{sys.argv[0][2:-4]} <raio>")


def circulo(raio):
    area_circunferencia = pi * float(raio) ** 2
    return area_circunferencia


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
    else:
        raio = sys.argv[1]
        area_circunferencia = circulo(raio)
        print(f"Área da Circunferencia: {area_circunferencia}")
