# Functions

try:
    onlyOneParameter = {'mod'}
    ## my fist function, it was really easy
    def dispatcher(functionName):
        allFunctions = {
            'sum':sum,
            'multiply': multiply,
            'divide': divide,
            'difference': difference,
            'mod': mod,
        }

        a = input('first param: ')
        if(functionName not in onlyOneParameter):
            b = input('second param: ')
        else:
            b = 0
        print(allFunctions[functionName](int(a),int(b)))
        begin()

    def sum(a,b):
        return a + b
    
    def difference(a,b):
        return a - b

    def multiply(a,b):
        return a * b
    
    def divide(a,b):
        return a / b
    
    def mod(a, b):
        return a % 2

    def begin():
        funcName = input('type the operation name: ')
        dispatcher(funcName)

    begin()
except:
    print('This operation is not implemented yet')
    begin()

