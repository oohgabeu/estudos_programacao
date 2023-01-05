# Exercício 04

numero = input('Digite um número: ')

numero_invertido = ''

cont = -1
for contagem in range(len(numero)):
  numero_invertido += numero[cont]
  cont -= 1

print(numero_invertido)

# Exercício 05

usuario = input('Usuário: ')
senha = input('Senha: ')

while usuario.lower() in senha.lower():
  print('Senha inválida!')
  senha = input('Senha: ')

print('Cadastro aceito.')

# Exercício 06

pop_a = 120000
pop_b = 200000

cresc_a = int((3 * pop_a) / 100)
cresc_b = int((1.5 * pop_b) / 100)

cont = 0
while pop_a < pop_b:
    pop_a += cresc_a
    pop_b += cresc_b
    cont += 1
    
print(f'Foram necessários {cont} anos!')
