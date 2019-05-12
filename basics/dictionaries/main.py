#Dictionaries
## It has the same structure than list, but it values are changeable and flexible, it means that you can add
## any value in the moment that you to wish

age = {'alisson':24, 'rui':32, 'mateus': 29}

print('Here you can see Alisson\'s age: '+str(age['alisson']))

age['luis'] = 34
print('Now yo can see that Luis has been added: '+ str(age))

for item in age:
    print(item+' is '+str(age[item])+' years old')

# show each item
print(age.items())
# show all keys
print(age.keys())
# show all values
print(age.values())

print(32 in age.values())
print('alisson' in age)