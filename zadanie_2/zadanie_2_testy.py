import utility as U 
import random
from zadanie_2 import *




def testAssignCentroidos():
    print("Test Assign Centroidos")
    data = [[0, 0, 0],
            [100, 100, 100],
            [1, 1, 1],
            [90, 90, 90]
            ]
    centroidoAlignmentList = list()
    for i in range(len(data)):
        centroidoAlignmentList.append(None)
        
    adjudicateCentroidos(data, [data[0]], centroidoAlignmentList)
    if (centroidoAlignmentList == [0, 0, 0, 0]):
        print(True)
    else:
        print(False)
    adjudicateCentroidos(data, [data[0], data[1]], centroidoAlignmentList)
    if (centroidoAlignmentList == [0, 1, 0, 1]):
        print(True)
    else:
        print(False)
    
    print()


def generate2randomPoints():
    dimensions = random.randint(2, 20)
    
    
    pointA = list()
    pointB = list()
    for i in range(dimensions):
        pointA.append(random.uniform(-0.5, 0.5))
        pointB.append(random.uniform(-0.5, 0.5))
    return (pointA, pointB)

def check(val1, val2, rounding:int=5, expectedResult:bool=True):
    print( (round(val1, rounding) == round(val2, rounding)) == expectedResult)



def testEuclideanDistance():
    print("Test Euclidean Distance")
    point0 = (0, 0)
    point1 = (1, 1)
    
    square_side = random.random()
    pointSQ = (square_side, square_side)
    
    check(euclideanDistance(point0, point1), math.sqrt(2))
    check(euclideanDistance(point0, pointSQ), math.sqrt(2)*square_side)
    
    
    pointN, pointM = generate2randomPoints();
    expectedDistance = 0
    for i in range(len(pointN)):
        expectedDistance += (pointN[i] - pointM[i])**2
    expectedDistance = math.sqrt(expectedDistance)
    

    check(euclideanDistance(pointN, pointM), expectedDistance)
    check(euclideanDistance(pointN, pointM), euclideanDistance(pointM, pointN))
    
    print()
    
    
def testSelectRandomIndexes():
    print("Test Select Random Indexes")
    lista = [0, 1, 2, 3, 4, 5, 6]
    wybrane = U.selectRandomIndexes(lista, 3)
    for x in wybrane:
        if not (x in {0, 1, 2, 3, 4, 5, 6}):
            print(False, end=" ")
        else:
            print(True, end=" ")
    print("\n")

def testAppendColumnToList():
    print("Test Append Column To List")
    
    lista = [[1, 2, 3],
             [1, 2, 3],
             [1, 2, 3],
             ]
    U.appendColumnToList(lista)
    if (len(lista)==3 and len(lista[0])==4 and len(lista[2])==4):
        print(True)
    else:
        print(False)
    print()
    
def testAverageCentroid():
    print("Test Average Centroid")
    
    data = U.fileLoader("testData2.csv")
    clusters = [0, 0, 0, 0, 0, 0, 0, 1, 1, 2]
    
    print(U.roundList(averageCentroid(clusters, data, 2), 2) == [4.9, 3.1, 1.5, 0.1])
    print(U.roundList(averageCentroid(clusters, data, 1), 2) == [4.7, 3.15, 1.45, 0.2])
    print(U.roundList(averageCentroid(clusters, data, 0), 2) == [4.9, 3.39, 1.44, 0.24])
    
    print()
    
def testAdjustCentroid():
    print("Test Adjust Centroid")
    
    data = U.fileLoader("testData2.csv")
    centroids = [[1, 2, 3, 4], [0, 0, 0, 0], [1000,1000,1000,100]]
    clusters = [0, 0, 0, 0, 0, 0, 0, 1, 1, 2]
    
    adjustCentroids(data, centroids, clusters)
    
    print(U.roundList(centroids[2], 2) == [4.9, 3.1, 1.5, 0.1])
    print(U.roundList(centroids[1], 2) == [4.7, 3.15, 1.45, 0.2])
    print(U.roundList(centroids[0], 2) == [4.9, 3.39, 1.44, 0.24])
    
    print()

def testMinMaxScaling():
    print("Test Min Max Scaling")
    
    data = U.fileLoader("testData2.csv")

    scaled_data = minMaxScaling(data)
    
    print(U.roundList(scaled_data[0], 2) == [0.7, 0.6, 0.25, 0.33])
    print(U.roundList(scaled_data[1], 2) == [0.5, 0.1, 0.25, 0.33])
    print(U.roundList(scaled_data[2], 2) == [0.3, 0.3, 0, 0.33])
    print(U.roundList(scaled_data[5], 2) == [1, 1, 1, 1])
    print(U.roundList(scaled_data[8], 2) == [0, 0, 0.25, 0.33])
    
    print()


testEuclideanDistance()
testSelectRandomIndexes()
testAppendColumnToList()
testAssignCentroidos()
testAverageCentroid()
testAdjustCentroid()
testMinMaxScaling()