#faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 


sexo = input('digite M para homem e F para mulher: ')

if sexo == "M":
    genero = 'Masculino'

elif sexo == "F":
    genero = 'Feminino'

else:
    print('Sexo inválido. Digite M para masculino ou F para feminino(atenção a letra maiuscula).')
    exit()

print(f'A letra digitada confere ao genero {genero}.')