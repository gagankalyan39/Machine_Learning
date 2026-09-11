import numpy as np

list1 = [1, 2, 3, 4]
list2 =[[1,2,3,4]]
list3 = [[1,2,3,4],
        [10,20,30,40],
        [100,200,300,400]]

arr1= np.array(list1)
arr2= np.array(list2)
arr3= np.array(list3)
print(type(arr1),type(arr2),type(arr3))


print(arr1.shape)  # Prints dimensions: 
print(arr2.shape)  # Prints dimensions: 
print(arr3.shape)  # Prints dimensions: 



print(arr1.dtype)  # Prints data type: int64 (or int32)
print(arr2.dtype)  # Prints data type: int64 (or int32)
print(arr3.dtype)  # Prints data type: int64 (or int32)


print(arr1.ndim)   # Prints number of dimensions: 2
print(arr2.ndim)   # Prints number of dimensions: 2
print(arr3.ndim)   # Prints number of dimensions: 2

arr4 = np.linspace(0, 10, 5)  # Creates an array of 5 evenly spaced numbers from 0 to 10
print(arr4)

print(arr4*5)