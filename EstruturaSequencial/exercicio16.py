#faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 

import math 


area = float(input('Digite o tamanho em metros quadrados da área a ser pintada: '))

litros_tinta = area / 3.0 
latas_tinta = math.ceil(litros_tinta / 18.0) 
preco_total = latas_tinta * 80.0 

print(f'Quantidade de latas de tinta a serem compradas: {latas_tinta}')
print(f'Preço total: R$ {preco_total:.2f}')