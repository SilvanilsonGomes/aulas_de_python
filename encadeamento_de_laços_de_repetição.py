# Encadeamento de laços de repetição
# laços de repetição é ate que simples pois como prorio nome ja fa ele vai se tratar de lacos de repeticao encadeados em um so bloco para criar uma estrutura mais complexa e funcional.
import random 
nome = None
turma = None
while True:
    nome = input('Bom dia qual seu nome:')
    turma = input('qual sua turma A ou B?') # graças ao input o usuario pode respoder seu nome e turma separados sem se preocupar em colocar tudo junto e nao armazenar corretamente as variaveis.  
    if (turma == "A"):
        number = random.randint(0,500) # essa linha de codigo é responsavel por cria aleatoriamente um numero de matricula entr 0 e 500.
        print(f'{nome} seu numero de matricula é {number}')
        break
    elif (turma == "B"):
        number = random.randint(500, 1000) 
        print(f'{nome} seu numero de matricula é {number}')
        break
print(f'Olá {nome}, seja bem vindo ao Instituto de Tecnologia e Inovação')
# Esse código solicita o nome do usuário e exibe uma mensagem de boas-vindas junto com o número de matrícula.

for number in range(0,10):
    number = random.randint(0,1000)
    print(f'o seu numero de matricula é {number}')
    # Esse laço for gera números aleatórios de matrícula entre 0 e 1000, exibindo-os para o usuário, usei ele de ase pra melhorar o bloco de cima que encadeia while e for.
