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

def getMinimumTraits(data:list) -> list:
    
    minimumTraits = []
    for i in range(len(data[0])):
        minimumTraits.append(float('inf'))
    
    for x in data:
        for i in range(len(data[0])):
            if x[i] < minimumTraits[i]:
                minimumTraits[i] = x[i]
                
    return minimumTraits
                
def getMaximumTraits(data:list) -> list:
    
    maximumTraits = []
    for i in range(len(data[0])):
        maximumTraits.append(0)
    
    for x in data:
        for i in range(len(data[0])):
            if x[i] > maximumTraits[i]:
                maximumTraits[i] = x[i]
                
    return maximumTraits

                    
def minMaxScaling(data:list):
    
    scaled_data = [[None for _ in range(len(data[0])-1)] for _ in range(len(data))]
    
    for i in range(len(data[0])-1):
        
        minimum = getMinimumTraits(data)[i] # min of current trait
        maximum = getMaximumTraits(data)[i] # max of current trait
        
        for j in range(len(data)):
            scaled_data[j][i] = (data[j][i] - minimum)/(maximum - minimum)
        
    # add classes
    for i in range(len(data)):
        scaled_data[i].append(data[i][-1])
    
    return scaled_data

                
# @param point - data point that is going to be normalized
# @param trainingData - 2D list with training data
def minMaxScalingPoint(point:list, trainingData:list):
    
    if(len(point) != len(trainingData[0])):
        raise Exception("Diffrent nr. of dimensions on data")
    
    scaled_point = [None for _ in range(len(point))]
    
    for i in range(len(point)-1):
        minimum = getMinimumTraits(trainingData)[i] # min of current trait
        maximum = getMaximumTraits(trainingData)[i] # max of current trait
        
        scaled_point[i] = (point[i] - minimum)/(maximum - minimum)
    
    scaled_point[-1] = point[-1] # append the class
    
    return scaled_point

def roundList(lista:list, dokladnosc:int):
    return [round(x, dokladnosc) for x in lista]
    
# @param testData, trainingData - lists with normalised data
# @returns - list with percentage of succeses for each k: [k=1, k=2, ..., k=15]
def getKNNSuccessPercentage(testData:list, trainingData:list):
    
    successPercentage = []
    
    for k in range(15):
        successPercentage.append(0) 
        for x in testData:
            if(x[-1] == kNearestNeighbours(trainingData, k+1, x[:-1])):
                successPercentage[k] += 1 # if success add 1
        successPercentage[k] /= len(testData) # convert to %
        successPercentage[k] *= 100
        
    return successPercentage
            
# Cuts out 3 out of 5 columns from the orignal "data" list
# requires a < b, doesn't allow for the removal of last column (where class is) (index 4)

# @param Data - original list (could be both test and training)
# @param a - int index of the trait to be picked <0,1,2,3>
# @param b - int index of the trait to be picked <0,1,2,3>
# @return a list with selected 2 of the 4 traits
def reduceToTwoDimensions(data:list, a:int, b:int):
    if a not in(0, 1, 2, 3):
        raise ValueError("parameter A is out of range for the data, stay within 0-3")
    elif b not in(0, 1, 2, 3):
        raise ValueError("parameter B is out of range for the data, stay within 0-3")
    elif a == b:
        raise ValueError("parameters A and B cannot be the same")
    elif a > b:
        raise ValueError("parameter A should(?) be smaller than B")
        
    reducedList = list()
    
    for i in range(len(data)):
        reducedList.append(list())
        reducedList[i].append(data[i][a])
        reducedList[i].append(data[i][b])
        reducedList[i].append(data[i][4])
    
    return reducedList

def calculateConfusionMatrix(testData, trainingData, k):
    confusionMatrix = list()
    for i in range(3):
        confusionMatrix.append(list())
        for j in range(3):
            confusionMatrix[i].append(0)
    # confusion matrix
    # [ 
    # [0, 0, 0],
    # [0, 0, 0],
    # [0, 0, 0]
    # ]
    # print(confusionMatrix)

    # successPercentage.append(0) 
    for x in testData:
        # first is guess, second is true
        guess = kNearestNeighbours(trainingData, k, x[:-1])
        true = x[-1]
        confusionMatrix[guess][true] +=1
    
    
    return confusionMatrix
    
    
    

    # for k in range(15):
    #     successPercentage.append(0) 
    #     for x in testData:
    #         if(x[-1] == kNearestNeighbours(trainingData, k+1, x[:-1])):
    #             successPercentage[k] += 1 # if success add 1
    #     successPercentage[k] /= len(testData) # convert to %
    