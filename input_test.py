from datetime import datetime

n = datetime.now()
t = n.timetuple()
y,m,d,h,m,s,wd,yd, isdst = t

try:

    idade = int(input('Digite a sua idade: '))
    nome = input('Digite o seu nome: ')
    year_born = str(y - idade)
    print('Sr(a) '+nome+' o ano de seu nascimento é: '+year_born)

except:
    print('Input inválidox')