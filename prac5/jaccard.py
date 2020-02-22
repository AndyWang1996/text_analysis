def jaccard_index(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    ans = float(len(set1 & set2)) / len(set1 | set2)
    return round(ans, 2)


def jaccard_distance(str1, str2):
    # set1 = set(str1.split())
    # set2 = set(str2.split())
    # ans = float(len(set1 | set2) - len(set1 & set2)) / len(set1 | set2)
    # return round(ans, 2)
    return 1 - jaccard_index(str1, str2)


def dice_coefficient(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    ans = float(2 * len(set1 & set2) / (len(set1) + len(set2)))
    return round(ans, 2)


book1 = 'novel science space alien technology'
book2 = 'novel magic love friendship war'
book3 = 'novel strong destiny struggle fish'
book4 = 'novel tragedy destiny prince drama'
book5 = 'novel humanitarian love society paris'
book6 = 'novel science humanitarian monster technology'

books = [book1, book2, book3, book4, book5, book6]

ctr1 = 1
ctr2 = 1
for book in books:
    for book_a in books:
        if book != book_a:
            print('The distance between book' + str(ctr1) +
                  ' and book' + str(ctr2) +
                  'is: ' + str(dice_coefficient(book, book_a)))
            ctr2 += 1
        else:
            ctr2 += 1
            continue
    ctr1 += 1
    ctr2 = 1

# base = "roy harper album stormy"
# target1 = "roy rovers comic sport"
# target2 = "roy harper album flashes"
# target3 = "roy green storm cock blip blop"
# target4 = "roy harper album stormy"

# ans1 = jaccard_index(base, target1)
# ans2 = jaccard_index(base, target2)
# ans3 = jaccard_index(base, target3)
# ans4 = jaccard_index(base, target4)

# ans1 = jaccard_distance(base, target1)
# ans2 = jaccard_distance(base, target2)
# ans3 = jaccard_distance(base, target3)
# ans4 = jaccard_distance(base, target4)

# print([ans1, ans2, ans3, ans4])



