#!/usr/bin/python3
# [ expressão for item in list if condicional ]

if __name__ == "__main__":
    dobros = [i * 2 for i in range(11) if i % 2 == 0]
    print(dobros)

    # Versão normal
    dobros = []
    for i in range(11):
        if i % 2 == 0:
            dobros.append(i * 2)
    print(f"{dobros}")
