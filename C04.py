coisa = input('Digite algo: ')
print(f'Seu tipo primitivo é: {type(coisa)}')
print(f'Só tem espaços: {coisa.isspace()}')
print(f'É um número: {coisa.isnumeric()}')
print(f'É alfabeto: {coisa.isalpha()}')
print(f'É alfanumérico: {coisa.isalnum()}')
print(f'Está em maiúscula: {coisa.isupper()}')
print(f'Está em minúscula: {coisa.islower()}')
print(f'Está capitalizada: {coisa.istitle()}')
