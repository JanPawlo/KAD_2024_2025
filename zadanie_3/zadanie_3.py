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
        for j in range(5):
            dataTable[i][j] = float(dataTable[i][j])
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
def kNearestNeighbours(data:list, k:int, point:list):
    
    L = []
    nearestNeighbours = []
    
    # 1. Calculate the Euclidean distance between p and all points in the dataset, storing the results in the list L.    
    for x in data:
        L.append(euclideanDistance(x[:4], point)) 
    
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

# @param classesNum -> number of classes
# NOT FINISHED
def ClassMembership(data:list, nearestNeighboursIndexes:list, classesNum:int):
    
    # creating list with classesNum elements with each element equal to 0
    classCount = []
    for i in range(classesNum):
        classCount.append(0)
        
    # count the classes 
    for x in nearestNeighboursIndexes:
        classCount[data[x][-1]] += 1
    
    # determine the most common class
    # NOT FINISHED
    classMembership = 0
    for i in range(1, classesNum):
        if(classCount[classMembership] < classCount[i]):
            classMembership = i
        # else if((classCount[classMembership] == classCount[i]))
    
    return classMembership
    
            