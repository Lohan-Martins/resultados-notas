# Função para imprimir uma linha horizontal
def print_linha(larguras):
    linha = "+"
    for largura in larguras:
        linha += "-" * (largura + 2) + "+"
    print(linha)

# Função para imprimir uma linha da tabela
def print_linha_tabela(valores, larguras):
    linha = "|"
    for valor, largura in zip(valores, larguras):
        linha += f" {valor:{largura}} |"
    print(linha)

# Dados da tabela
titulos = ["Nome", "Idade", "Cidade"]
dados = [
    ["João", 30, "São Paulo"],
    ["Maria", 25, "Rio de Janeiro"],
    ["Pedro", 35, "Belo Horizonte"]
]

# Calcula as larguras das colunas
larguras = [max(len(str(dado)) for dado in coluna) for coluna in zip(titulos, *dados)]

# Imprime a tabela
print_linha(larguras)
print_linha_tabela(titulos, larguras)
print_linha(larguras)
for dado in dados:
    print_linha_tabela(dado, larguras)
print_linha(larguras)