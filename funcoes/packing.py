#!/usr/bin/python3

def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == "__main__":
    print(soma_2(2, 4))
    print(soma_3(2, 4, 6))

    # Packing
    print(soma_n(1, 1, 1, 1, 1, 1, 1, 1))

    # Unpacking
    tupla_nums = (5, 5, 2)
    print(soma_n(*tupla_nums))
    lista_nums = [5, 5, 4]
    print(soma_n(*lista_nums))
