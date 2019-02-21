"""
Name: Vishal Sundareshwaran
UTA_ID : 1001572777
Reference: https://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/
"""
import csv
import sys



#laad the csv file and prepare the traning set
def loadCSVFile(filename, training=[]):

    csvdata = open(filename, 'r')
    data = csv.reader(csvdata)
    dataset = list(data)
    for instance in range(len(dataset)):
        for features in range(len(dataset[instance]) - 1):
            dataset[instance][features] = float(dataset[instance][features])
        if 1 == 1:
            training.append(dataset[instance])
import operator
import math

# calcuate the distance between given 2 points
def calculateDistance(training_instance1, training_instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((training_instance1[x] - training_instance2[x]), 2)
    return math.sqrt(distance)


# get the nearest neighbours for the input data
def findNeighbours(training, testInstance, k):
    # getting the distance and sorting accordingly
    distances = []
    length = len(testInstance)
    for instance in training:
        dist = calculateDistance(testInstance, instance, length)
        print('Distance from %s to %s = %f' % (testInstance, instance, dist))
        distances.append((instance, dist))
    distances.sort(key=operator.itemgetter(1))
    # extracting top k neighbours
    neighbours = []
    for instance in range(k):
        neighbours.append(distances[instance][0])
    return neighbours


# perform the gender prediction
# returns 'M' for Man and 'W' for Woman
def predictGender(k_neighbours):
    classes = {}
    for neighbour in k_neighbours:
        predict_Class = neighbour[-1]
        if predict_Class in classes:
            classes[predict_Class] += 1
        else:
            classes[predict_Class] = 1
    sortedClass = sorted(classes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClass[0][0]


# classifies the input with respect to the traning data and starts the predictions and returns the output
def knn(X, test, k):
    print('k: ' + repr(k))
    neighbours = findNeighbours(X, test, k)
    prediction = predictGender(neighbours)
    return prediction



if __name__ == '__main__':
    
    #command line arguments
    csvFile = sys.argv[1]
    height = int(sys.argv[2])
    weight = int(sys.argv[3])
    age = int(sys.argv[4])
    k = int(sys.argv[5])
    X = []  # Training set
    loadCSVFile(csvFile, X)
    print('Predicted class: ' + knn(X, [height,weight,age], k))