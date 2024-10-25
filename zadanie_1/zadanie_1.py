# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:59:25 2024

@author: Jan Pawloski
@author: Emil Franczak
"""


import matplotlib.pyplot as plt


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
    
# Checks the species of a flower, then increses the counter in dictionary.
# @data parameter - float [x][5]
# returns speciesCount - dictoriary with species names as keys and species count
def countThreeSpecies(data):
    
    speciesNames = {
        0 : "setosa",
        1 : "versicolor",
        2 : "virginica"
        }
    
    speciesCount = {
        "setosa" : 0,
        "versicolor" : 0,
        "virginica" : 0
        }
    
    
    for i in range(len(data)):
        spName = speciesNames[data[i][4]]
        speciesCount[spName] = speciesCount[spName] + 1
            
    return speciesCount    


# Finds ammount of flowers in dataset, each row is a single flower.
# @data parameter - float [x][y]
# returns int flower ammount
def totalPopulation(data):
    return len(data)


# Compares species count against the total.
# @speciesCount paremeter - dictionary contains counters of each species
# returns float share of total population
def speciesShareOfPopulation(speciesCount:dict):
    
    totalPop = 0
    for x in speciesCount:
        totalPop += speciesCount[x]
        
    speciesShare = {
        "setosa" : speciesCount["setosa"]/totalPop,
        "versicolor" : speciesCount["versicolor"]/totalPop,
        "virginica" : speciesCount["virginica"]/totalPop
        }
    
    
    return speciesShare


# Tracks the highest values for each of the 4 traits
# @data parameter - float [x][y]
# returns dictionary of maximum traits
def getMaximumTraits(data):
    
    traitIndexes = {
        0 : "sepal_length",
        1 : "sepal_width",
        2 : "petal_length",
        3 : "petal_width"        
        }
    
    
    maximumTraits = {
        "sepal_length" : 0,
        "sepal_width" : 0,
        "petal_length" : 0,
        "petal_width" : 0
        }
    
    for i in range(len(data)):
        for j in range(4):
            if maximumTraits[traitIndexes[j]] < data[i][j]:
                maximumTraits[traitIndexes[j]] = data[i][j]    

    return maximumTraits

# Tracks the lowest values for each of the 4 traits
# @data parameter - float [x][y]
# returns dictionary of minimum traits
def getMinimumTraits(data):
    traitIndexes = {
        0 : "sepal_length",
        1 : "sepal_width",
        2 : "petal_length",
        3 : "petal_width"        
        }
    
    minimumTraits = {
        "sepal_length" : 999, #swap for first row's values? 
        "sepal_width" : 999,
        "petal_length" : 999,
        "petal_width" : 999,
        }
    
    for i in range(len(data)):
        for j in range(4):
            if minimumTraits[traitIndexes[j]] > data[i][j]:
                minimumTraits[traitIndexes[j]] = data[i][j]
                
    return minimumTraits

# Sums all values of traits, then divides them by total sample size.
# @data parameter - float [x][y]
# returns dictionary of average traits
def getAverageTraits(data):
    traitIndexes = {
        0 : "sepal_length",
        1 : "sepal_width",
        2 : "petal_length",
        3 : "petal_width"        
        }
    
    traitSums = {
        "sepal_length" : 0, 
        "sepal_width" : 0,
        "petal_length" : 0,
        "petal_width" : 0,
        }
    
    
    totPop = totalPopulation(data)
    for i in range(len(data)):
        for j in range(4):
            traitSums[traitIndexes[j]] += data[i][j]
    
    for i in range(4):
        traitSums[traitIndexes[i]] = traitSums[traitIndexes[i]] / totPop
        
    return traitSums

def getMedianTraits(data):
    traitIndexes = {
        0 : "sepal_length",
        1 : "sepal_width",
        2 : "petal_length",
        3 : "petal_width"        
        }
    
    
    traitMedians = {
        "sepal_length" : 0, 
        "sepal_width" : 0,
        "petal_length" : 0,
        "petal_width" : 0,
        }
    
    
    # Creates four lists of traits, resembling how they're written in .csv file
    fourListsOfTraits = []
    for i in range(4):
        fourListsOfTraits.append([])
        for j in range(totalPopulation(data)):
            fourListsOfTraits[i].append(data[j][i])
        # finds the median
        traitMedians[traitIndexes[i]] = findMedianOfList(fourListsOfTraits[i])
        
    
    return traitMedians

 

# Finds the median of a 1 dimensional list
# @entryList parameter - unsorted list
# returns median value
def findMedianOfList(entryList:list):
    entryList.sort()
    length = len(entryList);
    if length % 2 == 1:
        return entryList[int(length/2)] #no +1, because indexes start from 0
    else:
        avrg = ((entryList[int(length/2)] + entryList[int(length/2)-1]) /2)
        return avrg



# Finds the quartiles of a 1 dimensional list
# @entryList parameter - unsorted list
# returns quartiles - list of [Q1, Q2, Q3]
def findQuartilesOfList(entryList:list):
    # entryList.sort()
    length = len(entryList);
    quartiles = [] # Q1, Q2, Q3
    
    median = findMedianOfList(entryList)
    firstHalf, secondHalf = splitList(entryList)
    Q1 = findMedianOfList(firstHalf)
    Q3 = findMedianOfList(secondHalf)
    
    return [Q1, median, Q3]

def splitList(entryList):
    length = len(entryList)
    
    if length % 2 == 1:
        entryList.pop(int(length/2))
        length -= 1
    
    
    middle = int(length/2)
    
    list1 = entryList[0:middle]
    list2 = entryList[middle:]
    
    return list1, list2

def getQuartilesTraits(data):
    traitIndexes = {
        0 : "sepal_length",
        1 : "sepal_width",
        2 : "petal_length",
        3 : "petal_width"        
        }
    
    
    traitQuartiles = {
        "sepal_length" : [0, 0, 0], 
        "sepal_width" : [0, 0, 0],
        "petal_length" : [0, 0, 0],
        "petal_width" : [0, 0, 0],
        }
    
    
    # Creates four lists of traits, resembling how they're written in .csv file
    fourListsOfTraits = []
    for i in range(4):
        fourListsOfTraits.append([])
        for j in range(totalPopulation(data)):
            fourListsOfTraits[i].append(data[j][i])
        # finds the median
        traitQuartiles[traitIndexes[i]] = findQuartilesOfList(fourListsOfTraits[i])
    return traitQuartiles

def testFindQuartilesOfList():
    entryList1 = [0, 2, 3, 4, 5, 5, 6, 7]
    entryList2 = [0, 2, 3, 4, 5, 5, 6]
    print( "Test Find Quartiles Of List")
    
    outputList1 = findQuartilesOfList(entryList1)
    print( (outputList1[0] == 2.5) == True)
    print( (outputList1[1] == 4.5) == True)
    print( (outputList1[2] == 5.5) == True)
    outputList2 = findQuartilesOfList(entryList2)
    print( (outputList2[0] == 2) == True)
    print( (outputList2[1] == 4) == True)
    print( (outputList2[2] == 5) == True)
    print()
    
def testGetQuartilesTraits():
    print("Test Get Quartiles Traits")
    
    data = fileLoader("test_data1.csv")
    quartilesTraits = getQuartilesTraits(data)
    
    print( (quartilesTraits["sepal_length"][0] == 4.6) == True)
    print( (quartilesTraits["sepal_length"][1] == 4.9) == True)
    print( (quartilesTraits["sepal_length"][2] == 5.0) == True)
    print( (quartilesTraits["petal_width"][0] == 0.2) == True)
    print( (quartilesTraits["petal_width"][1] == 0.2) == True)
    print( (quartilesTraits["petal_width"][2] == 0.2) == True)
    print()        
    
def testGetMedianTraits():
    print("Test Get Median Traits")

    data = fileLoader("test_data1.csv")
    medianTraits = getMedianTraits(data)
    print( (round(medianTraits["sepal_length"], 5) == 4.9) == True)
    print( (round(medianTraits["sepal_width"], 5) == 3.3) == True)
    print( (round(medianTraits["petal_length"], 5) == 1.4) == True)
    print( (round(medianTraits["petal_width"], 5) == 0.2) == True)
    print()    
    


def testGetAverageTraits():
    print("Test Get Average Traits")
    
    data = fileLoader("test_data1.csv")
    averageTraits = getAverageTraits(data)
    print( (round(averageTraits["sepal_length"], 5) == 4.86) == True)
    print( (round(averageTraits["sepal_width"], 5) == 3.31) == True)
    print( (round(averageTraits["petal_length"], 5) == 1.45) == True)
    print( (round(averageTraits["petal_width"], 5) == 0.22) == True)
    print()    
    
def testGetMinimumTraits():
    print("Test Get Minimum Traits")
    
    data = fileLoader("test_data1.csv")
    minimumTraits = getMinimumTraits(data)
    print( (minimumTraits["sepal_length"] == 5.4) == False)
    print( (minimumTraits["sepal_width"] == 3.9) == False)
    print( (minimumTraits["petal_length"] == 1.7) == False)
    print( (minimumTraits["petal_width"] == 0.4) == False)
    print()
    
def testGetMaximumTraits():
    print("Test Get Maximum Traits")
    data = fileLoader("test_data1.csv");
    maximumTraits = getMaximumTraits(data)
    print( (maximumTraits["sepal_length"] == 5.4) == True)
    print( (maximumTraits["sepal_width"] == 3.9) == True)
    print( (maximumTraits["petal_length"] == 1.7) == True)
    print( (maximumTraits["petal_width"] == 0.4) == True)
    print()

def testSpeciesShareOfPopulation():
    print("Test Species Share Of Population")
    data = fileLoader("data1.csv");
    
    speciesCount = countThreeSpecies(data)    
    
    speciesShare = speciesShareOfPopulation(speciesCount)
    
    
    #rounding just for testing
    print( (round(speciesShare["setosa"], 5) == round(1/3, 5)) == True)
    print( (round(speciesShare["versicolor"], 5) == round(1/3, 5)) == True)
    print( (round(speciesShare["virginica"], 5) == round(1/3, 5)) == True)
    print()    
    
def testCountThreeSpecies():
    print("Test Count Three Species")
    data = fileLoader("data1.csv");
    
    speciesCount = countThreeSpecies(data)
    
    print( (len(speciesCount) == 3) == True)
    print( (speciesCount["setosa"] == 50) == True)
    print( (speciesCount["versicolor"] == 50) == True)
    print()
    
    
def testFileLoader():
    print("Test File Loader")
    data = fileLoader("data1.csv");
    print((len(data[0]) == 5) == True)
    print(isinstance(data[0][0], float) == True)
    print((len(data) == 150) == True)
    print()
    

testFileLoader()
testCountThreeSpecies()
testSpeciesShareOfPopulation()
testGetMaximumTraits()
testGetMinimumTraits()
testGetAverageTraits()
testGetMedianTraits()
testFindQuartilesOfList()
testGetQuartilesTraits()