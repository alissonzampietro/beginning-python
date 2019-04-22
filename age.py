from datetime import datetime

n = datetime.now()
t = n.timetuple()
y,m,d,h,m,s,wd,yd, isdst = t

try:

    age = int(input('Type yor age: '))
    name = input('Type your name: ')
    minus = y - age
    year_born = str(minus)

    if 1950 <= minus < 1970:
        print('You\'re old '+name+'!')
    elif 1970 <= minus < 1990:
        print('You\'re not too old '+name+'!')
    elif 1990 <= minus < 2010:
        print('Soon you gonna getting old my dear '+name+'!')
    elif 2010 <= minus < 2030:
        print('Too young! Enjoy your life '+name+'!')

    print('Mr(s) '+name+' your birth year is: '+year_born)


except:
    print('Invalid input')