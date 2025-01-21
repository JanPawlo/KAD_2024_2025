import utility as U #utility commands, such as fileLoader, splitList
# import seaborn as sns
from zadanie_2 import *
import matplotlib.pyplot as plt


def main():
    
    data = U.fileLoader("data2.csv")
    normalized_data = minMaxScaling(data)
    
    #wynik dla k=3
    clusters, centroids = groupWithKcentroids(normalized_data, 3)
    current_WCSS = WCSS(centroids, clusters, normalized_data)
    
    # do prezentacji k=3, nie robimy chyba wyboru najlepszego z kilku
    # new_clusters, new_centroids = groupWithKcentroids(normalized_data, 3)
    # if(current_WCSS > WCSS(new_centroids, new_clusters, normalized_data)):
    #     current_WCSS = WCSS(new_centroids, new_clusters, normalized_data)
    #     clusters, centroids = new_clusters, new_centroids
    
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
    X_points = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    # finding the best WCSS for each K
    WCSS_list = findBestResultsForK(normalized_data)
    for i in range(len(WCSS_list)):
        print("Najlepszy wynik dla k:", i+2, "WCSS =", round(WCSS_list[i], 1), "100 cyklow")
    
    plt.figure(figsize=(8, 6), dpi=200)
    plt.plot(range(2, 11), WCSS_list, marker='o', markerfacecolor='red')  
    for a,b in zip(X_points, WCSS_list):
        wynik = str(round(b, 1))
        wynik = U.dotToComma(wynik)
        plt.text(a, b, wynik, ha='left', va='bottom')
    plt.xlabel('Liczba klastrów (k)')
    plt.ylabel('WCSS')
     
    
    return 0;

main()