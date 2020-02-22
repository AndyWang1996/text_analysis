import distance
import prac5.wangyikai as wyk
import nltk
import matplotlib.pyplot as plt
__author__ = 'user'

#  transposition flag allows transpositions edits (e.g., “ab” -> “ba”),

# s1 = 'dr mark keane'
# s2 = 'mr mark bean'
#
# s3 = 'rain'
# s4 = 'shine'
#
# s5 = 'mr rowan atkinson'
# s6 = 'mr bean'


def txt_handler(txt):
    txt = txt.replace('\r', '')
    txt = txt.replace('\t', '')
    txt = txt.split('\n')
    txt = [item for item in txt if len(item) > 0]
    return txt


normal = nltk.load('./normal_tweet.txt', encoding='gbk')
normal = txt_handler(normal)
spam = nltk.load('./spam.txt', encoding='gbk')
spam = txt_handler(spam)

# print(normal[0])
x1 = []
value1 = []
x2 = []
value2 = []
x3 = []
value3 = []
x4 = []
value4 = []
x5 = []
value5 = []

for tweet in spam:
    value1.append(wyk.edit_distance(normal[0], tweet, transpositions=False))
    x1.append(1)
    value2.append(wyk.edit_distance(normal[1], tweet, transpositions=False))
    x2.append(2)
    value3.append(wyk.edit_distance(normal[2], tweet, transpositions=False))
    x3.append(3)
    value4.append(wyk.edit_distance(normal[3], tweet, transpositions=False))
    x4.append(4)
    value5.append(wyk.edit_distance(normal[4], tweet, transpositions=False))
    x5.append(5)

print(value1)
print(value2)
print(value3)
print(value4)
print(value5)

axe = plt.subplot(1, 1, 1, facecolor='white')
axe.scatter(x1, value1, color='r')
axe.scatter(x2, value2, color='g')
axe.scatter(x3, value3, color='b')
axe.scatter(x4, value4, color='k')
axe.scatter(x5, value5, color='c')
x = range(1, 6, 1)
plt.xticks(x)
plt.show()
# ans = wyk.edit_distance(s1, s2, transpositions=False)
# print(ans)
#
# ans = wyk.edit_distance(s3, s4, transpositions=False)
# print(ans)
#
# ans = wyk.edit_distance(s5, s6, transpositions=False)
# print(ans)
#
# ans = distance.levenshtein(s1, s2)
# print(ans)
#
# ans = distance.levenshtein(s3, s4)
# print(ans)
#
# ans = distance.levenshtein(s5, s6)
# print(ans)
