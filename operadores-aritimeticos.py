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

idade = 18
altura = 1.50
resultado = (idade >= 18) and (altura >= 1.60) # verifica se a pessoa é maior de idade e tem altura maior ou igual a 1.60
print("Resultado da verificação de idade e altura:", str (resultado))
msg = "você é maior atendeu aos requisitos e está apto a entrar no evento" if resultado else "você não atendeu aos requisitos e não está apto a entrar no evento"
print(msg)

irigador_sul = 'desligado'
irigador_norte = 'desligado'
registro = (irigador_sul == 'desligado') or (irigador_norte == 'desligado') # verifica se o irrigador sul está desligado e o norte aberto
print("Resultado da verificação dos irrigadores:", str (registro))
msg = "irigadores norte e sul estão desligados no momento" if registro else "irigadores norte e sul estão ligados no momento"
print(msg)
conta_bancaria = 1000
conta_bancaria = not conta_bancaria
print ("saldo da conta bancaria:", str (conta_bancaria))
msg = "saldo da conta bancária está zerado" if conta_bancaria else "saldo da conta bancária tem dinheiro"
print (msg)