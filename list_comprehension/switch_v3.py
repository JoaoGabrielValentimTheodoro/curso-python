#!/usr/bin/python3


def get_tipo_dia(dia):
    dias = {
        (1, 7): "Fim de semana",
        tuple(range(2, 7)): "Dias da semana"
    }
    dia_escolhido = (tipo for numero, tipo in dias.items() if dia in numero)
    return next(dia_escolhido, "** Dia inválido **")


if __name__ == "__main__":
    for dia in range(0, 9):
        print(f"{dia} : {get_tipo_dia(dia)}")
