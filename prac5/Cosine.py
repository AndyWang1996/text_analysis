__author__ = 'user'
# bits from
# http://stackoverflow.com/questions/15173225/how-to-calculate-cosine-similarity-given-2-sentence-strings-python
# load_docs, process_docs and compute_vector by MK
import math
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

vector_dict = {}


# Just loads in all the documents
def load_docs():
    print("Loading docs...")

    book1 = ('d1', 'novel science space alien technology')
    book2 = ('d2', 'novel magic love friendship war')
    book3 = ('d3', 'novel strong destiny struggle fish')
    book4 = ('d4', 'novel tragedy destiny prince drama')
    book5 = ('d5', 'novel humanitarian love society paris')
    book6 = ('d6', 'novel science humanitarian monster technology')
    book7 = ('d7', 'novel science space alien technology')
    book8 = ('d8', 'novel science space blah technology')
    # book7 = ('d7', 'novel science space alien technology blah blue blow blot blob')

    doc1 = ('d1', 'LSI tutorials and fast tracks')
    doc2 = ('d2', 'books on semantic analysis')
    doc3 = ('d3', 'learning latent semantic indexing')
    doc4 = ('d4', 'advances in structures and advances in indexing')
    doc5 = ('d5', 'analysis of latent structures')
    # return [doc1, doc2, doc3, doc4, doc5]
    return [book1, book2, book3, book4, book5, book6, book7, book8]


# Computes TF for words in each doc, DF for all features in all docs; finally whole Tf-IDF matrix
def process_docs(all_dcs):
    stop_words = ['of', 'and', 'on', 'in']
    all_words = []
    counts_dict = {}
    for doc in all_dcs:
        words = [x.lower() for x in doc[1].split() if x not in stop_words]
        words_counted = Counter(words)
        unique_words = list(words_counted.keys())
        counts_dict[doc[0]] = words_counted
        all_words = all_words + unique_words
    n = len(counts_dict)
    df_counts = Counter(all_words)
    compute_vector_len(counts_dict, n, df_counts)
    print(len(all_words))


# computes TF-IDF for all words in all docs
def compute_vector_len(doc_dict, no, df_counts):
    global vector_dict
    for doc_name in doc_dict:
        doc_words = doc_dict[doc_name].keys()
        wd_tfidf_scores = {}
        for wd in list(set(doc_words)):
            wds_cts = doc_dict[doc_name]
            wd_tf_idf = wds_cts[wd] * math.log(no / df_counts[wd], 10)
            wd_tfidf_scores[wd] = round(wd_tf_idf, 4)
        vector_dict[doc_name] = wd_tfidf_scores


def get_cosine(text1, text2):
    vec1 = vector_dict[text1]
    vec2 = vector_dict[text2]
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    else:
        return round(float(numerator) / denominator, 3)


def distance(d1, d2):
    vec1 = vector_dict[d1]
    vec2 = vector_dict[d2]
    intersection = set(vec1.keys()) & set(vec2.keys())
    dist = sum(abs(vec1[x] - vec2[x]) for x in intersection)
    dist += sum(vec1[x] for x in set(vec1.keys()) if x not in intersection)
    dist += sum(vec2[x] for x in set(vec2.keys()) if x not in intersection)
    return dist


def e_distance(d1, d2):
    vec1 = vector_dict[d1]
    vec2 = vector_dict[d2]
    intersection = set(vec1.keys()) & set(vec2.keys())
    dist = sum((vec1[x] - vec2[x])**2 for x in intersection)
    dist += sum(vec1[x]**2 for x in set(vec1.keys()) if x not in intersection)
    dist += sum(vec2[x]**2 for x in set(vec2.keys()) if x not in intersection)
    return math.sqrt(dist)


# RUN
all_docs = load_docs()
process_docs(all_docs)
# vector_dict['q'] = {'semantic': 1, 'latent': 1, 'indexing': 1}
# vector_dict['q'] = {'novel': 1, 'science': 1, 'love': 1}

# for keys, values in vector_dict.items():
#     print(keys, values)

# text1 = 'd1'
# text5 = 'd5'
# text6 = 'd6'
# text2 = 'q'
# cosine1 = get_cosine(text1, text5)
# cosine2 = get_cosine(text1, text6)
# cosine3 = get_cosine(text5, text6)
# print(distance(text1, text5))
# print(distance(text1, text6))
# print(distance(text5, text6))
# print('Cosine: 1&5', cosine1)
# print('Cosine: 1&6', cosine2)
# print('Cosine: 5&6', cosine3)
axe = plt.subplot(1, 1, 1, facecolor='white')
x = []
y = []
i = 1
while i != 8:
    j = i+1
    while j != 9:
        key1 = 'd' + str(i)
        key2 = 'd' + str(j)
        print(key1 + '|' + key2)
        x.append(e_distance(key1, key2))
        y.append(get_cosine(key1, key2))
        j += 1
    i += 1
# print(x)
# print(y)
# axe.set_title('similarity & e_distance')
# x = [distance(text1, text5), distance(text5, text6), distance(text1, text6)]
# y = [cosine1, cosine3, cosine2]
axe.scatter(x, y)
plt.show()
i = 0
while i != 28:
    print('(' + str(x[i]) + ',' + str(y[i]) + ')')
    i += 1




