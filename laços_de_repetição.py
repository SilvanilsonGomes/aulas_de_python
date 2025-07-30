# laços de repetição while e for 
# os lacos de repeticao servem pra repetir um bloco de código várias vezes, enquanto uma condição for verdadeira (while) ou para cada item em uma coleção (for).
number = 1
while (number <= 10):
    print(number) # caso esqueça esse print aqui dentro do bloco o laço vai exibir o proximo print como programado no laço. 
    number +=1 
print("o laço foi encerrado com sucesso")
# esse laço while vai repetir o bloco de código enquanto a variável number for menor ou igual a 10, e a cada iteração, ele vai somar 1 a number.

# python faz diferenciação entre letras maiusculas e minusculas por isso deve se ter atencao ao escrever o codigo e colocar letra ou palavra como condicao de parada o inicio use a funcao or pra compara as duas

nome = None # aqui a variavel nome recebe a varaiavel none que representa o vazio em python 
while True:
    print ('digite seu nome: ')
    nome = input() # aqui o input vai receber o nome digitado pelo usuario e armazenar dentro da variavel nome 
    print(f"seja bem vindo {nome}")
    if(nome == "encerra" or nome == "Encerra"):
        print("obrigado por usar o nosso sistema")
        break # o break vai encerra o bloco de repeticao 

# esse laço while vai continuar pedindo o nome do usuário até que ele digite "encerra" ou "Encerra", e quando isso acontecer, o laço será encerrado com o comando break.


# laço for e funcao range 
# (range é uma função que gera uma sequência de números, e é frequentemente usada com laços for para iterar sobre essa sequência.
# o laço for é usado para iterar sobre uma sequência (como uma lista, tupla ou string) e executar um bloco de código para cada item dessa sequência.

nome = None
matricula = 13840
while True:
    print('Bom dia qual seu nome:')
    nome = input()
    print(f'Olá {nome}, seja bem vindo ao planeta diario')
    for nome in [nome]:
        print(f'{nome} seu numero de matricula é {matricula}')
    break

