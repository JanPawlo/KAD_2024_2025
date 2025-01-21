import matplotlib.pyplot as plt
import math
import pandas as pd
import utility as U 


#snailcase
#nie uzywac funkcji void cosSieZmienia(listaktorasiezmienia)

def findBestResultsForK(normalized_data:list, N:int=10):
    
    bestResults = [None] * 9
    
    for k in range(9):
        clusters, centroids = groupWithKcentroids(normalized_data, k+2)
        bestResults[k] = WCSS(centroids, clusters, normalized_data)
        for i in range(N-1):
            clusters, centroids = groupWithKcentroids(normalized_data, k+2)
            current_WCSS = WCSS(centroids, clusters, normalized_data)
            if (bestResults[k] > current_WCSS):
                bestResults[k] = current_WCSS
    return bestResults

        
def euclideanDistance(p1:list, p2:list) -> float:


    if (len(p1) != len(p2)):

        raise Exception("euclideanDistanceNdim: Diffrent nr. of dimensions on points")
    
    dimensions = len(p1)
    
    total = 0

    for i in range (dimensions):
        word = p1[i] - p2[i]
        total += word * word
    distance = math.sqrt(total)
    
    return distance


def groupWithKcentroids(data:list, K:int, cycles:int=100):
    

    centroids = list()
    randomIndexes = U.selectRandomIndexes(data, K)
    for i in range (K):
        centroids.append(data[randomIndexes[i]])
    
    

    centroidoAlignmentList = []
    for i in range(len(data)):
        centroidoAlignmentList.append(None)
        
        

    i = 0
    while (i < cycles):
        adjudicateCentroidos(data, centroids, centroidoAlignmentList)
        adjustCentroids(data, centroids, centroidoAlignmentList)
        i += 1
    
    return centroidoAlignmentList, centroids



def adjudicateCentroidos(data:list, centroidos:list, aligmentList:list):
    
    for i in range(len(data)):
        aligmentList[i] = pickClosestPoint(data[i], centroidos)


def pickClosestPoint(point:list, centroidos:list):

    closestIndex = 0
    closestDistance = euclideanDistance(point, centroidos[0])**2 
    for i in range (len(centroidos)-1):
        currentDistance = euclideanDistance(point, centroidos[i+1])**2
        if (currentDistance < closestDistance):
            closestDistance = currentDistance 
            closestIndex = i+1
    return closestIndex


def averageCentroid(clusters:list, data:list, old_centroids:list, centroid_index:int):
    
    new_centroid = [0, 0, 0, 0]
    x = 0 
    
    for i in range(len(data)):
        if(clusters[i] == centroid_index):
            x += 1
            for j in range(4):
                new_centroid[j] += data[i][j]
    if (x==0):
        new_centroid = old_centroids[centroid_index]
    else:
        for i in range(4):
            new_centroid[i] /= x 
        
    return new_centroid

def adjustCentroids(data:list, centroids:list, clusters:list):
    
    for i in range(len(centroids)):
        centroids[i] = averageCentroid(clusters, data, centroids, i)
        

def minMaxScaling(data:list):
    

    scaled_data = [[None for _ in range(len(data[0]))] for _ in range(len(data))]
    
    for i in range(len(data[0])):
        
        minimum = U.getMinimumTraits(data)[i] # min of current trait
        maximum = U.getMaximumTraits(data)[i] # max of current trait
        
        for j in range(len(data)):
            scaled_data[j][i] = (data[j][i] - minimum)/(maximum - minimum)
    
    return scaled_data


def WCSS(centroids:list, clusters:list, data:list):
    
    sum_WCSS = 0;
    
    for i in range(len(centroids)):
        for j in range(len(clusters)):
            if(clusters[j] == i):
                sum_WCSS += euclideanDistance(data[j], centroids[i])**2
    
    return sum_WCSS
                
def generateScatterPlot(data:list, trait_x:int, trait_y:int, axis, clusters:list, centroids:list):
    
    
    x = []
    y = []
    
    for i in range(len(data)):
        x.append(data[i][trait_x])
        y.append(data[i][trait_y])
    
    df = pd.DataFrame(dict(x=x, y=y, clusters=clusters))
    colors = {0:'red', 1:'green', 2:'blue'}
    
    axis.scatter(df['x'], df['y'], edgecolors=df['clusters'].map(colors), facecolors='none')
    
    centroids_x = [centroids[0][trait_x], centroids[1][trait_x], centroids[2][trait_x]]
    centroids_y = [centroids[0][trait_y], centroids[1][trait_y], centroids[2][trait_y]]
    
    axis.scatter(centroids_x, centroids_y, marker="D", s=120, c=['red', 'green', 'blue'])
        
    
    

