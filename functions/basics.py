# Functions

try:
    ## my fist function, it was really easy
    def dispatcher(functionName):
        allFunctions = {
            'sum':sum,
            'multiply': multiply
        }
        return allFunctions[functionName]

    def sum(a,b):
        return a + b

    def multiply(a,b):
        return a * b

    def begin():
        func = dispatcher(input('type the operation name: '))
        a = input('first param: ')
        b = input('second param: ')
        print(func(int(a),int(b)))
        begin()

    begin()
except:
    print('This operation is not implemented yet')
    begin()

