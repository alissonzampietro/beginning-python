#FUNCTIONS

## To create a function you should use the term 'def'
def hello():
    print('hello world')

# Here you can pass a list as arguments
def total(*params):
    print('calc total: '+str(sum(*params)))

# You can pass undefined amount of params for the functions
def any(*args):
    print('Showing only first parameter: '+str(args[0]))

def total(*params):
    # here it shows individual items
    print(*params)
    # here it shows a tuple 
    print(params)

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
total(1,2,3,4)
    