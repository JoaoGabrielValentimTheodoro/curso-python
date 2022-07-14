#!/usr/bin/python3

def tag_bloco(texto, classe="success"):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == "__main__":
    # Teste (assertions)
    assert tag_bloco("Incluido com sucesso") == \
        '<div class="success">Incluido com sucesso</div>'
    assert tag_bloco("Impossível excluir", "error") == \
        '<div class="error">Impossível excluir</div>'
    print(tag_bloco("bloco"))
