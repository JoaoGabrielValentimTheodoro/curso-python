print(True or False)
print(7 != 3 and 2 > 3)

# Tabela verdade do AND (binário/ operandos(2))
print(True and True)  # Verdadeiro (True)
print(True and False)  # Falso (False)
print(False and True)  # Falso (False)
print(False and False)  # Falso (False)
print(True and True and True and False and True and True)

# Tabela verdade do OR
print(True or True)  # Verdadeiro (True)
print(True or False)  # Verdadeiro (True)
print(False or True)  # Verdadeiro (True)
print(False or False)  # Falso (False)
print(True or True or True or False or True or True)

# Tabela lógica do XOR
print(True != True)
print(False != True)
print(True != False)
print(False != False)

# Operador de Negação (unário)
print(not True)
print(not False)

print(not 0)
print(not 1)
print(not not -1)
print(not True)
print(not False)
print(not not True)
print(not not False)

# Cuidado
print(True & True)
print(False | True)
print(True ^ True)

# True && True -> Erro

# AND Bit-a-Bit
# 3 = 11
# 2 = 10
print(3 & 2)

# OR Bit-a-Bit
# 3 = 11
# 2 = 10
print(3 | 2)

# XOR Bit-a-Bit
# 3 = 11
# 2 = 10
print(3 ^ 2)

# Um  pouco de Relaidade
saldo = 1000
salario = 4000
despesas = 2967

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario
meta = saldo_positivo and despesas_controladas
print(meta)
