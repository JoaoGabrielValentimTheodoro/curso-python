from random import randint


def novo_nome():
    nomes = ("Carlito", "Luiz", "Felipe", "Juraci")
    return nomes[randint(0, len(nomes)-1)]
