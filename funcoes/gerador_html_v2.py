#!/usr/bin/python3

def tag_bloco(texto, classe="success", inline=False):
    tag = "span" if inline else "div"
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == "__main__":
    print(tag_bloco("bloco"))
    print(tag_bloco("Inline e classe", "info", True))
    print(tag_bloco("Inline", inline=True))
    print(tag_bloco(inline=True, texto="Inline"))
    print(tag_bloco("Falhou", classe="error"))
