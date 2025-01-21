import math
import copy

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
        # last value is a class so it has to be int
        dataTable[i][4] = int(dataTable[i][4])
        i += 1
    
    file.close()
    
    return dataTable

# calculates euclideanDistance between 2 points located in ANY ammount dimensions
# @param p1, p2 - lists [x, y, z, ... ]
# @return float
def euclideanDistance(p1:list, p2:list) -> float:

    # CHECKING VALUES
    if (len(p1) != len(p2)):

        raise Exception("euclideanDistanceNdim: Diffrent nr. of dimensions on points")
    
    dimensions = len(p1)
    
    total = 0
    # SUMATION
    for i in range (dimensions):
        word = p1[i] - p2[i]
        total += word * word
    distance = math.sqrt(total)
    
    return distance


# @param point - classified object
# @param data - 2D list with [x, y, z, ... , classNumber] pattern
def kNearestNeighbours(data:list, k:int, point:list):
    
    
    L = []
    nearestNeighbours = []
    
    # 1. Calculate the Euclidean distance between p and all points in the dataset, storing the results in the list L.    
    for x in data:
        L.append(euclideanDistance(x[:-1], point)) 
    
    # 2. Identify k points in L with the smallest distance from p.
    nearestNeighboursIndexes = findNearestNeighbours(k, L)
    
    # 3. Determine the most common class among the k of nearest neighbours.
    classMembership = determineClassMembership(data, nearestNeighboursIndexes, 3) 
    
    return classMembership;

# @return - indexes of K nearest points
def findNearestNeighbours(k:int, L:list):
    
    if k > len(L):
      raise ValueError("k cannot be greater than the length of the list.")

    L_copy = copy.deepcopy(L)
    nearestNeighboursIndexes = []

    # Find K nearest points
    for i in range(k):
        nearestPointIndex = 0
        # Find the CURRENT nearest point
        for j in range(1, len(L_copy)):
            if L_copy[nearestPointIndex] > L_copy[j]:
                nearestPointIndex = j
        # Save and change the current nearest point to infinity (it won't be considered during another iteration)
        nearestNeighboursIndexes.append(nearestPointIndex)
        L_copy[nearestPointIndex] = float('inf')
    
    return nearestNeighboursIndexes

    #@param data - all the points
    #@param nearestNeighboursIndexes - SORTED list of indexes(within the "data") of the "near" points
    #@param classesNum - number of classes
    #returns -> int number, that signifies class member ship for our point
def determineClassMembership(data:list, nearestNeighboursIndexes:list, classesNum:int):
    if len(data) == 0:
        raise ValueError("List of all data is empty!")
    elif len(nearestNeighboursIndexes) == 0:
        raise ValueError("List of the near neighbours indexes is empty!")
    elif classesNum <=0:
        raise ValueError("Number of classes has to be a positive intiger")
    
    #default class assignment
    #important: we assume the nearestNeighboursIndexes is sorted based on distance ascending
    nearestPointDataIndex = nearestNeighboursIndexes[0]
    nearestPointClass = data[nearestPointDataIndex][-1]
    classMembership = nearestPointClass
    
    # creating list for counting the class occurances
    # [0, 0, 0] for classNum = 3
    classCount = []
    for i in range(classesNum):
        classCount.append(0)
        
    # count the classes 
    
    for x in nearestNeighboursIndexes:
        classCount[data[x][-1]] += 1
    
    topScore = max(classCount)
    topOwners = 0 #classes that have the same count as max
    
    # find the classes that have the same count as max
    for i in range(3):
        if classCount[i] == topScore:
            classMembership = i
            topOwners += 1
            
    # checking the outcomes
    # if there's a tie, do recursion[lovely]:
    if topOwners > 1:
        return determineClassMembership(data, nearestNeighboursIndexes[:-1], classesNum)
    elif topOwners != 1:
        raise ValueError("Didn't find a single fitting class to the top score somehow")
    else:
        return classMembership    
        
    
    
    
    
    
    
    