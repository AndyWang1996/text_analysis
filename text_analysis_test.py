import nltk
import porter
from nltk.stem.wordnet import WordNetLemmatizer
import requests
from bs4 import BeautifulSoup
from nltk.probability import FreqDist
# from nltk.corpus import stopwords


def Q1():

    text = nltk.load('text_0.txt', encoding='gbk')  # code for Q1a

    # token_sentlist = nltk.sent_tokenize(text)
    #
    # token_list = []
    #
    # for sent in token_sentlist:
    #     token_list.append(nltk.word_tokenize(sent))

    token_list = nltk.word_tokenize(text)  # code for Q1a

    english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']',
                            '&', '!', '*', '@', '#', '$', '%', '"', '\'s', '``', "''"]

    token_list = [word for word in token_list if word not in english_punctuations]

    token_list1 = nltk.pos_tag(token_list)

    print(len(token_list1))   # code for Q1a

    print(token_list1)    # code for Q1a

    token_list2 = [w.lower() for w in token_list]

    token_list2 = nltk.pos_tag(token_list2)

    print(token_list2)


def Q2a():
    p = porter.PorterStemmer()
    text = nltk.load('text.txt', encoding='gbk')  # code for Q2a
    token_list = nltk.word_tokenize(text)
    english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']',
                            '&', '!', '*', '@', '#', '$', '%', '"', '\'s', '``', "''", "-"]

    token_list = [word for word in token_list if word not in english_punctuations]
    token_list1 = [w.lower() for w in token_list]
    print(token_list1)
    token_list2 = [p.stem(w) for w in token_list1]
    print(token_list2)


def Q2b():
    # nltk.download('wordnet')
    text = nltk.load('text.txt', encoding='gbk')  # code for Q2a
    token_list = nltk.sent_tokenize(text)
    english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']',
                            '&', '!', '*', '@', '#', '$', '%', '"', '\'s', '``', "''", "-"]
    token_list = [nltk.word_tokenize(sen) for sen in token_list]
    new_token = []
    for sens in token_list:
        sens = [word for word in sens if word not in english_punctuations]
        new_token.append(sens)

    new_token = [nltk.pos_tag(sen) for sen in new_token]
    print(new_token)
    lemmatized = []

    for sen in new_token:
        for word in sen:
            if "V" in word[1]:
                w = WordNetLemmatizer().lemmatize(word[0].lower(), 'v')
            else:
                w = WordNetLemmatizer().lemmatize(word[0], 'n')
            lemmatized.append(w.lower())
    # test = [WordNetLemmatizer().lemmatize(new_token)]
    # print(new_token[1])
    print(lemmatized)


def Q3():
    p = porter.PorterStemmer()
    stopwords = []
    with open('stopwords.txt', 'r') as f:
        for line in f:
            stopwords.append(line.rstrip())
        f.close()
    # print(stopwords)
    temp = requests.get("https://www.bbc.com/news/world-us-canada-49871909")
    temp.encoding = 'utf-8'
    soup = BeautifulSoup(temp.content, 'html.parser')
    text_1 = soup.find('div', {'class': 'story-body__inner'}).findAll('p')
    # text_1.remove('<p>')
    text_1 = [part.get_text() for part in text_1]
    text_1 = [nltk.word_tokenize(sen) for sen in text_1]
    english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']',
                            '&', '!', '*', '@', '#', '$', '%', '"', '\'s', '``', "''", "-"]
    text_1 = [[word for word in sens if word not in english_punctuations] for sens in text_1]
    text_1 = [[word for word in sens if word not in stopwords] for sens in text_1]
    text_1 = [nltk.pos_tag(sen) for sen in text_1]
    # print(text_1)

    result = []

    for sen in text_1:
        for word in sen:
            if "V" in word[1]:
                w = WordNetLemmatizer().lemmatize(word[0].lower(), 'v')
            elif "N" in word[1]:
                w = WordNetLemmatizer().lemmatize(word[0], 'n')
            else:
                w = p.stem(word[0])
            result.append(w.lower())
    # print(result)
    fdist = FreqDist(result)
    tops = fdist.most_common(40)
    print(tops)



# Q1()
# Q2a()
# Q2b()
Q3()