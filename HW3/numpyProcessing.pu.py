# Write a Python/NumPy code block that finds the distinct/unique common items between these two
# arrays:
# a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
# b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
# Your output should contain only the distinct overlapping values. For example, if a 2 is found in both array a and array b,
# your output should contain only one 2 even if array a contains more than one 2 within it.
import numpy as np
import pandas as pd

a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
# https://www.geeksforgeeks.org/find-common-values-between-two-numpy-arrays/#:~:text=In%20NumPy%2C%20we%20can%20find,the%20common%20elements%20will%20appear.
c=np.intersect1d(a,b)
print(c,'\n')
print("-----------------------------------------------  \n")


# Problem 2:
# Create the following 5x3 array using knowledge you have of Python’s / NumPy’s sequencing functionality
# so that you do not need to explicitly key in every integer value.
# matrix=np.random.randint(1, 16,(5,3))
matrix=np.array([[1,6,11],[2,7,11],[3,8,13],[4,9,14],[5,10,15]])
print(matrix,'\n')
print("-----------------------------------------------  \n")




#3
# The process of transforming a multidimensional array into a unidimensional array is referred to as “flattening”. 
# Transform the 5x3 array shown above in Problem 2 into a unidimensional array such that the sequence of values
#  contained within the array 
# is as follows: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15

flatten_array=matrix.flatten()
print(flatten_array,'\n')
print("-----------------------------------------------  \n")



#4
# Transform the 2-D array shown in Problem 2 into a 3 dimensional array such that the first column
#  becomes the first dimension of the 3-D array, the second column becomes the second dimension of the 
#  3-D array, and the third column becomes the third dimension of the 3-D array.
# print(matrix.shape[0:1])
matrix2=matrix.reshape(3,5,1)
print("This is current dimension of the selected matrix" + np.ndim)
print(matrix2)
print("---------------------------------------------- \n")



# Problem 5:
# Transform the 3-D array you created in Problem 4 back to the 2-dimensional format shown
#  in Problem 2.
matrix2=matrix.reshape(3,5)
print("This is current dimension of the selected matrix" + np.ndim)
print(matrix2)
print("-----------------------------------------------  \n")

# 6:
ax = np.array([12, 5, 7, 15, 3, 1, 8])
bx = np.array([14, 6, 3, 11, 19, 12, 5])
for i in ax:
    if i in bx:
        print(i)
        ax=np.delete(ax,np.where(ax==i)[0][0])
print(ax)
print("-----------------------------------------------  \n")



# 7

dataFrame=pd.read_csv('Module6_Data.csv')
data=dataFrame.to_numpy()
maximum_value=np.max(data[:,2])
yearsRepresentation=np.shape(data)
standard_deviation=np.abs(np.std(data[:,3]))
changeInPopulation=np.diff(data[:,1])
print(" Negative Value means , decrease of population with the corresponding next year:  \n"+ str(changeInPopulation))
mean=np.std(data[:,3])
print("Number of years being represented in the dataset:  "+ str(yearsRepresentation))
print("Maximum Value: " + str(maximum_value))
print("Mean: "+ str(mean))
print("Standard Deviation: "+ str(standard_deviation))




