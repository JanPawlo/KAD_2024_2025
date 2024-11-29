import utility as U #utility commands, such as fileLoader, splitList
import random
from zadanie_2 import *




def generate2randomPoints():
    dimensions = random.randint(2, 20)
    
    
    pointA = list()
    pointB = list()
    for i in range(dimensions):
        pointA.append(random.uniform(-0.5, 0.5))
        pointB.append(random.uniform(-0.5, 0.5))
    return (pointA, pointB)

# simple function that rounds result before comparing it with the compared value
# by default we expect them to be equal
def check(val1, val2, rounding:int=5, expectedResult:bool=True):
    print( (round(val1, rounding) == round(val2, rounding)) == expectedResult)



def testEuclideanDistance():
    print("Test Euclidean Distance")
    point0 = (0, 0)
    point1 = (1, 1)
    
    square_side = random.random()
    pointSQ = (square_side, square_side)
    
    #basic
    check(euclideanDistance(point0, point1), math.sqrt(2))
    check(euclideanDistance(point0, pointSQ), math.sqrt(2)*square_side)
    
    
    #random
    pointN, pointM = generate2randomPoints();
    expectedDistance = 0
    for i in range(len(pointN)):
        expectedDistance += (pointN[i] - pointM[i])**2
    expectedDistance = math.sqrt(expectedDistance)
    
    #check normal
    check(euclideanDistance(pointN, pointM), expectedDistance)
    #check reversed
    check(euclideanDistance(pointN, pointM), euclideanDistance(pointM, pointN))

    
    
    print()
    
    
testEuclideanDistance()