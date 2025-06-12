# Calcular o IMC

nome = "Leon Santana"
altura = 1.80
peso = 86
imc = peso / (altura ** 2) 

# f-strings
linha_1 = (f'{nome} tem {altura:.2f} de altura,')
linha_2 = (f'pesa {peso} quilos e seu imc é {imc:.2f}')

# print(nome, "tem", altura, "de altura,",)
# print('pesa', peso, 'quilos e seu imc é', imc)
print(linha_1)
print(linha_2)