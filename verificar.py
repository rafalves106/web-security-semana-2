"""Confere os 4 critérios do Projeto 2 contra o site de laboratório (lab/servidor.py precisa estar ligado)."""
import io
import subprocess
import sys
from contextlib import redirect_stdout

import checador

OK, FALHA = "OK    ", "FALHOU"
falhas = 0


def criterio(nome, passou, dica):
    global falhas
    print(f"{OK if passou else FALHA} {nome}" + ("" if passou else f"  -> {dica}"))
    falhas += 0 if passou else 1


def linhas(funcao, endereco):
    """Roda a função do aluno sobre a página e devolve o que ela escreveu."""
    buffer = io.StringIO()
    try:
        with redirect_stdout(buffer):
            funcao(checador.pedir(endereco))
    except Exception as erro:
        return ["erro: " + type(erro).__name__]
    return buffer.getvalue().splitlines()


saida = subprocess.run([sys.executable, "checador.py"], capture_output=True, text=True, timeout=30).stdout.splitlines()
base = "http://localhost:8080/"
paginas = ["protegida", "simples", "cookie-fraco", "cookie-forte"]

criterio("a) mostra o status de cada página",
         all(f"--- {base}{p}" in saida for p in paginas) and saida.count("código de status: 200") == 4,
         "PARTE 3: para cada página, mostre '--- ' e o endereço, e 'código de status:' e o resultado")

criterio("b) marca tem ou falta para cada cabeçalho de segurança",
         linhas(checador.conferir_cabecalhos, base + "protegida") == ["Strict-Transport-Security: tem", "X-Content-Type-Options: tem"]
         and linhas(checador.conferir_cabecalhos, base + "simples") == ["Strict-Transport-Security: falta", "X-Content-Type-Options: falta"],
         "PARTE 1: conferir_cabecalhos() deve escrever 'NOME: tem' ou 'NOME: falta' para os dois cabeçalhos")

criterio("c) mostra os atributos de cada cookie",
         linhas(checador.conferir_cookies, base + "cookie-forte") == ["cookie: sid", "HttpOnly: tem", "Secure: tem", "SameSite: tem"]
         and linhas(checador.conferir_cookies, base + "cookie-fraco") == ["cookie: tema", "HttpOnly: falta", "Secure: falta", "SameSite: falta"]
         and linhas(checador.conferir_cookies, base + "simples") == [],
         "PARTE 2: conferir_cookies() deve escrever o nome e 'ATRIBUTO: tem' ou 'ATRIBUTO: falta'; página sem cookie não escreve nada")

esperada = [
    "Checador de cookies e cabeçalhos",
    "--- http://localhost:8080/protegida", "código de status: 200",
    "Strict-Transport-Security: tem", "X-Content-Type-Options: tem",
    "--- http://localhost:8080/simples", "código de status: 200",
    "Strict-Transport-Security: falta", "X-Content-Type-Options: falta",
    "--- http://localhost:8080/cookie-fraco", "código de status: 200",
    "Strict-Transport-Security: falta", "X-Content-Type-Options: falta",
    "cookie: tema", "HttpOnly: falta", "Secure: falta", "SameSite: falta",
    "--- http://localhost:8080/cookie-forte", "código de status: 200",
    "Strict-Transport-Security: falta", "X-Content-Type-Options: falta",
    "cookie: sid", "HttpOnly: tem", "Secure: tem", "SameSite: tem",
]
criterio("d) percorre a lista inteira", saida == esperada,
         "PARTE 3: a saída deve ter as 4 páginas, na ordem, com o texto exato do enunciado")

print("pronto" if falhas == 0 else f"{falhas} criterio(s) falhando")
sys.exit(1 if falhas else 0)
