__author__ = 'user'
# http://pythonprogramming.net/support-vector-machine-svm-example-tutorial-scikit-learn-python/

import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm


def accuracy(predict=[], target=[]):
    k = 0
    error = 0
    while k != len(predict):
        if predict[k] != target[k]:
            error += 1
            k += 1
            continue
        else:
            k += 1
            continue
    # print(target)
    # print('accuracy = ' + str(1 - (error / len(predict))))
    return 1 - (error / len(predict))

# print(digits)

# classifier = svm.SVC(gamma=0.0001, C=1)

# print(len(digits))

# x, y = digits.data[1:1500], digits.target[1:1500]
# classifier.fit(x, y)

# print(digits.data[:-1])

# predict = classifier.predict(digits.data[1501:])
# target = digits.target[1501:]

# print(predict)


def v_gamma():
    digits = datasets.load_digits()
    x, y = digits.data[1:1500], digits.target[1:1500]
    g = []
    a = []
    gamma = 0.0001
    C = 0.01
    while C < 2:
        classifier = svm.SVC(gamma=gamma, C=C)
        classifier.fit(x, y)
        g.append(C)
        a.append(accuracy(classifier.predict(digits.data[1501:]), digits.target[1501:]))
        C += 0.01
        C = round(C, 4)
        print(C)

    axe = plt.subplot(1, 1, 1, facecolor='white')
    axe.set_xlabel('C')
    axe.set_ylabel('Accuracy')
    axe.plot(g, a, linestyle='-', color='b')
    plt.show()
# print('Prediction:', len(classifier.predict(digits.data[501:])))
# print(len(digits.target[:-1]))

# plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation='nearest')
# plt.xlim(1, 10)
# plt.ylim(1, 10)
# plt.show()
v_gamma()