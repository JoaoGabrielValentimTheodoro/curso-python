#!/usr/bin/python3
class Data:
    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"


if __name__ == "__main__":
    d1 = Data()
    d1.dia = 12
    d1.mes = 12
    d1.ano = 2022
    print(d1)

    d2 = Data()
    d2.dia = 14
    d2.mes = 12
    d2.ano = 2022
    print(d2)
