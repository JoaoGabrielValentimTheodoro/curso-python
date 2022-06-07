#!/usr/bin/python3


def imprimir(maximo, atual):
    # condição de parada
    if atual >= maximo:
        return
    print(atual)
    imprimir(maximo, atual+1)


if __name__ == "__main__":
    imprimir(100, 1)
