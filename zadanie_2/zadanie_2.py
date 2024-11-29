import matplotlib.pyplot as plt
import math



# calculates euclideanDistance between 2 points located in ANY ammount dimensions
# @param p1, p2 - lists [x, y, z, ... ]
# @return float
def euclideanDistance(p1:list, p2:list) -> float:
    
    # CHECKING VALUES
    if (p1.length != p2.length):
        raise Exception("euclideanDistanceNdim: Diffrent nr. of dimensions on points")
    
    dimensions = p1.length
    
    total = 0
    # SUMATION
    for i in range (dimensions):
        word = p1[i] - p2[i]
        total += word * word
    distance = math.sqrt(total)
    
    return distance
    
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