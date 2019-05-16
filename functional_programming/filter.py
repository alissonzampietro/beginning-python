items = [1,2,3,4,5,6,7,8,9,20]
myList = list(filter(lambda x: x % 2 == 0, items))
print(myList)