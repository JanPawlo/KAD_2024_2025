import utility as U #utility commands, such as fileLoader, splitList
# import seaborn as sns
from zadanie_2 import *
import matplotlib.pyplot as plt


def main():
    
    data = U.fileLoader("data2.csv")
    normalized_data = minMaxScaling(data)
    
    
    # finding the best WCSS (potentially could be implemented as function)
    clusters, centroids = groupWithKcentroids(normalized_data, 3)
    current_WCSS = WCSS(centroids, clusters, normalized_data)
    for i in range(10):
        new_clusters, new_centroids = groupWithKcentroids(normalized_data, 3)
        if(current_WCSS > WCSS(new_centroids, new_clusters, normalized_data)):
            current_WCSS = WCSS(new_centroids, new_clusters, normalized_data)
            clusters, centroids = new_clusters, new_centroids
            
    # "denormalize" centroids
    for i in range(4):
        minimum = U.getMinimumTraits(data)[i] # min of current trait
        maximum = U.getMaximumTraits(data)[i] # max of current trait
        for j in range(3):
            centroids[j][i] = centroids[j][i]*(maximum - minimum) + minimum
    
    
    # Displaying the scatter plots with grouping
    figure, axis = plt.subplots(3, 2, figsize=(10, 14)) # rows, columns
    figure.tight_layout(pad=4.0) # adjusting padding between plots

    generateScatterPlot(data, 0, 1, axis[0][0], clusters, centroids)
    axis[0][0].set_xlabel("Długość działki kielicha (cm)") # Dlugosc dzialki kielicha w 1
    axis[0][0].set_ylabel("Szerokość działki kielicha (cm)") #szerokosc dzialki kielicha w 1 
    
    generateScatterPlot(data, 0, 2, axis[0][1], clusters, centroids)
    axis[0][1].set_xlabel("Długość działki kielicha (cm)") 
    axis[0][1].set_ylabel("Długość płatka (cm)")
    
    generateScatterPlot(data, 0, 3, axis[1][0], clusters, centroids)
    axis[1][0].set_xlabel("Długość działki kielicha (cm)") 
    axis[1][0].set_ylabel("Szerokość płatka (cm)")
    
    generateScatterPlot(data, 1, 2, axis[1][1], clusters, centroids)
    axis[1][1].set_xlabel("Szerokość działki kielicha (cm)") 
    axis[1][1].set_ylabel("Długość płatka (cm)")
    
    generateScatterPlot(data, 1, 3, axis[2][0], clusters, centroids)
    axis[2][0].set_xlabel("Szerokość działki kielicha (cm)") 
    axis[2][0].set_ylabel("Szerokość płatka (cm)")
    
    generateScatterPlot(data, 2, 3, axis[2][1], clusters, centroids)
    axis[2][1].set_xlabel("Długość płatka (cm)") 
    axis[2][1].set_ylabel("Szerokość płatka (cm)")
    
    plt.show()
    
    #generate WCSS for k=2,3,...,10
    WCSS_list = list()
    for i in range(2, 11):
        clusters, centroids = groupWithKcentroids(normalized_data, i)
        WCSS_list.append(WCSS(centroids, clusters, normalized_data))
    
    
    plt.plot(range(2, 11), WCSS_list, marker='o', markerfacecolor='red')  
    plt.xlabel('Liczba klastrów (k)')
    plt.ylabel('WCSS')
     
    
    return 0;

main()