import matplotlib.pyplot as plt
import math


# subtracts two point (p1 - p2)
# @param p1, p2 - lists [x, y]
# @return list with the result
def subtract_points(p1, p2):
    return [p1[0]-p2[0], p1[1]-p2[1]]

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
                    cmp_p1 = (subtract_points(p, m[i]))**2
                    cmp_p2 = (subtract_points(p,m[(i+j)%3]))**2
                    if( (cmp_p1[0] <= cmp_p2[0]) and (cmp_p1[1] <= cmp_p2[1])):
                        S[i].append(p)