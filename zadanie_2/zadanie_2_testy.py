import utility as U #utility commands, such as fileLoader, splitList
import random
import seaborn as sns
from zadanie_2 import *



# simple function that returns a tuple of two points, represented by lists of length N
# where N is a random int number from 2-20
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
    
def testColors():
    from matplotlib.colors import ListedColormap
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    my_colors = ListedColormap(sns.color_palette(U.colorPallete))
    
    one = [5, 7, 8, 12, 4, 6, 2]
    two = [7, 6, 3, 1, 11, 9, 12]
    three = [7, 6, 3, 1, 11, 9, 12]
    four = [7, 6, 3, 1, 11, 9, 12]
    five = [7, 6, 3, 1, 11, 9, 12]
    six = [1, 4, 5, 1, 2, 3, 10]
    index = ['Jack', 'Jill', 'James',
         'Juliet', 'Jim', 'Jackie', 'Joe']
    df = pd.DataFrame({'green light': one,
                   'yellow light': two,
                   'red light': three,
                   'etc' : four,
                   'etcs' : five,
                   'etccc' : six}, index=index)
    ax = df.plot.bar(rot=0, colormap=my_colors)
    ax = df.plot.bar(rot=0)    
    
testEuclideanDistance()
testColors()


