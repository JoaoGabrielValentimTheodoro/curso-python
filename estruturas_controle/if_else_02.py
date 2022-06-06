#!/home/joaogvt/.pyenv/versions/3.10.4/bin/python
def faixa_etaria(idade):
    if 0 <= idade < 18:
        return "Menor de Idade"
    if idade in range(18, 65):
        return "Adulto"
    if idade in range(65, 100):
        return "Melhor idade"
    if idade >= 100:
        return "Centenário"
    else:
        return "Idade inválida"


if __name__ == "__main__":
    for idade in (17, 35, 87, 113, -2, 0):
        print(f"Idade: {faixa_etaria(idade)}")
