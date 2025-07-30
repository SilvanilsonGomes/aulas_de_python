# desvios condicionais if, elif, else
# como  o proprio nome ja sugere essa trestags sao condicionais que vao atuar para cria condicoes especificas ou atendelas dentro de um programa
# exemplo de uso de desvios condicionais em Python 
n1 = n2 = 0.0
media = 0.0 
n1 = float(input("insira a nota 1:"))
n2 = float(input("insira a nota 2:"))
media = (n1+ n2) / 2 

# If cria uma condicinal dentro do programa, se a condicional for atendida o bloco de codigo dentro do if sera executado
# elif e else sao usados para criar outras condicoes, caso a primeira nao seja atendida
if (media >= 7.0):
    print("aprovado com sucesso")

    # Elif é usado para cria uma condicional de encadeamento, ouseja, se a primeira condicional do if nao for atendida o programa vai verificar a condicional do elif.
elif(media >=6.0) and (media <7.0):
    print("você está de recuperação")

    # Else é usado para criar uma condicional que será atendida caso nenhuma das anteriores seja.  
else:
    print("você foi reprovado")
print("a sua media foi:", media)


