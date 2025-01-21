from zadanie_3 import *
import matplotlib.pyplot as plt

def main():
    
    # load data
    trainingData = fileLoader('data3_train.csv') 
    testData = fileLoader('data3_test.csv')
    
    #normalize data
    normalizedTrainingData = minMaxScaling(trainingData)
    normalizedTestData = [minMaxScalingPoint(x, trainingData) for x in testData]
    
    print(getKNNSuccessPercentage(normalizedTestData, normalizedTrainingData))
    
    return 0;
    
main()




