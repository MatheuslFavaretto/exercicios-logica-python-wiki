#Faça um Programa que peça as 4 notas bimestrais e mostre a média. 

primeiro_bimestre = float(input('digite a nota do bimestre: '))
segundo_bimestre = float(input('digite a nota do bimestre: '))
terceiro_bimestre = float(input('digite a nota do bimestre: '))
quarto_bimestre = float(input('digite a nota do bimestre: '))

media = (primeiro_bimestre + segundo_bimestre + terceiro_bimestre + quarto_bimestre) / 4

print(f'A media dos bimestre é {media}.')