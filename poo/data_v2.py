#!/usr/bin/python3
class Data:
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"


if __name__ == "__main__":
    d1 = Data(12, 12, 2022)
    # d1.dia = 12
    # d1.mes = 12
    # d1.ano = 2022
    print(d1)

    d2 = Data()
    # d2.dia = 20
    # # d2.mes = 12
    # # d2.ano = 2022
    print(d2)
