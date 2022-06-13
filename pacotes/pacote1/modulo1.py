print(f"Importado módulo {__name__} de {__package__}")


def soma(*valores):
    soma = 0
    for valor in valores:
        soma += valor
    return soma
