#!/usr/bin/python3
# 0, 1, 1, 2, 3, 5,8, 13, 21...

def fibonnaci(quantidade):
    resultado = [0, 1]
    for _ in range(2, quantidade):  # _ variável não usada
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == "__main__":
    for valor in fibonnaci(20):
        print(valor, end=", ")
