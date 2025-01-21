from zadanie_3 import *
import matplotlib.pyplot as plt

def main():
    
    # load data
    trainingData = fileLoader('data3_train.csv') 
    testData = fileLoader('data3_test.csv')
    
    #normalize data
    normalizedTrainingData = minMaxScaling(trainingData)
    normalizedTestData = [minMaxScalingPoint(x, trainingData) for x in testData]
    
    k =[]
    for i in range(1, 16):
        k.append(i)
    
    
    plt.bar(k, getKNNSuccessPercentage(normalizedTestData, normalizedTrainingData))
    plt.ylim(90, 100)
    # plt.title() -- wszystkie cechy
    plt.show()

    # calculateConfusionMatrix(normalizedTestData, normalizedTrainingData)
    
    figure, axis1 = plt.subplots(3, 1, figsize=(10, 14))
    
    reducedTrainingData = reduceToTwoDimensions(normalizedTrainingData, 0, 1)
    reducedTestData = reduceToTwoDimensions(normalizedTestData, 0, 1)
    axis1[0].bar(k, getKNNSuccessPercentage(reducedTestData, reducedTrainingData))
    axis1[0].set_ylim(60, 100)
    axis1[0].set_xlabel('k')
    # axis1[0].title --- dlugosc dzialki kielicha, szerokosc dzialki kielicha
    
    reducedTrainingData = reduceToTwoDimensions(normalizedTrainingData, 0, 2)
    reducedTestData = reduceToTwoDimensions(normalizedTestData, 0, 2)
    axis1[1].bar(k, getKNNSuccessPercentage(reducedTestData, reducedTrainingData))
    axis1[1].set_ylim(90, 100)
    axis1[1].set_xlabel('k')
    # axis1[1].title --- dlugosc dzialki kielicha, dlugosc platka
    
    reducedTrainingData = reduceToTwoDimensions(normalizedTrainingData, 0, 3)
    reducedTestData = reduceToTwoDimensions(normalizedTestData, 0, 3)
    axis1[2].bar(k, getKNNSuccessPercentage(reducedTestData, reducedTrainingData))
    axis1[2].set_ylim(90, 100)
    axis1[2].set_xlabel('k')
    # axis1[2].title --- dlugosc dzialki kielicha, szerokosc platka
    
    figure, axis2 = plt.subplots(3, 1, figsize=(10, 14))
    
    reducedTrainingData = reduceToTwoDimensions(normalizedTrainingData, 1, 2)
    reducedTestData = reduceToTwoDimensions(normalizedTestData, 1, 2)
    axis2[0].bar(k, getKNNSuccessPercentage(reducedTestData, reducedTrainingData))
    axis2[0].set_ylim(90, 100)
    axis2[0].set_xlabel('k')
    # axis2[0].title --- szerokosc dzialki kielicha, dlugosc platka
    
    reducedTrainingData = reduceToTwoDimensions(normalizedTrainingData, 1, 3)
    reducedTestData = reduceToTwoDimensions(normalizedTestData, 1, 3)
    axis2[1].bar(k, getKNNSuccessPercentage(reducedTestData, reducedTrainingData))
    axis2[1].set_ylim(90, 100)
    axis2[1].set_xlabel('k')
    # axis2[1].title --- szerokosc dzialki kielicha, szerokosc platka
    
    reducedTrainingData = reduceToTwoDimensions(normalizedTrainingData, 2, 3)
    reducedTestData = reduceToTwoDimensions(normalizedTestData, 2, 3)
    axis2[2].bar(k, getKNNSuccessPercentage(reducedTestData, reducedTrainingData))
    axis2[2].set_ylim(90, 100)
    axis2[2].set_xlabel('k')
    # axis2[1].title --- dlugosc platka, szerokosc platka
    
    return 0;
    
main()




