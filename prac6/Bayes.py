import nltk
from nltk.corpus import names
import random


def gender_features1(word):
    return {'last_letter': word[-1]}

def gender_features2(word):
    return {'fisrt&last_letter': word[0] + "" + word[-1]}


def gender_features3(word):
    return {'fisrt_2_letters': word[0] + "" + word[1]}


def gender_features4(word):
    return {'fisrt_2&last_letters': word[0] + "" + word[1] + "" + word[-1]}


def gender_features5(word):
    return {'fisrt_letters': word[0]}


def gender_features6(word):
    return {'last_2_letters': word[-2] + '' + word[-1]}


# gender_features('Shrek') = {'last_letter': 'k'}

male_names = [(name, 'male') for name in names.words('male.txt')]
female_names = [(name, 'female') for name in names.words('female.txt')]
labeled_names = male_names + female_names
random.shuffle(labeled_names)

featuresets = [(gender_features1(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
classifier.show_most_informative_features(5)
print(nltk.classify.accuracy(classifier, test_set))
ans = classifier.classify(gender_features1('Dora'))
print(ans)

featuresets = [(gender_features2(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
classifier.show_most_informative_features(5)
print(nltk.classify.accuracy(classifier, test_set))

featuresets = [(gender_features3(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
classifier.show_most_informative_features(5)
print(nltk.classify.accuracy(classifier, test_set))

featuresets = [(gender_features4(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
classifier.show_most_informative_features(5)
print(nltk.classify.accuracy(classifier, test_set))

featuresets = [(gender_features5(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
classifier.show_most_informative_features(5)
print(nltk.classify.accuracy(classifier, test_set))

featuresets = [(gender_features6(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
classifier.show_most_informative_features(5)
print(nltk.classify.accuracy(classifier, test_set))
