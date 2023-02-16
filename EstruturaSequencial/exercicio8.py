#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. 

valor_hora = float(input('Digite o valor hora trabalhada: '))
horas = float(input('Digite as horas trabalhadas no mês: '))

resuldado = (valor_hora * horas)

print(f'O valor a ser recebido é {resuldado}')