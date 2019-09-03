nome = str(input('Qual seu nome? '))
if nome == 'Anderson':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Ana' or nome == 'Maria':
    print('Nome popular!')
else:
    print('Entrou no else!')
print('Tenha um bom dia, {}!'.format(nome))
