# print(dir(str))
nome = "Saulo Pedro"
print(nome)
print(nome[0])
# nome[0] = "P" # TypeError -> String é imutável
# 'marca d'agua' -> Erro de Sintaxe
# para texto com aspas simples dentro de aspas simples use
# \ -> para fazer parte do texto
print('Dias D\'Avila' == 'Dias D\'Avila')
# print("Teste \" Teste")
texto = 'Texto Entre Apostrofos pode ter "aspas".'
print(texto)

doc = """ Texto com multiplas
...\tlinhas
"""

print("Texto com multiplas\n...\tlinhas")
print(doc)

doc2 = ''' Também é possível com
aspas simples
'''
print(doc2)
