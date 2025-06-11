nome = 'Leon'
sobrenome = 'Santana'
idade = 27
ano_nascimento = 1998
maior_de_idade = idade >= 18
altura_metros = 1.80


print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)

print(f'Meu nome é {nome} {sobrenome}, tenho {idade} anos, nasci em {ano_nascimento}, tenho {altura_metros} metros e { "sou maior de idade" if maior_de_idade else "sou menor de idade" }.')