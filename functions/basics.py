#FUNCTIONS

## To create a function you should use the term 'def'
def hello():
    print('hello world')

def total(*args):
    print('calc total: '+str(sum(*args)))

# You can pass undefined amount of params for the functions
def any(*args):
    print('Showing only first parameter: '+str(args[0]))

hello()
total([1,2,3,4])
any([1,2,3,4])

# You can assign a method to a variable
imprimir = print
imprimir('Teste em português')

# Default params

def showName(name='Sem nome'):
    print(name)

showName('Alisson Zampietro')
    