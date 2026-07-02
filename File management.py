import requests
import json
from bs4 import BeautifulSoup
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

data = {
    "title": soup.title.text,
    "heading": soup.h1.text,
    "body": soup.body.text
}
with open('data.json','w') as  f:
    json.dump(data,f,indent=4)
print("Data has been written to data.json")
print(data)