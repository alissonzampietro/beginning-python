import numpy as np

arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10]

## NumPy
a = np.array([arr1, arr2])

### get average
print('average: '+str(a.mean()))

### get diagonal
print('diagonal: '+str(a.diagonal()))

### get dimension
print('dimension: '+str(a.ndim))

## Python list

listSample = [1,2,3,4,'Alisson']

### appending item
listSample.append('one more')
print('appended item: '+str(listSample))