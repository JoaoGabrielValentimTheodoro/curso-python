trabalho_terca = True
trabalho_quinta = True

"""
    - Confirmando os dois trabalhos: TV de 50' + sorvete
    - Confirmando um trabalho: TV 32' + sorvete
    - Nenhum confirmado Fica em casa
"""

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta  # XOR
mais_saudavel = not sorvete

print("TV 50' = {} TV 32' = {} Sorvete = {} Saudavel = {}".format(
    tv_50, tv_32, sorvete, mais_saudavel))

# "{1}, {0}, {2}".format(tv_50, tv_32, "Resultado")
