myList = [1,2,3,4,'test',['joao','maria']]
int = 'alisson'

# Damn it, i don't know yet how this kind of thing can happens
print(int)

# 'len' get the size of the lists
print(len(myList))

print('\n')

# iterating list
for item in myList:
    print(isinstance(item, list), end='')