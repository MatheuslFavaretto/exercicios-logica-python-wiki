#Faça um Programa que leia três números e mostre-os em ordem decrescente. 

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
meio = (num1 + num2 + num3) - maior - menor

print(maior, meio, menor)
