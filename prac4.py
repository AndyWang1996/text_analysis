import nltk
import csv
import xlwt
import numpy as np
from math import log


def Q1():
    text = []
    stopwords = nltk.load('stopwords.txt')
    english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']',
                            '&', '!', '*', '@', '#', '$', '%', '"', '\'s', '``', "''"]
    i = 1
    while i <= 10:
        path = '/txt/' + str(i) + '.txt'
        temp = nltk.load(path, encoding='gbk')
        temp = nltk.word_tokenize(temp)
        temp = [words.lower() for words in temp]
        temp = [words for words in temp if words not in english_punctuations]
        temp = [words for words in temp if words not in stopwords]
        text.append(temp)
        i += 1

    #print(text)
    wordlist = []
    for sens in text:
        for words in sens:
            if words not in wordlist:
                wordlist.append(words)
            else:
                continue

    print(len(wordlist))
    wb = xlwt.Workbook()
    ws = wb.add_sheet('TF')
    i = 0
    while i != len(wordlist):
        ws.write(i+1, 0, label=wordlist[i])
        i += 1

    i = 0
    while i != 10:
        ws.write(0, i+1, label='text' + str(i+1))
        i += 1

    i = 0
    while i != 10:
        j = 0
        for word in wordlist:
            ctr = 0
            for item in text[i]:
                if word == item:
                    ctr += 1
                else:
                    continue
            ws.write(j + 1, i + 1, label=ctr)
            j += 1
        i += 1
    wb.save('data.xls')


def to_csv(text):
    with open(r'./output.csv', 'w', newline='',) as f:
        writer = csv.writer(f)
        for sens in text:
            writer.writerow(sens)


def txt_handle():
    with open(r'./output1.txt', 'r', newline='')as f:
        txt = f.read()
        txt = txt.replace(',',' ')
        print(txt)


def PMI():
    text = []
    stopwords = nltk.load('stopwords.txt')
    english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']',
                            '&', '!', '*', '@', '#', '$', '%', '"', '\'s', '``', "''"]
    i = 1
    while i <= 10:
        path = '/txt/' + str(i) + '.txt'
        temp = nltk.load(path, encoding='gbk')
        temp = nltk.word_tokenize(temp)
        temp = [words.lower() for words in temp]
        temp = [words for words in temp if words not in english_punctuations]
        temp = [words for words in temp if words not in stopwords]
        text.append(temp)
        i += 1

    pairs = []
    words = nltk.load('word1.txt')
    words = nltk.word_tokenize(words)
    wb = xlwt.Workbook()
    ws = wb.add_sheet('TF')
    # print(words)
    i = 0
    for word in words:
        for sens in text:
            if word in sens:
                for item in sens:
                    if item in words and item != word:
                        temp1 = item + ' ' + word
                        temp2 = word + ' ' + item
                        if temp1 not in pairs and temp2 not in pairs:
                            pairs.append(temp2)
                            ws.write(i + 1, 0, word)
                            ws.write(i + 1, 1, item)
                            i += 1

    print(pairs)
    wb.save('PMI.xls')


def ent():
    random = []
    spam = []
    stopwords = nltk.load('stopwords.txt')
    english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']',
                            '&', '!', '*', '@', '#', '$', '%', '"', '\'s', '``', "''"]
    i = 1
    while i <= 10:
        path = '/txt/random/tweet' + str(i) + '.txt'
        temp = nltk.load(path, encoding='gbk')
        temp = nltk.word_tokenize(temp)
        temp = [words.lower() for words in temp]
        temp = [words for words in temp if words not in english_punctuations]
        temp = [words for words in temp if words not in stopwords]
        random.append(temp)
        i += 1

    i = 1
    while i <= 10:
        path = '/txt/spam/tweet' + str(i) + '.txt'
        temp = nltk.load(path, encoding='gbk')
        temp = nltk.word_tokenize(temp)
        temp = [words.lower() for words in temp]
        temp = [words for words in temp if words not in english_punctuations]
        temp = [words for words in temp if words not in stopwords]
        spam.append(temp)
        i += 1

    # random = np.array(random)
    # spam = np.array(spam)

    # print(random)
    # print(spam)
    ent_random = 0.0
    random = [' '.join(tweet) for tweet in random]
    spam = [' '.join(tweet) for tweet in spam]

    print(calcShannonEnt(random))
    print(calcShannonEnt(spam))

    # print(calc_ent(np.array(random)))

    # print(calc_ent(np.array(spam)))
    # ent_random += calc_ent(np.array(tweet))
    # print(ent_random)
    #
    # ent_spam = 0.0
    # for tweet in spam:
    #     ent_spam += calc_ent(np.array(tweet))
    # print(ent_spam)


def calcShannonEnt(dataSet):
    numEntries = len(dataSet) # 样本数
    labelCounts = {} # 该数据集每个类别的频数
    for featVec in dataSet:  # 对每一行样本
        currentLabel = featVec[-1] # 该样本的标签
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
            labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries # 计算p(xi)
        shannonEnt -= prob * log(prob, 2)  # log base 2
    return shannonEnt


def calc_ent(x):
    x_value_list = set([x[i] for i in range(x.shape[0])])
    ent = 0.0
    for x_value in x_value_list:
        p = float(x[x == x_value].shape[0]) / x.shape[0]
    logp = np.log2(p)
    ent -= p * logp
    return ent
    # print(ent)


ent()
# PMI()
# Q1()
# txt_handle()
