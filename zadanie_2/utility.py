# A storage for functions usefull for many projects
import random


# Opens a .csv file, reads lines from it and saves it into an array as float values
# @path - relative file path to the data
# returns - two dimensional array of float values
def fileLoader(path:str):
    
    file = open(path, 'r', newline='\n')    
    dataTable = [];

    i = 0;
    for x in file:
        dataTable.append(x.split(','))
        for j in range(5):
            dataTable[i][j] = float(dataTable[i][j])
        i += 1
    
    file.close()
    
    return dataTable




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


def encodeAsHex(d10:int) ->str:
    
    return

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