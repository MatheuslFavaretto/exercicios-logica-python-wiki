#faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#   a. o produto do dobro do primeiro com metade do segundo .
#   b. a soma do triplo do primeiro com o terceiro.
#   c. o terceiro elevado ao cubo. 

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = float(input("Digite o número real: "))

respota_a = (2 * num1) + (num2 / 2)
print(f'O produto do dobro do primeiro com metade do segundo é: {respota_a}')

respota_b = (3 * num1) + num3
print(f'A soma do triplo do primeiro com o terceiro é: {respota_b}')

respota_c = num3 ** 3
print(f'O terceiro elevado ao cubo é: {respota_c}')