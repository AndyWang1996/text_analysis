# Example of kNN implemented from Scratch in Python
# By Jason Brownlee
# http://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/


import csv
import random
import math
import operator
import matplotlib.pyplot as plt


def loadDataset(filename, split, trainingSet=[], testSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])


def N_fold_Dataset(filename, N, folds=[[]]):
    with open(filename, 'r') as csvfile:    #load the data from file
        lines = csv.reader(csvfile)         #filename: the path of data file
        dataset = list(lines)               #N: how many folds to divide
                                            #folds=[[]]: a 2D array to carry the result
        for x in range(N-1):                #expend the size of folds due to N
            folds.append([])
        for x in range(len(dataset) - 1):   #randomly add elements in dataset into folds[n]
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            folds[random.randint(0, N-1)].append(dataset[x])
    for subset in folds:
        print(len(subset))


def fold_join(n, folds=[[]], test=[], train=[]):
    ctr = 0
    for item in folds:
        if ctr == n:
            for i in item:
                test.append(i)
            ctr += 1
        else:
            for i in item:
                train.append(i)
            ctr += 1
        # print(test)


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0


def main():
    axe = plt.subplot(1, 1, 1, facecolor='white')
    axe.set_xlabel('K')
    axe.set_ylabel('Accuracy')
    # prepare data

    # split = 0.9
    split = 0.6
    GAP = 0.02
    # generate predictions

    k = 1
    split_set = []
    k_set = []
    accuracy_set = []
    while(k < 21):

        ctr = 0
        accuracy = 0

        while(ctr < 100):
            trainingSet = []
            testSet = []
            predictions = []
            loadDataset('iris.csv', split, trainingSet, testSet)
            # print('Train set: ' + repr(len(trainingSet)))
            # print('Test set: ' + repr(len(testSet)))
            for x in range(len(testSet)):
                neighbors = getNeighbors(trainingSet, testSet[x], k)
                result = getResponse(neighbors)
                predictions.append(result)
            # print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
            accuracy += getAccuracy(testSet, predictions)
            ctr += 1

        k_set.append(k)
        accuracy_set.append(accuracy/100)
        print('k = ' + str(k) + ' Accuracy: ' + repr(accuracy/100) + '%')
        k += 1

    axe.plot(k_set, accuracy_set, linestyle='-', color='b')
    axe.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    axe.set_yticks([94, 94.5, 95, 95.5, 96, 96.5])
    plt.show()


def five_fold():
    folds = [[]]
    N_fold_Dataset('iris.csv', 5, folds)
    k = 0
    while k != 5:
        test = []
        train = []
        predictions = []
        fold_join(k, folds, test, train)
        print(len(train))
        print(len(test))
        for x in range(len(test)):
            neighbors = getNeighbors(train, test[x], 5)
            result = getResponse(neighbors)
            predictions.append(result)
        accuracy = getAccuracy(test, predictions)
        print(accuracy)
        k += 1




five_fold()
# main()