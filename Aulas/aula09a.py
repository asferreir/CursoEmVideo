frase = 'Curso em Video Python'
# Exibir a string que esta na posição 9
print(frase[9])
# Exibir as string iniciando no 9 indo ate a
# string anterior a 21, contando de 2 em 2
print(frase[9:21:2])
# Exibir as string do inicio ate a 5
print(frase[:5])
# Exibir as string do iniciando na string 15
# e indo ate o final
print(frase[15:])
# Exibir as string começado na string 9 e indo ate o final,
# Contanto de 3 em 3 itens
print(frase[9::3])
# Exibir o comprimento de frase
print(len(frase))
# Exibir a quantidadede 'o' no conjunto de String
print(frase.count('o'))
# Exibir a quantidadede 'o', entre as strings 0 e 13
print(frase.count('o', 0, 13))
# Exibir o local de inicio da string 'deo'
print(frase.find('deo'))
# Vai exibir o valor -1, pois nao encontrou a String
print(frase.find('Android'))
# Verifica se tem 'Curso' em frase
# 'Curso' in frase
frase.replace('Python', 'Android')
frase.upper()
frase.lower()
frase.capitalize()
frase.title()
frase.strip()
frase.rstrip()
frase.lstrip()
print(frase.split())
'-'.join(frase)
