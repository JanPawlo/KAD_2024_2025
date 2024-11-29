import utility as U #utility commands, such as fileLoader, splitList
import random
from zadanie_2 import *




def generate2randomPoints():
    dimensions = random.randint%20 + 2
    
    
    pointA = list()
    pointB = list()
    for i in range(dimensions):
        pointA.append(random.random())
        pointB.append(random.random())
    return (pointA, pointB)


def check(val1, val2, expectedResult:bool=True):
    print( (round(val1, 3) == round(val2), 3) == expectedResult)

def testEuclideanDistance():
    point0 = (0, 0)
    point1 = (1, 1)
    
    print(euclideanDistance(point0, point1), math.sqrt(2))
    check( euclideanDistance(point0, point1), math.sqrt(2))
    
    
    
testEuclideanDistance()