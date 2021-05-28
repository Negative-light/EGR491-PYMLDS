# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Function to check for a file
# returns TRUE if there is a file, else returns false
def check4File(filePath):
    import os.path
    return os.path.isfile(filePath)
    


# %%
# reads a file and loads it into a list, all new lines are treated as the default separator
def readFile(path):
    f = open(path, "r")
    output = ""
    for l in f:
        output += ','
        output += str(l.strip())
    output = output[1:]
    return output


# %%
# Function that reads the users input and elminates all non recoverable values
def loadLst(strLst):
    lst = []
    for i in str(strLst).split(','):
        try:
            lst.append(int(i))
        except:
            print("INVALID VALUE: ", i)
    
    return lst
    
    


# %%
# Opening Title
print("EGR491 Project 1: Paul A. Pace")
print("This project is designed to display various simple attributes of python.")
userData = input("Please input either a comma separated list OR a file path.")


# %%
# Check for if userData is a file else read the list
if check4File(userData):
    print("Reading From your file")
    userData = readFile(userData)
else:
    print("Reading List now!!!")


# Print out userData
print(userData)

# %%
# Make your list from the userData and check for its sum
myList = loadLst(userData)

m = 0
for i in myList:
    m += i
print("The Sum of your list is ", m)
# %%

# Make a unorderd list out of myList
myList2 = {i for i in myList}
print("Your list without duplicates is ", myList2)

# %%
# Make a list with only the even inputs
myList3 = [i for i in myList if i % 2 == 0]

# PRint myList3
print(myList3)