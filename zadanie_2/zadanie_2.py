import matplotlib.pyplot as plt
import math
import pandas as pd
import utility as U #utility commands, such as fileLoader, splitList



# Does N (10) runs of our generic grouping algorithm for each of our K values (2-10).
# @param N - int, number of runs to be done.
# returns - best parameters achieved by each of the K-groupings.
def findBestResultsForK(normalized_data:list, N:int=10):
    
    bestResults = [None] * 8
    
    for k in range(8):
        clusters, centroids = groupWithKcentroids(normalized_data, k+2)
        bestResults[k] = WCSS(centroids, clusters, normalized_data)
        for i in range(N-1):
            clusters, centroids = groupWithKcentroids(normalized_data, k+2)
            current_WCSS = WCSS(centroids, clusters, normalized_data)
            if (bestResults[k] < current_WCSS):
                bestResults[k] = current_WCSS
    return bestResults

        
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

#returns - clusters (centroidoAligmentList), centroids
def groupWithKcentroids(data:list, K:int, cycles:int=250):
    
    # SELECTING INITIAL, RANDOM CENTROIDOS
    centroids = list()
    randomIndexes = U.selectRandomIndexes(data, K)
    for i in range (K):
        centroids.append(data[randomIndexes[i]])
    
    
    # CREATING ADDITIONAL BLANK LIST - REPRESENTING TO WHICH CENTROID A POINT BELONGS
    centroidoAlignmentList = list()
    for i in range(len(data)):
        centroidoAlignmentList.append(None)
        
        
    # DOING A SET NR OF CYCLES
    i = 0
    while (i < cycles):
        adjudicateCentroidos(data, centroids, centroidoAlignmentList)
        adjustCentroids(data, centroids, centroidoAlignmentList)
        i += 1
    
    return centroidoAlignmentList, centroids


# Updates algimentList to show the closest Centroido to each data point.
# @data - two dimensional list
# @centroid - one dimensional list of centroido points
# @aligmentList - one dimensional, list of which point belongs to which centroido
def adjudicateCentroidos(data:list, centroidos:list, aligmentList:list):
    
    for i in range(len(data)):
        aligmentList[i] = pickClosestPoint(data[i], centroidos)

# Finds which centroido Index is the closest one
# @point - one dimensional list describing the 4 coordinates of a point
# @centroidos - two dimensional list containing centroidos' dimensions
# returns - index of the closes centroido
def pickClosestPoint(point:list, centroidos:list):
    # First point as a comparisson
    closestIndex = 0
    closestDistance = euclideanDistance(point, centroidos[0])**2 
    for i in range (len(centroidos)-1):
        currentDistance = euclideanDistance(point, centroidos[i+1])**2
        if (currentDistance < closestDistance):
            closestDistance = currentDistance 
            closestIndex = i+1
    return closestIndex

# Finds new centroid
# @clusters - one dimensional list containing index of centroids
# @data -two dimensional list
# @centroid - index of centroid we want to adjust
# retruns - new centroid ([x, y, z, w])
def averageCentroid(clusters:list, data:list, centroid_index:int):
    
    new_centroid = [0, 0, 0, 0]
    x = 0 
    
    for i in range(len(data)):
        if(clusters[i] == centroid_index):
            x += 1
            for j in range(4):
                new_centroid[j] += data[i][j]
    
    for i in range(4):
        new_centroid[i] /= x 
    
    return new_centroid

# Adjusts all centroids in a given list
# @data - two dimensional list
# @centroids - two dimensional list containing current centroids
# @clusters - one dimensional list containing index of centroids
def adjustCentroids(data:list, centroids:list, clusters:list):
    
    for i in range(len(centroids)):
        centroids[i] = averageCentroid(clusters, data, i)
        
# Scales all of the traits to the [0, 1] range
# @data - two dimensional list
# returns - two dimensional list with scaled data
def minMaxScaling(data:list):
    
    #creating empty list for scaled data
    scaled_data = [[None for _ in range(len(data[0]))] for _ in range(len(data))]
    
    for i in range(len(data[0])):
        
        minimum = U.getMinimumTraits(data)[i] # min of current trait
        maximum = U.getMaximumTraits(data)[i] # max of current trait
        
        for j in range(len(data)):
            scaled_data[j][i] = (data[j][i] - minimum)/(maximum - minimum)
    
    return scaled_data

# Calculates WCSS (within-cluster sum of squares)
# @centroids - two dimensional list containing all centroids
# @clusters - one dimensional list containing index of centroids
# @data - two dimensional list
# returns - WCSS
def WCSS(centroids:list, clusters:list, data:list):
    
    sum_WCSS = 0;
    
    for i in range(len(centroids)):
        for j in range(len(clusters)):
            if(clusters[j] == i):
                sum_WCSS += euclideanDistance(data[j], centroids[i])**2
    
    return sum_WCSS
                
# generates ScatterPlot with 3 colored groups
# @trait_x, trait_y - indexes of traits
# @clusters - one dimensional list containing index of centroids
# @centroids - two dimensional list containing all centroids
def generateScatterPlot(data:list, trait_x:int, trait_y:int, axis, clusters:list, centroids:list):
    
    
    x = []
    y = []
    
    for i in range(len(data)):
        x.append(data[i][trait_x])
        y.append(data[i][trait_y])
    
    df = pd.DataFrame(dict(x=x, y=y, clusters=clusters))
    colors = {0:'red', 1:'green', 2:'blue'}
    
    axis.scatter(df['x'], df['y'], edgecolors=df['clusters'].map(colors), facecolors='none')
    
    #centroids
    centroids_x = [centroids[0][trait_x], centroids[1][trait_x], centroids[2][trait_x]]
    centroids_y = [centroids[0][trait_y], centroids[1][trait_y], centroids[2][trait_y]]
    
    axis.scatter(centroids_x, centroids_y, marker="D", s=120, c=['red', 'green', 'blue'])
    
    
    #in main(): plt.show()
    
    
        
    

