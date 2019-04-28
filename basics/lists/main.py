myList = [1,2,3,4,'test',['joao','maria']]

# 'len' get the size of the lists
print(len(myList))

#iterating list using for
for x in myList:
    print(x, end='-')

# show last item from list
print('\n------------------------------')
print(myList[-1])

print('\n------------------------------')
print(myList[3:len(myList)])

print('\n------------------------------')
myList2 = myList
myList2[-1] = 'changed vaue'
#It happens because a list is an object, and when you assign a existing variable to a new, they gonna have the same reference
print(myList)

# To change the behavior above, you should do this 
myList3 = myList[:]
myList3[-1] = 'myList3'
print(myList)
print(myList3)

print('\n------------------------------')

#cocat lists
myList4 = myList2 + myList3
print(myList4)

print('\n------------------------------')

#remove item from list

## @Remove by position
### Show removed element
print(myList.pop(1))
###Show updated list
print(myList)

## @Remove by value
myList.remove(1)
print(myList)


print('\n------------------------------')

