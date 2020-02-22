import re
import math
import collections
import sys


def tokenize(_str):
    stopwords = []
    with open('stopwords.txt', 'r') as f:
        for line in f:
            stopwords.append(line.rstrip())
        f.close()
    tokens = collections.defaultdict(int)
    for m in re.finditer(r"(\w+)", _str, re.UNICODE):
        m = m.group(1).lower()
        if len(m) < 2:
            continue
        if m in stopwords:
            continue
        tokens[m] += 1
    return tokens


def kldiv(_s, _t):
    if (len(_s) == 0) or (len(_t) == 0):
        return 1e33
    ssum = 0. + sum(_s.values())
    # slen = len(ssum)

    tsum = 0. + sum(_t.values())
    # tlen = len(tsum)

    vocabdiff = set(_s.keys()).difference(set(_t.keys()))
    lenvocabdiff = len(vocabdiff)

    epsilon = min(min(_s.values())/ssum, min(_t.values())/tsum) * 0.001

    gamma = 1 - lenvocabdiff * epsilon

    sc = sum([v/ssum for v in _s.values()])
    st = sum([v/tsum for v in _t.values()])

    if sc < 9e-6 or st < 9e-6:
        print("Sum P: %e, Sum Q: %e" % (sc, st))
        print("*** ERROR: sc does not sum up to 1. Bailing iut ..")
        sys.exit(2)

    div = 0.

    for t, v in _s.items():
        pts = v / ssum
        ptt = epsilon
        if t in _t:
            ptt = gamma * (_t[t] / tsum)

        ckl = (pts - ptt) * math.log(pts / ptt)

        div += ckl

    return div


def run():
    sentence1 = 'john fell down harry fell as-well down by the stream the sun shone before it went down mary was fine'
    sentence2 = 'bill fell down jeff fell too down by the river the sun shone until it sunk down belinda was ill'
    sentence3 = 'abey jump up david jump up too up to the teaching building the sun shone until the class was finish'
    print('kldiv - s1-s2:', kldiv(tokenize(sentence1), tokenize(sentence2)))
    print('kldiv - s2-s1:', kldiv(tokenize(sentence2), tokenize(sentence1)))
    print('kldiv - s1-s3:', kldiv(tokenize(sentence1), tokenize(sentence3)))
    print('kldiv - s3-s1:', kldiv(tokenize(sentence3), tokenize(sentence1)))
    print('kldiv - s2-s3:', kldiv(tokenize(sentence2), tokenize(sentence3)))
    print('kldiv - s3-s2:', kldiv(tokenize(sentence3), tokenize(sentence2)))

run()
