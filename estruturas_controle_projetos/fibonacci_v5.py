#!/usr/bin/python3
# 0, 1, 1, 2, 3, 5,8, 13, 21...

def fibonnaci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == "__main__":
    for valor in fibonnaci(29000):
        print(valor, end=", ")
