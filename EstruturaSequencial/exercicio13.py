#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

#    Para homens: (72.7*h) - 58
#    Para mulheres: (62.1*h) - 44.7 

sexo = input('digite M para homem e F para mulher: ')
altura = float(input('Digite a altura: '))

peso_ideal = (72.7*altura) - 58

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    genero = "masculino"

elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
    genero = "feminino"

else:
    print('Sexo inválido. Digite M para masculino ou F para feminino.')
    exit()

print(f'Seu peso ideal para o sexo {genero} é de {peso_ideal}kg.')