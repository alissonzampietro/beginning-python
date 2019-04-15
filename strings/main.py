## Strings
name = "Marcosa"
print('Show declared string: '+name)
print('Range 1:5 showing string: '+name[1:5])
print('Range :3 showing string: '+name[:3])
print('Range 3: showing string: '+name[3:])

# conta a quantidade de caracteres que uma string possui
print('Show the size if the string using a method __len__():  '+str(name.__len__()))
print('Show the size if the string using a method len():  '+str(len(name)))

#escaping
print(r'C:\nome\nada')

## Values assignement
idade = 24
tempo_moraria = 6
nome = 'Alisson'
print('%s tem %d anos e mora em portugal a %d meses' % (nome, idade, tempo_moraria))