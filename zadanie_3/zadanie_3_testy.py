from zadanie_3 import *

def testFindKNearestNeighbours():
    print("Test FIND K Nearest Neighbours")
    
    
    L = [4, 11, 9, 21, 3]
    
    
    print(findNearestNeighbours(1, L) == [4])
    print(findNearestNeighbours(2, L) == [4, 0])
    print(findNearestNeighbours(3, L) == [4, 0, 2])
    print(findNearestNeighbours(4, L) == [4, 0, 2, 1])
    print(findNearestNeighbours(5, L) == [4, 0, 2, 1, 3])
    
    print()
def testKnearestNeighbours():
    print("Test K Nearest Neighbours")
    
    fakeData = [
        [0, 0, 0, 0, 0],
        [100, 100, 100, 100, 1],
        [50, 50, 50, 50, 2]
        ]
    k = 1
    point0 = [0, 0, 0, 0]; point1 = [100, 100, 100, 100]; point2 = [50, 50, 50, 50];
    
    
    # temporarily commented to reduce bloat
    # print(kNearestNeighbours(fakeData, k, point0) == 0) 
    # print(kNearestNeighbours(fakeData, k, point1) == 1)
    # print(kNearestNeighbours(fakeData, k, point2) == 2)
    # print()
    # print(kNearestNeighbours(fakeData, k+1, point0) == 0)
    # print(kNearestNeighbours(fakeData, k+1, point1) == 1)
    # print(kNearestNeighbours(fakeData, k+1, point2) == 2)
    # print()
    print(kNearestNeighbours(fakeData, k+2, point0) == 0)
    print(kNearestNeighbours(fakeData, k+2, point1) == 1)
    print(kNearestNeighbours(fakeData, k+2, point2) == 2)
        
    print()
    


def testDetermineClassMembership():
    print("Test Determine Class Membership")
    classesNum = 3;
    fakeData = [
        [0, 0, 0, 0, 0],
        [100, 100, 100, 100, 1],
        [50, 50, 50, 50, 2]
        ]
    
    # In case of total draw, it should pick the first class
    nearestNeighboursIndexes = [2, 1, 0]
    print(determineClassMembership(fakeData, nearestNeighboursIndexes, classesNum) == 2)
    nearestNeighboursIndexes = [0, 1, 2]
    print(determineClassMembership(fakeData, nearestNeighboursIndexes, classesNum) == 0)
    print()
    

def testMinMaxScaling():
    print("Test Min Max Scaling")
    
    data = fileLoader("testData2.csv")
        
    scaled_data = minMaxScaling(data)
    
    print(roundList(scaled_data[0], 2) == [0.7, 0.6, 0.25, 0.33, 0])
    print(roundList(scaled_data[1], 2) == [0.5, 0.1, 0.25, 0.33, 0])
    print(roundList(scaled_data[2], 2) == [0.3, 0.3, 0, 0.33, 0])
    print(roundList(scaled_data[5], 2) == [1, 1, 1, 1, 1])
    print(roundList(scaled_data[8], 2) == [0, 0, 0.25, 0.33, 2])
    
    print()

    
def testOnRealData():

        

    
    print("Test Out For Real")
    trainData = fileLoader("data3_train.csv")
    classesNum = 3;
    testData = fileLoader("data3_test.csv")
    k = 3
    
    # somewhere here we should normalise both of them
    # normalise based on the trainData, NOT testData
    
    
    
    #for checking the results
    classCount = []
    for i in range(classesNum):
        classCount.append(0)
    
    
    for point in testData:
        #ignore the class assigment for the purposes of our guessing (the [:-1] part)
        classDetermined = kNearestNeighbours(trainData, k, point[:-1])
        classCount[classDetermined] += 1
        # print(classDetermined)
    
    print("Real class count is: [15, 15, 15]")
    print("What we've found is:", classCount) #we are 1 class assignment  off
    print()

testFindKNearestNeighbours()
testKnearestNeighbours()
testDetermineClassMembership()
testMinMaxScaling()

testOnRealData()