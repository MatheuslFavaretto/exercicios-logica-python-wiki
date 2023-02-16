#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#    comprar apenas latas de 18 litros;
#    comprar apenas galões de 3,6 litros;
#    misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. 

import math

area = float(input('Informe o tamanho da área a ser pintada em metros quadrados: '))

litros_tinta = area / 6.0 * 1.1

latas_tinta = math.ceil(litros_tinta / 18.0)
preco_latas = latas_tinta * 80.0
print(f'Solução 1: Comprar {latas_tinta} latas de tinta de 18 litros. Preço total: R$ {preco_latas:.2f}')

galoes_tinta = math.ceil(litros_tinta / 3.6)
preco_galoes = galoes_tinta * 25.0
print(f'Solução 2: Comprar {galoes_tinta} galões de tinta de 3,6 litros. Preço total: R$ {preco_galoes:.2f}')

latas_tinta = int(litros_tinta // 18.0) 
resto_litros = litros_tinta % 18.0 
galoes_tinta = math.ceil(resto_litros / 3.6) 
preco_mix = latas_tinta * 80.0 + galoes_tinta * 25.0 
print(f'Solução 3: Comprar {latas_tinta} latas de tinta de 18 litros e {galoes_tinta} galões de tinta de 3,6 litros. Preço total: R$ {preco_mix:.2f}')
