# Exercício 07

N = [12, 43, 54, 7, 22, 8, 19]

P = []
I = []

for n in N:
    if n % 2 == 0:
        P.append(n)
    else:
        I.append(n)
        
print(I)

# Exercício 08

def soma(n01, n02, n03):
    return n01 + n02 + n03
    
print(f'Soma: {soma(5, 10, 5)}')

# Exercício 09

def checar_aluno(nome, nota):
    if nota < 7:
        return False
    else:
        return True
        
if checar_aluno('Gabriel', 10):
    print('Situação: Aprovado!')
else:
    print('Situação: Reprovado!')
