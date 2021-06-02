# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Project Goal
# 
# Show multiple methods and function on an set of arrays including data analysis.

# %%
import numpy as np


# %%
def welcome():
    print("This Project was produced by: Paul A. Pace")
    print("FOR: EGR491 Project 2 Summer 21 Mercer University")


# %%
def promt4array():
    num1 = input("How many rows for your array")
    num2 = input("How many columns for your array")
    return (int(num1),int(num2))


# %%
welcome()
arr1 = np.ones(promt4array())


# %%
print("This is your array: ")
print(arr1)
print("applying random value")
arr1 += np.random.randint(0,100, arr1.shape)


# %%
print("Evaluating your array")
print(arr1)
print("These values are over 50")
mskArr = arr1 > 50
print(mskArr)

print("The average value above 50 is ", arr1[mskArr].mean())

print("It looks a little sloppy lets fix that: ")
arr1 = np.sort(arr1, axis=1)

print("The sum of each column is: ")
print(arr1.sum(axis=0))
print("The Average Column Size is: ", end=' ')
print(arr1.sum(axis=1).mean())



# %%
print("Lets do some more: ")
print(arr1.max(), ":MAX")
print(arr1.min(), ":MIN")


# %%
print("-------------------")
print("now let us do some boardcasting")
x = arr1.shape[1]
print(x)
arrTmp = np.array(np.arange(x))
print(arrTmp.shape)
arr2 = arrTmp - arr1
print(arr2)
print(arr1 - arr2) # This will print your column numbers


# %%
print("Some Advaced Indexing")
# We must get the smallest of either rows of columns
x = arr1.shape[0]
if x < arr1.shape[1]:
     x = arr1.shape[1]

arr3 = np.random.randint(0, arr1.shape[0]-1, x) #Generate your Rows
arr4 = np.random.randint(0, arr1.shape[1]-1, x) # Generate your columns
arr3 += np.zeros(arr4.shape, dtype='int32') # You must set the type to int32 and have the same number of values
arr4 += np.zeros(arr3.shape, dtype='int32')
print(arr3, "\n", arr4)
print("The values at these locations are: ")
print(arr1[arr3,arr4])


# %%
print("And just for kicks lets make a graph:")
print("We will print arr3 vs arr4")
import matplotlib.pyplot as plt
plt.scatter(arr3, arr4)
plt.title("These are the values we picked")
plt.show()

# %%



