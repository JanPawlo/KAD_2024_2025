import math

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

# @param point - classified object
def kNearestNeighbours(data:list, k:int, point:list):
    
    # 1. Calculate the Euclidean distance between p and all points in the dataset, storing the results in the list L.
    listL = []
    
    for x in data:
        listL.append(euclideanDistance(x, point))
    
    # 2. Identify k points in L with the smallest distance from p.
    # 3. Determine the most common class among the k closest points.
    
    return 0;