import datetime
now = datetime.datetime.now()

# Recursive function
def factorial(number):
    if number == 0 or number == 1:
        return 1
    
    return number * factorial(number-1)

def calcAge(age=0):
    return now.year - age

# You can pass function as parameter
def buildProfile(name, age, calcAge=calcAge):
    print('Hello '+name+', i calculated that you waws born in '+str(calcAge(age)))

print(factorial(5))
print(buildProfile('Alisson', 24))
