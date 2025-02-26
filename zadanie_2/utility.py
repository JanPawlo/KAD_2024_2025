import random



def dotToComma(writing:str):
    new_writing = str()
    for i in range(len(writing)):
        if (writing[i] == "."):
            new_writing = new_writing + ","
        else:
            new_writing = new_writing + writing[i]
    return str(new_writing)

def appendColumnToList(toBeAppended:list):
    for i in range(len(toBeAppended)):
        toBeAppended[i].append(None)


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


def roundList(lista:list, dokladnosc:int):
    return [round(x, dokladnosc) for x in lista]




def splitList(entryList):
    length = len(entryList)
    

    middle = int(length/2)
    list1 = entryList[0:middle]

    if length % 2 == 1:
        list2 = entryList[middle+1:]
    else:
        list2 = entryList[middle:]
    
    
    return (list1, list2)


def getMaximumTraits(data):
    
    maximumTraits = {
        0 : 0,
        1 : 0,
        2 : 0,
        3 : 0
        }
    
    for i in range(len(data)):
        for j in range(4):
            if maximumTraits[j] < data[i][j]:
                maximumTraits[j] = data[i][j]    

    return maximumTraits


def getMinimumTraits(data):
    
    minimumTraits = {
        0 : 999, 
        1 : 999,
        2 : 999,
        3 : 999,
        }
    
    for i in range(len(data)):
        for j in range(4):
            if minimumTraits[j] > data[i][j]:
                minimumTraits[j] = data[i][j]
                
    return minimumTraits


