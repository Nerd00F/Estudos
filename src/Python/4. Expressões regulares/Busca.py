import re

teste = 'Programando em python'

padrao = re.search(r'em',teste)

if padrao:
  print(padrao.group())
else:
  print("Padrao nao encontrado")