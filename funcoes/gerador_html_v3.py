#!/usr/bin/python3

def tag_bloco(conteudo, classe="success", inline=False):
    tag = "span" if inline else "div"
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


def tag_lista(*itens):
    lista = "".join(f'<li>{item}</li>' for item in itens)
    return f"<ul>{lista}</ul>"


if __name__ == "__main__":
    print(tag_bloco("bloco"))
    print(tag_bloco("Inline e classe", "info", True))
    print(tag_bloco("Inline", inline=True))
    print(tag_bloco(inline=True, conteudo="Inline"))
    print(tag_bloco("Falhou", classe="error"))
    print(tag_bloco(tag_lista("Heloisa", "Heliton", "João", "Helena")))
