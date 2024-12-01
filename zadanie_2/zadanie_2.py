import matplotlib.pyplot as plt
import math
import utility as U #utility commands, such as fileLoader, splitList



# Does N (10) runs of our generic grouping algorithm for each of our K values (2-10).
# @param N - int, number of runs to be done.
# returns - best parameters achieved by each of the K-groupings.
def findBestResultsForK(N:int=10):
    
    raise NotImplementedError("Ta funkcja potrzebuje implementacji grupowania!")
    
    results = list()    # A 8 x 2 list
                        # first index [i] determines K-number(with a -2 offset)
                        # second index [j] determines: 0-ile cyklow; 1-jakosc dopasowania
                        # zapomnialem jak te miary jakosci wynikow sie nazywaja xDD

    for i in range(9):
        # firstReadout = findKgroups(i+2)
        # firstResults = list(firstReadout[0], firstReadout[1])
        # results[i].append(firstResults)
        for j in range(N):
            # readout = findKgroups(i+2)
            # if (readout[0] < results[i][0]):
            #     results[i][0] = readout[0]
            # if (readout[1] > results[i][1]):
            #     results[i][1] = readout[1]
                
            #all all the sequences
            print(i+2, ":", j)
        
    return results
        

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

def groupWithKcentroids(data:list, K:int, cycles:int=100):
    
    # SELECTING INITIAL, RANDOM CENTROIDOS
    centroidos = list()
    randomIndexes = U.selectRandomIndexes(data, K)
    for i in range (K):
        centroidos.append(data[randomIndexes[i]])
    
    
    # CREATING ADDITIONAL BLANK LIST - REPRESENTING TO WHICH CENTROID A POINT BELONGS
    centroidoAlignmentList = list()
    for i in range(len(data)):
        centroidoAlignmentList.append(None)
        
        
    # DOING A SET NR OF CYCLES
    i = 0
    while (i < cycles):
        adjudicateCentroidos(data, centroidos, centroidoAlignmentList)
        # adjustCentroidos(data, centroidos)
        i += 1

def adjudicateCentroidos(data:list, centroidos:list, aligmentList:list):
    
    for i in range(len(data)):
        aligmentList[i] = pickClosestPoint(data[i], centroidos)
    
def pickClosestPoint(point:list, centroidos:list):
    # First point as a comparisson
    closestIndex = 0
    closestDistance = euclideanDistance(point, centroidos[0]) 
    for i in range (len(centroidos)-1):
        currentDistance = euclideanDistance(point, centroidos[i+1])
        if (currentDistance < closestDistance):
            closestDistance = currentDistance 
            closestIndex = i+1
    return closestIndex
        
# groups traits based on centroids that were given
# @param data - two-dimensonial list
# @param m - two-dimensional list with three centroids
# @param trait1, trait2 - indexes
def group(data, m, trait1, trait2):
    
    S = [[],[],[]] #[S1, S2, S3]
    
    for x in data:
        p = [x[trait1], x[trait2]] #point
        for i in range(3):
            for j in range(1, 3):
                distance1 = euclideanDistance(p, m[i])**2 <= euclideanDistance(p, m[(i+j)%3])**2
                distance2 = euclideanDistance(p, m[i])**2 <= euclideanDistance(p, m[(i+j+1)%3])**2
                if(distance1 and distance2):
                        S[i].append(p)