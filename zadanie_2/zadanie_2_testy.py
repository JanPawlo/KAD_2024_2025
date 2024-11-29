import utility as U #utility commands, such as fileLoader, splitList
import random
from zadanie_2 import *




def generate2randomPoints():
    dimensions = random.randint(2, 20)
    
    
    pointA = list()
    pointB = list()
    for i in range(dimensions):
        pointA.append(random.random())
        pointB.append(random.random())
    return (pointA, pointB)


def check(val1, val2, rounding:int=5, expectedResult:bool=True):
    print( (round(val1, rounding) == round(val2, rounding)) == expectedResult)

def testEuclideanDistance():
    point0 = (0, 0)
    point1 = (1, 1)
    
    square_side = random.random()
    pointSQ = (square_side, square_side)
    
    
    
    check(euclideanDistance(point0, point1), math.sqrt(2))
    check(euclideanDistance(point0, pointSQ), math.sqrt(2)*square_side)
    
    
    
testEuclideanDistance()