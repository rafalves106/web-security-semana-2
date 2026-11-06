"""Checador de cookies e cabeçalhos: para cada página da lista, mostra o código de status,
os cabeçalhos de segurança e os atributos de cada cookie.
Procure por ">>> PARTE" neste arquivo: são as 3 partes que faltam. O resto já funciona."""
from urllib.request import urlopen

PAGINAS = [
    "http://localhost:8080/protegida",
    "http://localhost:8080/simples",
    "http://localhost:8080/cookie-fraco",
    "http://localhost:8080/cookie-forte",
]
CABECALHOS = ["Strict-Transport-Security", "X-Content-Type-Options"]
ATRIBUTOS = ["HttpOnly", "Secure", "SameSite"]


def pedir(endereco):
    """Pede a página ao site de laboratório e devolve a resposta."""
    return urlopen(endereco)


def conferir_cabecalhos(resposta):
    """Para cada nome de CABECALHOS, escreve o nome e 'tem' ou 'falta'."""
    for c in CABECALHOS:
        print(c + ":", "tem" if c in resposta.headers else "falta")


def conferir_cookies(resposta):
    """Para cada cookie da resposta, escreve o nome e 'tem' ou 'falta' para cada atributo de ATRIBUTOS."""
    for cookie in resposta.headers.get_all("Set-Cookie", []):
        print("cookie: " + cookie.split("=")[0])
        for atributo in ATRIBUTOS:
            print(atributo + ":", "tem" if atributo in cookie else "falta")
    # >>> PARTE 2: percorra resposta.headers.get_all("Set-Cookie", []) com um for. Para cada cookie, mostre "cookie:"
    # e o nome (cookie.split("=")[0]). Depois, para cada atributo de ATRIBUTOS, mostre o atributo, dois-pontos
    # e "tem" ou "falta", perguntando se o atributo está no texto do cookie, como no passo 6 da ponte.


def checar(paginas):
    print("Checador de cookies e cabeçalhos")

    for p in paginas:
        print("--- " + p)

        resposta = pedir(p)
        status = resposta.status
        print("código de status: " + str(status))
        conferir_cabecalhos(resposta)
        conferir_cookies(resposta)
    # >>> PARTE 3: para cada endereço da lista, mostre "--- " e o endereço. Peça a página com pedir(endereco)
    # e mostre "código de status:" e resposta.status. Depois chame conferir_cabecalhos(resposta)
    # e conferir_cookies(resposta).


if __name__ == "__main__":
    checar(PAGINAS)
