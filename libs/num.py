import numpy

# Matrix
a = numpy.array([10,20,30,40])
print(a)
print(type(a))

# two-dimensional matrix
## The bth arrays should have the same amount of values
twoMatrix = numpy.array([[2,4,6,8,10,12],[1,3,5,7,9,11]])
print(twoMatrix)

## accessing values
print(twoMatrix[1][0])

## [ 2  4  6  8 10 12]
print(twoMatrix[0,:])

## [ 1  3  5  7  9 11]
print(twoMatrix[1,:])


## get size on total (12)
print('total of itens: '+str(numpy.size(twoMatrix)))

## [4 3]
print(twoMatrix[:,1])