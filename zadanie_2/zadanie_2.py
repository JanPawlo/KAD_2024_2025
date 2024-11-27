import matplotlib.pyplot as plt
import math


# calculates euclideanDistance between p1 and p2
# @param p1, p2 - lists [x, y]
# @return float
def euclideanDistance(p1, p2):
    distance = math.sqrt((p1[0]-p2[0])**2 +  (p1[1]-p2[1])**2)
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