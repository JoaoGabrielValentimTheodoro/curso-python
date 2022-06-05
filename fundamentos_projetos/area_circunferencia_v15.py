#!/home/joaogvt/.pyenv/versions/3.10.4/bin/python
from math import pi
import sys
import errno


class TerminalColor:
    ERRO = "\033[91m"
    NORMAL = "\033[0m"


def help():
    print("É necessaŕio informar o raio do circulo.")
    print(f"{sys.argv[0][2:-3]} <raio>")


def circulo(raio):
    area_circunferencia = pi * float(raio) ** 2
    return area_circunferencia


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERRO +
              "O Raio deve ser valor númerico" + TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)  # Argumento inválido

    raio = sys.argv[1]
    area_circunferencia = circulo(raio)
    print(f"Área da Circunferencia: {area_circunferencia}")
