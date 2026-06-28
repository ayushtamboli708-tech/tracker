import re
text = 'The quick brown fox jumps over the lazy dog'
match = re.match(r'The quick brown fox', text,re.IGNORECASE)
print(match)
print(match.span())
match = re.search('lazy', text,re.IGNORECASE)
print(match)
print(match.span())
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
matches = re.findall('python', txt,re.IGNORECASE)
print(matches)
match = re.sub('python', 'java', txt,re.IGNORECASE)
print(match)
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\t', txt)) 