# operadores aritmeticos 
# ordem de precedencia dos operadores 
# parenteses 
# potenciacao 
# multiplicacao e divisao 
# soma e subtracao (da esquerda para direita)
# Exemplo de uso de operadores aritméticos em Python 
# x = y = z = 0
# y = int(input("Digite um valor para y: "))
# z = int(input("Digite um valor para z: "))
# x = y + z
# print("Resultado da soma de y e z:", x)

# operadores de comparacao
# == (igualdade)
# != (diferente)
# > (maior que)
# < (menor que)
# >= (maior ou igual a)
# <= (menor ou igual a)
# Um sinal de igualdade (==) é usado para comparar valores, enquanto um sinal de atribuição (=) é usado para atribuir valores a variáveis.
x = y = z = False
y = int(input("digite um valor para y:"))
z = int(input("digite um valor para z:"))
x = y != z # verifica se y é diferente de z
print("Resultado da comparação de y e z:", x)

x = y + z # soma os valores de y e z
print("resultado da soma de y e z:",x)

media = (y == z) >= x # verifica se a média é igual ou maior que x
print("resultado da comparacao de y e z com x:", media)

# operadores logicos Or, Not e And
# os operadores logicos sao usados para aplicar logica booleana em expressoes (A álgebra booleana é o ramo da álgebra na qual as variáveis podem assumir somente os valores falso e verdadeiro (comumente representados por 0 e 1). Os operadores fundamentais são conjunção (e-lógico), disjunção (ou-lógico) e negação. A álgebra booleana é fundamental em programas de computador, em particular nas expressões ...lógicas e na lógica proposicional.)
x = y = z = False
x = int(input("insira um valor para x:"))
y = int(input("digite um valor para y:"))
z = int(input("digite um valor para z:"))
x = False if y == z else True # verifica se y é igual a z
print("Resultado da comparação de y e z com x:", x)
y = (not x == z) # verifica se y é diferente de z
print("Resultado da comparação de y e z com x:", y)

idade = 21
altura = 1.50
print("digite sua idade:")
print("digite sua altura:")
print('idade:', idade)  # Exibe a idade
print('altura:', altura)  # Exibe a altura
print('idade and altura:', idade and altura)  # Retorna a última expressão avaliada se ambas forem verdadeiras

