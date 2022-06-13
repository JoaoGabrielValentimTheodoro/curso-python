#!/usr/bin/python3

def todos_params(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")


if __name__ == "__main__":
    todos_params('a', 'b', 'c', 'd')
    todos_params(1, 2, 3, 4, legal=True, valor=12.98)
    todos_params("Trapésio", True, [1, 2, 3, 4], tamanho="M", fragil=False)
    todos_params(primeiro="Joel", segundo="Henrique")
    todos_params(terceiro="Lucas", quarto="Luiz")
