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
    
    plt.figure(figsize=(10,5))
    plt.bar(k, getKNNSuccessPercentage(normalizedTestData, normalizedTrainingData)) 
    plt.ylim(90, 101)
    plt.xlim(0.5,15.5)
    plt.xticks(k)
    plt.xlabel("k")
    # plt.title() -- wszystkie cechy
    plt.show()
    
    print('Dla wszystkich cech:')
    print('k = 5: ', calculateConfusionMatrix(normalizedTestData, normalizedTrainingData, 5));
    
    figure, axis1 = plt.subplots(3, 1, figsize=(10, 14))
    
    reducedTrainingData = reduceToTwoDimensions(normalizedTrainingData, 0, 1)
    reducedTestData = reduceToTwoDimensions(normalizedTestData, 0, 1)
    axis1[0].bar(k, getKNNSuccessPercentage(reducedTestData, reducedTrainingData))
    axis1[0].set_ylim(60, 101)
    axis1[0].set_xlim(0.5,15.5)
    axis1[0].set_xticks(k)
    axis1[0].set_xlabel('k')
    # axis1[0].title --- dlugosc dzialki kielicha, szerokosc dzialki kielicha
    
    print('dlugosc dzialki kielicha, szerokosc dzialki kielicha:')
    print('k = 4: ', calculateConfusionMatrix(reducedTestData, reducedTrainingData, 4));
    
    reducedTrainingData = reduceToTwoDimensions(normalizedTrainingData, 0, 2)
    reducedTestData = reduceToTwoDimensions(normalizedTestData, 0, 2)
    axis1[1].bar(k, getKNNSuccessPercentage(reducedTestData, reducedTrainingData))
    axis1[1].set_ylim(90, 101)
    axis1[1].set_xlim(0.5,15.5)
    axis1[1].set_xticks(k)
    axis1[1].set_xlabel('k')
    # axis1[1].title --- dlugosc dzialki kielicha, dlugosc platka
    
    print('dlugosc dzialki kielicha, dlugosc platka:')
    print('k = 11: ', calculateConfusionMatrix(reducedTestData, reducedTrainingData, 11));
    
    reducedTrainingData = reduceToTwoDimensions(normalizedTrainingData, 0, 3)
    reducedTestData = reduceToTwoDimensions(normalizedTestData, 0, 3)
    axis1[2].bar(k, getKNNSuccessPercentage(reducedTestData, reducedTrainingData))
    axis1[2].set_ylim(90, 101)
    axis1[2].set_xlim(0.5,15.5)
    axis1[2].set_xticks(k)
    axis1[2].set_xlabel('k')
    # axis1[2].title --- dlugosc dzialki kielicha, szerokosc platka
    
    print('dlugosc dzialki kielicha, szerokosc platka:')
    print('k = 5: ', calculateConfusionMatrix(reducedTestData, reducedTrainingData, 5));
    
    
    figure, axis2 = plt.subplots(3, 1, figsize=(10, 14))
    
    reducedTrainingData = reduceToTwoDimensions(normalizedTrainingData, 1, 2)
    reducedTestData = reduceToTwoDimensions(normalizedTestData, 1, 2)
    axis2[0].bar(k, getKNNSuccessPercentage(reducedTestData, reducedTrainingData))
    axis2[0].set_ylim(90, 101)
    axis2[0].set_xlim(0.5,15.5)
    axis2[0].set_xticks(k)
    axis2[0].set_xlabel('k')
    # axis2[0].title --- szerokosc dzialki kielicha, dlugosc platka
    
    print('szerokosc dzialki kielicha, dlugosc platka:')
    print('k = 5: ', calculateConfusionMatrix(reducedTestData, reducedTrainingData, 5));
    
    reducedTrainingData = reduceToTwoDimensions(normalizedTrainingData, 1, 3)
    reducedTestData = reduceToTwoDimensions(normalizedTestData, 1, 3)
    axis2[1].bar(k, getKNNSuccessPercentage(reducedTestData, reducedTrainingData))
    axis2[1].set_ylim(90, 101)
    axis2[1].set_xlim(0.5,15.5)
    axis2[1].set_xticks(k)
    axis2[1].set_xlabel('k')
    # axis2[1].title --- szerokosc dzialki kielicha, szerokosc platka
    
    print('szerokosc dzialki kielicha, szerokosc platka:')
    print('k = 3: ', calculateConfusionMatrix(reducedTestData, reducedTrainingData, 3));
    
    reducedTrainingData = reduceToTwoDimensions(normalizedTrainingData, 2, 3)
    reducedTestData = reduceToTwoDimensions(normalizedTestData, 2, 3)
    axis2[2].bar(k, getKNNSuccessPercentage(reducedTestData, reducedTrainingData))
    axis2[2].set_ylim(90, 101)
    axis2[2].set_xlim(0.5,15.5)
    axis2[2].set_xticks(k)
    axis2[2].set_xlabel('k')
    # axis2[1].title --- dlugosc platka, szerokosc platka
    
    print('dlugosc platka, szerokosc platka:')
    print('k = 1: ', calculateConfusionMatrix(reducedTestData, reducedTrainingData, 1));
    
    return 0;
    
main()




