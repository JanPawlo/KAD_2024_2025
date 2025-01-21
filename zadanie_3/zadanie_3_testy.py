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
    point0 = [0, 1, 1, -1]; point1 = [100, 80, 80, 120]; point2 = [50, 40, 60, 70];
    print("k == 1")
    print("0:",kNearestNeighbours(fakeData, k, point0) == 0, kNearestNeighbours(fakeData, k, point0)) 
    print("1:",kNearestNeighbours(fakeData, k, point1) == 1, kNearestNeighbours(fakeData, k, point1))
    print("2:",kNearestNeighbours(fakeData, k, point2) == 2, kNearestNeighbours(fakeData, k, point2))

    print("k == 2")
    print("0:", kNearestNeighbours(fakeData, k+1, point0) == 0, kNearestNeighbours(fakeData, k+1, point0))
    print("1:",kNearestNeighbours(fakeData, k+1, point1) == 1, kNearestNeighbours(fakeData, k+1, point1))
    print("2:",kNearestNeighbours(fakeData, k+1, point2) == 2, kNearestNeighbours(fakeData, k+1, point2))

    print("k == 3")
    print("0:",kNearestNeighbours(fakeData, k+2, point0) == 0, kNearestNeighbours(fakeData, k+2, point0))
    print("1:",kNearestNeighbours(fakeData, k+2, point1) == 1, kNearestNeighbours(fakeData, k+2, point1))
    print("2:",kNearestNeighbours(fakeData, k+2, point2) == 2, kNearestNeighbours(fakeData, k+2, point2))
        
    print()


    
testFindKNearestNeighbours()
testKnearestNeighbours()
