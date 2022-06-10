#!/usr/bin/python3
# [ expressão for item in list if condicional ]

if __name__ == "__main__":
    dobro = [i * 2 for i in range(11)]
    print(f"{dobro}")

    # Versão normal
    dobros = []
    for i in range(11):
        dobros.append(i * 2)
    print(f"{dobros}")
