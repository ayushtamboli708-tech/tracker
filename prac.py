
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add("twitter")
print('twitter' in it_companies)
com={"com1","compe2","cpm3"}
it_companies.update(com)
it_companies.pop()
print(A.union(B))
print(B.union(A))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
del it_companies
st = set(age)
if len(age) > len(st):
    print("The list has duplicate ages")

st=" am a teacher and I love to inspire and teach people."
stw=[st.split]
str=set(stw)
print(st)
print(str)