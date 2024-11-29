# A storage for functions usefull for many projects



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