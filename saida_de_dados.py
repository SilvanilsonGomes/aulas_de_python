 # saida de dados com funcão print, format e f-strings 
# a função print é usada para exibir mensagens na tela, ela pode receber vários argumentos e também pode formatar a saída de dados.
# end='' é um argumento opcional que define o que será colocado no final da mensagem, por padrão é uma quebra de linha.
# sep='' é outro argumento opcional que define o separador entre os argumentos, por padrão é um espaço em branco.

nome = "silvanilson"
idade = 21 
estado_civil = "solteiro"
pontuação = 38
media = 700.45678987654
msg = f"meu nome é {nome}, tenho {idade} anos e sou {estado_civil}.\n"
print(msg + f" minha idade é {idade} somada com minha {pontuação} é igual a {idade + pontuação}.")
print(f"minha media é  {media:.2f}") # formatando a média com duas casas decimais isso evitar que o numero inteiro apareça congestonando o visual do arquivo 
# duas barras "\\" dentro do codigo no lugar certo da print significa adicionar uma barra no arquivo na hora de exibir a mensagem contida dentro de print
print("sou {nome}\\{idade}\\{estado_civil}".format(nome=nome, idade=idade, estado_civil=estado_civil)) # usando barras invertidas para formatar a string
print("sou {} tenho {} e sou {}".format(nome, idade, estado_civil)) # usando o método format para formatar a string 


