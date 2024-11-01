# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 17:17:31 2024

@author: Jan Pawłowski
@author: Emil Franczak
"""


import matplotlib.pyplot as plt
from zadanie_1 import fileLoader, countThreeSpecies, speciesShareOfPopulation, getMinimumTraits, getAverageTraits, getMedianTraits, getMaximumTraits, getQuartilesTraits, getStandardDeviationTraits, generateHistogram, generateBoxPlot

def main():
    print("---- Zadanie 1 ----")
    
    data = fileLoader("data1.csv")
    
    
    print()
    print("Tabela 1. Liczności gatunku irysów.")
    
    # two dictionaries with species names as keys
    # one containing species count and the other species share
    species_count = countThreeSpecies(data)
    species_share = speciesShareOfPopulation(species_count)
    
    #printing the table (species name;species count(spiecies share))
    print("Setosa;" +  str(species_count["setosa"]) +"("+ str(round(species_share["setosa"]*100, 1))+"%)")
    print("Versicolor;" + str(species_count["versicolor"]) +"("+ str(round(species_share["versicolor"]*100, 1))+"%)")
    print("Virginica;" + str(species_count["virginica"]) +"("+ str(round(species_share["virginica"]*100, 1))+"%)")
    print("Total;"+ str(len(data))+"(100.0%)")
    
    
    print()
    print("Tabela 2. Charakterystyka cech irysów.")
        
    minimum = getMinimumTraits(data)
    maximum = getMaximumTraits(data)
    average = getAverageTraits(data)
    median = getMedianTraits(data)
    quartiles = getQuartilesTraits(data)
    deviation = getStandardDeviationTraits(data)
    
    print("Długość działki kielicha (cm);" + str(round(minimum["sepal_length"], 2)) + ";" + str(round(average["sepal_length"], 2)) + "(+-" + str(round(deviation["sepal_length"], 2)) + ");" + str(round(median["sepal_length"], 2)) + "(" + str(round(quartiles["sepal_length"][0], 2)) + " - " + str(round(quartiles["sepal_length"][2], 2)) + ");" + str(round(maximum["sepal_length"], 2)))
    print("Szerokość działki kielicha (cm);" + str(round(minimum["sepal_width"], 2)) + ";" + str(round(average["sepal_width"], 2)) + "(+-" + str(round(deviation["sepal_width"], 2)) + ");" + str(round(median["sepal_width"], 2)) + "(" + str(round(quartiles["sepal_width"][0], 2)) + " - " + str(round(quartiles["sepal_width"][2], 2)) + ");" + str(round(maximum["sepal_width"], 2)))
    print("Długość płatka (cm);" + str(round(minimum["petal_length"], 2)) + ";" + str(round(average["petal_length"], 2)) + "(+-" + str(round(deviation["petal_length"], 2)) + ");" + str(round(median["petal_length"], 2)) + "(" + str(round(quartiles["petal_length"][0], 2)) + " - " + str(round(quartiles["petal_length"][2], 2)) + ");" + str(round(maximum["petal_length"], 2)))
    print("Szerokość płatka (cm));" + str(round(minimum["petal_width"], 2)) + ";" + str(round(average["petal_width"], 2)) + "(+-" + str(round(deviation["petal_width"], 2)) + ");" + str(round(median["petal_width"], 2)) + "(" + str(round(quartiles["petal_width"][0], 2)) + " - " + str(round(quartiles["petal_width"][2], 2)) + ");" + str(round(maximum["petal_width"], 2)))

    
    figure, axis = plt.subplots(1, 2, figsize=(15, 6)) # rows, columns
    
    axis[0].set_title("Długość działki kielicha")
    generateHistogram(data, "sepal_length", [4.0,4.5,5,5.5,6,6.5,7,7.5,8], axis[0])
    generateBoxPlot(data, "sepal_length", axis[1])
    
    plt.show()
    


    

    
    

main()
    
