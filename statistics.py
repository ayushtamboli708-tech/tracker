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

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("1. Mean")
print("2. Median")
print("3. Mode")
print("4. Range")
print("5. Variance")
print("6. Standard Deviation")
while True:

    choice = int(input("Enter choice: "))

    if choice == 1:
        print(mean(lst))
    elif choice == 2:
        print(median(lst))
    elif choice == 3:
        print(mode(lst))
    elif choice == 4:
        print(find_range(lst))
    elif choice == 5:
        print(variance(lst))
    elif choice == 6:
        print(std(lst))
    loo = input(":wanna do more  y/n   ")
    if loo == "n":
        break