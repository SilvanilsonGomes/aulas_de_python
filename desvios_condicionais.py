# desvios condicionais if, elif, else
# como  o proprio nome ja sugere essa trestags sao condicionais que vao atuar para cria condicoes especificas ou atendelas dentro de um programa
# exemplo de uso de desvios condicionais em Python 
n1 = n2 = 0.0
media = 0.0 
n1 = float(input("insira a nota 1:"))
n2 = float(input("insira a nota 2:"))
media = (n1+ n2) / 2 
if (media >= 7.0):
    print("aprovado com sucesso")
elif(media >=6.0) and (media <7.0):
    print("você está de recuperação")
else:
    print("você foi reprovado")
print("a sua media foi:", media)


