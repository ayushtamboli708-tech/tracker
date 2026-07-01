from collections import Counter

def mean(lst):
    return sum(lst) / len(lst)

def median(lst):
    lst.sort()
    return lst[len(lst)//2]

def mode(lst):
    count = Counter(lst)
    return count.most_common(1)[0][0]

def find_range(lst):
    maximum = max(lst)
    minimum = min(lst)
    return maximum - minimum

def variance(lst):
    m = mean(lst)
    total = 0

    for i in lst:
        total += (i - m) ** 2

    return total / len(lst)

def std(lst):
    return variance(lst) ** 0.5

