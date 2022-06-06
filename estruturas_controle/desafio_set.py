#!/home/joaogvt/.pyenv/versions/3.10.4/bin/python
PALAVRAS_PROIBIDAS = {"futebol", "religião", "politica"}

textos = {
    "Sicrano odeia futebol e politica",
    "Fulana ama futebol e politica",
    "Andar com o vô é muito bom"
}

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print(f"Texto possui palavras proibidas: {intersecao}")
    else:
        print(f"Texto autorizado: {texto}")
