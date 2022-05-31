tupla = tuple()
tupla = ()  # Declarar tupla
# Expreção de declaração de string -> Não é um indice na tupla
tupla = ("Hello")
print(type(tupla))
tupla = ("World", )  # Elemento declarado em uma tupla
# print(dir(tuple)) -> Métodos de tuple
# print(help(tuple)) -> Ajuda
print(type(tupla))
# tupla[0] = "Hello World" -> TypeError
# -> tuple' object does not support item assignment
cores = ("Vermelho", "Verde", "Azul", "Laranja", "Azul")
print(cores[0])
print(cores[-1])
print(cores[1:])

print(cores.index("Laranja"))
print(cores.count("Azul"))
print(len(cores))
