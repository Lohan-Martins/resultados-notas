import requests

url = "https://raw.githubusercontent.com/Lohan-Martins/resultados-notas/main/dados/dados.json"

resposta = requests.get(url)


dados = resposta.json();

alunos_aprovados = []
alunos_recuperacao = []
alunos_reprovados = []

for objeto in dados:
  if objeto["Nota"] >= 600:
    alunos_aprovados.append(objeto)
  elif objeto["Nota"] >= 300:
    alunos_recuperacao.append(objeto)
  else:
    alunos_reprovados.append(objeto)

alunos_aprovados.sort(key=lambda x: x["Nome"])

melhor_aluno = max(alunos_aprovados, key=lambda x: x["Nota"]);
print(f'Melhor aluno: {melhor_aluno["Nome"]}')
print()  # Isso imprimirá uma linha em branc

print('----- Alunos aprovados -----')
for aluno in alunos_aprovados:
  print(f'{aluno["Nome"]} - {aluno["Nota"]}')

print()  # Isso imprimirá uma linha em branco

print('----- Alunos de recuperação -----')
for aluno in alunos_recuperacao:
  print(f'{aluno["Nome"]} - {aluno["Nota"]}')

print()  # Isso imprimirá uma linha em branco

print('----- Alunos reprovados -----')
for aluno in alunos_reprovados:
  print(f'{aluno["Nome"]} - {aluno["Nota"]}')