#!/home/joaogvt/.pyenv/versions/3.10.4/bin/python
PALAVRAS_PROIBIDAS = {"futebol", "religião", "politica"}

textos = {
    "Sicrano odeia futebol e politica",
    "Fulana ama futebol e politica",
    "Andar com o vô é muito bom"
}

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print("Texto possui pelomenos uma palavra proibida: ", palavra)
            found = True
            break

        if not found:
            print("Texto autorizado: ", texto)
