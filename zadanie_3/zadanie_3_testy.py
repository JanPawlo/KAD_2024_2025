from zadanie_3 import *

def testFindKNearestNeighbours():
    
    L = [4, 11, 9, 21, 3]
    
    
    print(findNearestNeighbours(1, L) == [4])
    print(findNearestNeighbours(2, L) == [4, 0])
    print(findNearestNeighbours(3, L) == [4, 0, 2])
    print(findNearestNeighbours(4, L) == [4, 0, 2, 1])
    print(findNearestNeighbours(5, L) == [4, 0, 2, 1, 3])
    
    
testFindKNearestNeighbours()

