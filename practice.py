import re
from collections import Counter

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text):
    # Remove every character except letters and spaces
    cleaned = re.sub(r'[^A-Za-z\s]', '', text)
    return cleaned

def most_frequent_words(text):
    words = text.split()
    count = Counter(words)
    return count.most_common(3)

cleaned_text = clean_text(sentence)

print(cleaned_text)
print(most_frequent_words(cleaned_text))