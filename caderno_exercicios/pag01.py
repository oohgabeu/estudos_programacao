# Exercício 01

peso = int(input('Peso: '))

if peso > 50: 
  excesso = peso - 50
else:
  excesso = 0

multa = excesso * 4

if multa == 0:
  print(f'Você pescou {peso} quilos... Multa não aplicada.')
else:
  print(f'Você pescou {peso} quilos... Multa aplicada! [R${multa}]')
  
# Exercício 02

morangos = int(input('Morangos: '))
macas = int(input('Maças: '))

peso_total = morangos + macas

if morangos > 5:
  preco_morango = 2.20
else:
  preco_morango = 2.50

if macas > 5:
  preco_maca = 1.50
else:
  preco_maca = 1.80

preco_total = (morangos * preco_morango) + (macas * preco_maca)

preco_desconto = preco_total - ((preco_total * 10) / 100)

if peso_total > 8 or preco_total > 25:
  print(f'Você recebeu 10% de desconto! Valor: R${preco_desconto}')
else:
  print(f'Valor: R${preco_total}')
  
# Exercício 03

p01 = input('Telefonou para a vítima [S/N]? ')
p02 = input('Esteve no local do crime [S/N]? ')
p03 = input('Mora perto da vítima [S/N]? ')
p04 = input('Devia para a vítima [S/N]? ')
p05 = input('Já trabalhou com a vítima [S/N]? ')

cont = 0
for pergunta in [p01, p02, p03, p04, p05]:
  if pergunta == 'S':
    cont += 1

if cont == 2:
  print('Interrogado é suspeito...')
elif cont in range (3, 5):
  print('Interrogado deve ser cúmplice.')
elif cont == 5:
  print('Interrogado é o assassino!')
else:
  print('Interrogado liberado.')
