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

## matrix transpose
print('tranposed matrix: '+str(numpy.transpose(twoMatrix)))


## get size on total (12)
print('total of itens: '+str(numpy.size(twoMatrix)))

## [4 3]
print(twoMatrix[:,1])

## matrix operations
array1 = numpy.array([2,6])
array2 = numpy.array([7,8])
print('sum items in the unique array: '+str(array1.sum()))
### remember: in this case below, where we have operations converted in string, python gonna always execute the operations first and after convert the result to string
print('array sum: '+str(array1 + array2))
print('array multiply: '+str(array1 * array2))
print('array subtract: '+str(array1 - array2))

### show biggest value array numpy
print('biggest value: '+str(array1.max()))

### show biggest value array numpy
print('smaller value: '+str(array1.min()))

### show position biggest value array numpy
print('position biggest value: '+str(array1.argmax()))

### show position of the smaller value array numpy
print('position smaller value: '+str(array1.argmin()))