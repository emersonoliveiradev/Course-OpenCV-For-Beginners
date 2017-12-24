import numpy as np

array_unidimensional = np.array([5, 10, 15])

#Return the type of element
print(array_unidimensional.dtype)

#Return de "shape" of element - Structure
print(array_unidimensional.shape)

#Acess element in array
for i in range(0, 3, 1):
    print(array_unidimensional[i])

#Change the value of a element in array
array_unidimensional[1] = 888
print(array_unidimensional[1])

#Define array multidimensional
array_multidimensional= np.array([[1,2], [3,4], [5,6]])

print(array_multidimensional)

#Return the number of lines and columns
print(array_multidimensional.shape)

