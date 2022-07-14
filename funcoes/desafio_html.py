#!/usr/bin/python3
ESPECIAIS = ("id")


def filtra_atributo(informados, valido):
    return " ".join(f'{k.split("_")[-1]}="{v}"'
                    for k, v in informados.items() if k in ESPECIAIS)


def tag(tag, *args, **kwargs):
    attr_css = " ".join(f"class={v}" or "" for k,
                        v in kwargs.items() if k == "html_css")
    html = "".join(conteudo for conteudo in args)
    return f'<{tag} {attr_css} {filtra_atributo(kwargs, args)}>{html}</{tag}>'


if __name__ == "__main__":
    print(
        tag("p",
            tag("span", "Curso de Python 3"),
            tag("strong", "Juraci Filho", id="jf"),
            tag("span", " e "),
            tag("strong", "Leonardo Leitao", id="ll"),
            tag("span", "."),
            html_css="alert")
    )
