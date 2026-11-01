# Projeto 2: Checador de cookies e cabeçalhos

### Objetivo

Você completa o Checador de cookies e cabeçalhos, o script da ponte. Ele pede uma lista de páginas ao site de laboratório e marca, para cada uma, o que tem e o que falta. Assim você prova que lê o status, os cabeçalhos e os cookies de uma resposta.

### Entregável

Um repositório público no GitHub com o `checador.py` completo. O repositório já traz o código-base pronto, menos as 3 partes marcadas, e o site de laboratório. Você completa as 3 partes marcadas com `>>> PARTE` no `checador.py`:

- Parte 1: a função `conferir_cabecalhos`, que escreve `tem` ou `falta` para cada cabeçalho de segurança.
- Parte 2: a função `conferir_cookies`, que escreve o nome e os atributos de cada cookie.
- Parte 3: a função `checar`, que pede cada página da lista e repete as duas conferências.

A saída esperada, com o texto exato:

```
Checador de cookies e cabeçalhos
--- http://localhost:8080/protegida
código de status: 200
Strict-Transport-Security: tem
X-Content-Type-Options: tem
--- http://localhost:8080/simples
código de status: 200
Strict-Transport-Security: falta
X-Content-Type-Options: falta
--- http://localhost:8080/cookie-fraco
código de status: 200
Strict-Transport-Security: falta
X-Content-Type-Options: falta
cookie: tema
HttpOnly: falta
Secure: falta
SameSite: falta
--- http://localhost:8080/cookie-forte
código de status: 200
Strict-Transport-Security: falta
X-Content-Type-Options: falta
cookie: sid
HttpOnly: tem
Secure: tem
SameSite: tem
```

Antes de entregar, rode `python3 verificar.py`: ele diz `OK` ou `FALHOU` para cada critério abaixo.

### Critérios de "pronto"

- A saída mostra `código de status: 200` para cada página da lista [8.t1, 12.t1].
- `conferir_cabecalhos` escreve `tem` ou `falta` para `Strict-Transport-Security` e `X-Content-Type-Options` [9.t1, 9.t3, 12.t2].
- `conferir_cookies` escreve `tem` ou `falta` para HttpOnly, Secure e SameSite de cada cookie [10.t2, 12.t2].
- Uma página sem cookie não escreve linha de cookie, e o script não para [12.t2].
- A saída é igual à saída esperada: as 4 páginas, na ordem [12.t3].

### Ferramentas esperadas

- Python 3, só com a biblioteca padrão (`urllib.request`).
- Dois terminais: um para `python3 lab/servidor.py`, outro para o checador.
- Referências: documentação do Python sobre `urllib.request.urlopen` e tutorial do Python sobre o `for`.

## Como rodar

Você precisa do Python 3 instalado. Abra dois terminais na pasta do projeto.

No primeiro, ligue o site de laboratório e deixe aberto:

```
python3 lab/servidor.py
```

No segundo, rode o checador e confira os critérios:

```
python3 checador.py
python3 verificar.py
```

No Windows, se `python3` não funcionar, use `py` no lugar.

## O que já vem pronto

- `lab/`: o site de laboratório (não mexa).
- `checador.py`: o código-base. Procure `>>> PARTE` e complete as 3 partes.
- `verificar.py`: confere cada critério e diz qual parte ainda falta.
