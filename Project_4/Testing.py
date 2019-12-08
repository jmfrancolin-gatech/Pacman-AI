from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle
from math import pow, sqrt

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData()
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData,maxItr = 200,hiddenLayerList =  hiddenLayers)






def learningWithRestarts():

    print "Learning With Restarts"

    print "PenData"
    data = []
    for i in range(5):
        data.append(testPenData()[1])

    print "max: ", max(data)
    print "avg: ", average(data)
    print "std: ", stDeviation(data)

    print "CarData"
    data = []
    for i in range(5):
        data.append(testCarData()[1])

    print "max: ", max(data)
    print "avg: ", average(data)
    print "std: ", stDeviation(data)


def varyingTheHiddenLayer():

    print "Pen Data"
    file = open('q6PenData.csv','w')
    file.write('hidden layers, max, avg, std\n')

    perceptrons = 0
    while perceptrons <= 40:
        data = []
        for i in range (2):
            data.append(testPenData(hiddenLayers=[perceptrons])[1])

        string =  str(perceptrons) + ',' + str(max(data)) + ','  + \
                str(average(data)) + ',' + str(stDeviation(data)) + "\n"
        file.write(string)

        # file.write({d}.format(perceptrons) + ',' + {f}.format(max(data)) + ',' + \
        #     {f}.format(average(data)) + ',' + {d}.format(average(data)) + '\n')

        print "Perceptrons: ", perceptrons
        print "Car Data Max: ", max(data)
        print "Car Data Avg: ", average(data)
        print "Car Data SD: ", stDeviation(data)
        perceptrons += 5
    file.close()

    print "Car Data"
    file = open('q6CarData.csv','w')
    file.write('hidden layers, max, avg, std\n')

    perceptrons = 0
    while perceptrons <= 40:
        data = []
        for i in range (2):
            data.append(testCarData(hiddenLayers=[perceptrons])[1])

        string =  str(perceptrons) + ',' + str(max(data)) + ','  + \
                str(average(data)) + ',' + str(stDeviation(data)) + "\n"
        file.write(string)
        print "Perceptrons: ", perceptrons
        print "Car Data Max: ", max(data)
        print "Car Data Avg: ", average(data)
        print "Car Data SD: ", stDeviation(data)
        perceptrons += 5
    file.close()

# testCarData()
# learningWithRestarts()
varyingTheHiddenLayer()
