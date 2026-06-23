def add_num(*args):
    print("here")
    sum=0
    for i in args:
        sum +=i
        print("here2")
    return sum
    print("here3")

print(add_num(2,4,6,9))
print("here4")
