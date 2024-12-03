# A storage for functions usefull for many projects
import random





# Appends a blank column (comprised of Nones) at the end of a 2 dimensional list.
# Where i-rows, j-columns
# @toBeAppended - list to be changed
def appendColumnToList(toBeAppended:list):
    for i in range(len(toBeAppended)):
        toBeAppended[i].append(None)

# Choses random indexes from a list of points.
# Loses efficiency when howMany nears length of the list.
# @points - list of points
# @howMany - how many indexes do you want to pick (must be between 1 and len(points) )
# returns - one dimensional list of all the picked indexes
def selectRandomIndexes(points:list, howMany:int) -> list: 
    picked = list()
    
    length = len(points)
    if (howMany > length):
        raise ValueError("Cant pick more points than there are in a list")
    if (howMany <= 0):
        raise ValueError("Can't pick 0 or less points")
    
    alreadyChosen = set()
    
    
    successfull = 0
    while (successfull < howMany):
        new = random.randint(0, length-1)
        if not (new in alreadyChosen):
            alreadyChosen.add(new)
            picked.append(new)
            successfull += 1
        
    return picked
    

# Opens a .csv file, reads lines from it and saves it into an array as float values
# @path - relative file path to the data
# returns - two dimensional array of float values
def fileLoader(path:str):
    
    file = open(path, 'r', newline='\n')    
    dataTable = [];

    i = 0;
    for x in file:
        dataTable.append(x.split(','))
        for j in range(4):
            dataTable[i][j] = float(dataTable[i][j])
        i += 1
    
    file.close()
    
    return dataTable

# Rounds every element of a list
# @lista - one dimensional list of floats
# @dokladnosc - e.g. 0.01 for 2
# returns - list with rounded elements
def roundList(lista:list, dokladnosc:int):
    return [round(x, dokladnosc) for x in lista]




# Splits a list in half, ignores the middle index if list is not even.
# @entryList - 1 dim list
# returns - a tuple of 2 lists IMPORTANT: shallow copies
def splitList(entryList):
    length = len(entryList)
    

    middle = int(length/2)
    list1 = entryList[0:middle]

    if length % 2 == 1:
        list2 = entryList[middle+1:]
    else:
        list2 = entryList[middle:]
    
    
    return (list1, list2)



# Returns a list of N colors, to be used for a pallete
def createPalleteOfColors(N:int) ->str:
    output = str()
    red = list(); green = list(); blue = list()
    
    prev_choice = 0;
    #pick R
    for i in range (N):
        prev_choice = random.randint(0+prev_choice, (int(255/N)*(i+1)))
        red.append(prev_choice)
    #pick G
    print(red)
    
    #pick B

# 10 element list of RGB colors. WARNING, potentially similar colors
# also not super usefull
colorPallete = ["#E1C588", "#7B2452", "#627098", "#DD858A", "#76B86F", "#1E4D5F", "#993900", "#4B0365", "#8E9700", "#00FFF5"]