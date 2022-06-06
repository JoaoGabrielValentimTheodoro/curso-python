#!/home/joaogvt/.pyenv/versions/3.10.4/bin/python

# Conceito    Notas
# A           De 10,0 á 9,1
# A-          De 9,0 á 8,1
# B           De 8,0 á 7,1
# B-          De 7,0 a 6,1
# C           De 6,0 á 5,1
# C-          De 5,0 á 4,1
# D           De 4,0 á 3,1
# D-          De 3,0 á 2,1
# E           De 2,0 á 1,1
# E-          De 1,0 á 0,0

# Para notas maiores do que 10 e menores do que 0 será impresso "Nota Inválida"

def nota_para_conceito(valor):
    nota = float(valor)
    if nota <= 10 and nota >= 9.1:
        return "A"
    if nota <= 9 and nota >= 8.1:
        return "A-"
    if nota <= 8 and nota >= 7.1:
        return "B"
    if nota <= 7 and nota >= 6.1:
        return "B-"
    if nota <= 6 and nota >= 5.1:
        return "C"
    if nota <= 5 and nota >= 4.1:
        return "C-"
    if nota <= 4 and nota >= 3.1:
        return "D"
    if nota <= 3 and nota >= 2.1:
        return "D-"
    if nota <= 2 and nota >= 1.1:
        return "E"
    if nota <= 1 and nota >= 0:
        return "E-"
    else:
        return "Nota Inválida"


if __name__ == "__main__":
    nota = input("Informe a nota do aluno: ")
    conceito = nota_para_conceito(nota)
    print(conceito)
