import utility as U #utility commands, such as fileLoader, splitList
import random
import seaborn as sns
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

# simple function that returns a tuple of two points, represented by lists of length N
# where N is a random int number from 2-20
# for use in testing
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
    # 3x3 list
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

# def testColors():
#     from matplotlib.colors import ListedColormap
#     import pandas as pd
#     import seaborn as sns
#     import matplotlib.pyplot as plt
#     my_colors = ListedColormap(sns.color_palette(U.colorPallete))
    
#     one = [5, 7, 8, 12, 4, 6, 2]
#     two = [7, 6, 3, 1, 11, 9, 12]
#     three = [7, 6, 3, 1, 11, 9, 12]
#     four = [7, 6, 3, 1, 11, 9, 12]
#     five = [7, 6, 3, 1, 11, 9, 12]
#     six = [1, 4, 5, 1, 2, 3, 10]
#     index = ['Jack', 'Jill', 'James',
#          'Juliet', 'Jim', 'Jackie', 'Joe']
#     df = pd.DataFrame({'green light': one,
#                    'yellow light': two,
#                    'red light': three,
#                    'etc' : four,
#                    'etcs' : five,
#                    'etccc' : six}, index=index)
#     ax = df.plot.bar(rot=0, colormap=my_colors)
#     ax = df.plot.bar(rot=0)    
    
testEuclideanDistance()
# testColors()
testSelectRandomIndexes()
testAppendColumnToList()
testAssignCentroidos()