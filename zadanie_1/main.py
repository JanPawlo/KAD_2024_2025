# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 17:17:31 2024

@author: Jan Pawłowski
@author: Emil Franczak
"""


import matplotlib.pyplot as plt
from zadanie_1 import fileLoader, countThreeSpecies, speciesShareOfPopulation, getMinimumTraits, getAverageTraits, getMedianTraits, getMaximumTraits, getQuartilesTraits, getStandardDeviationTraits, generateHistogram, generateBoxPlot, generateScatterPlot, getPearsonsCorrelation, getOffsetPearson

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

    
    figure, axis = plt.subplots(4, 2, figsize=(12, 16)) # rows, columns
    figure.tight_layout(pad=4.0) # adjusting padding between plots
    
    axis[0][0].set_title("Długość działki kielicha")
    generateHistogram(data, "sepal_length", [4.0,4.5,5,5.5,6,6.5,7,7.5,8], axis[0][0])
    generateBoxPlot(data, "sepal_length", axis[0][1])
    
    axis[1][0].set_title("Szerokość działki kielicha")
    generateHistogram(data, "sepal_width", [1.0,1.5,2,2.5,3,3.5,4,4.5,5], axis[1][0])
    generateBoxPlot(data, "sepal_width", axis[1][1])
    
    axis[2][0].set_title("Długość płatka")
    generateHistogram(data, "petal_length", 12, axis[2][0])
    generateBoxPlot(data, "petal_length", axis[2][1])
    
    axis[3][0].set_title("Szerokość płatka")
    generateHistogram(data, "petal_width", 12, axis[3][0])
    generateBoxPlot(data, "petal_width", axis[3][1])
    
    plt.show()
    
    
    figure, axis = plt.subplots(4, 2, figsize=(10, 14)) # rows, columns
    figure.tight_layout(pad=4.0) # adjusting padding between plots


    pearsonsCorrelation01 = getPearsonsCorrelation(data, "sepal_length", "sepal_width")
    b = getOffsetPearson(average["sepal_length"], average["sepal_width"], pearsonsCorrelation01)
    
    title = "r =" + str(round(pearsonsCorrelation01, 2)) + "; y = ??? + " + str(round(b, 1))
    axis[0][0].set_title(title)
    generateScatterPlot(data, "sepal_length", "sepal_width", axis[0][0])
    axis[0][0].set_xlabel("Dlugosc dzialki kielicha (cm)") # Dlugosc dzialki kielicha w 1
    axis[0][0].set_ylabel("Szerokosc dzialki kielicha (cm)") #szerokosc dzialki kielicha w 1
    
    
    # dodanie lini, dosc chaotyczne, daloby sie to ladnie ujac
    # cos jest nie tak, wynik wychodzi zle, moze gdzies po drodze pomijamy jakies dane? albo zaokragalamy?
    
    
    line_x = [minimum["sepal_length"], maximum["sepal_length"]]
    line_y = [minimum["sepal_length"]*pearsonsCorrelation01 + b, maximum["sepal_length"] * pearsonsCorrelation01 + b]
    axis[0][0].plot(line_x, line_y, color="red")
    
    plt.show()
    


    

    
    

main()
    
