import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://www.nykaa.com/search/result/?q=women%27s+watches&root=search&searchType=Misc&suggestionType=search&ssp=3&tst=watches&searchItem=women%27s%20watches&sourcepage=Search%20Page&")
print(response)

soup = BeautifulSoup(response.content,'html.parser')
print(soup)

names = soup.find_all('div',class_='css-xrzmfa')
print(names)

for i in names:
  d = i.get_text()
  print(d)

name = []
for i in names:
  d = i.get_text()
  name.append(d)
#print(name)

prices = [i.get_text() for i in soup.find_all('span', class_='css-111z9ua')]

cleaned_prices = [int(''.join(filter(str.isdigit, p))) if any(ch.isdigit() for ch in p) else None for p in prices]
print(cleaned_prices)

ratings = [i.get_text() for i in soup.find_all('span', class_='css-1qbvrhp')]

cleaned_ratings = [int(''.join(filter(str.isdigit, r))) if any(ch.isdigit() for ch in r) else None for r in ratings]
print(cleaned_ratings)


images = soup.find_all('img',class_='css-11gn9r6')
print(images)

for i in images[0:10]:
  d = i['src']
  #print(d)

image = []
for i in images[0:10]:
  d = i['src']
  image.append(d)
print(image)

print(len(name), len(cleaned_prices), len(cleaned_ratings), len(image))
min_length = min(len(name), len(cleaned_prices), len(cleaned_ratings), len(image))
print("Using min length:", min_length)

name = name[:min_length]
cleaned_prices = cleaned_prices[:min_length]
cleaned_ratings = cleaned_ratings[:min_length]
image = image[:min_length]

df = pd.DataFrame({
    'Names': name,
    'Prices': cleaned_prices,
    'Ratings': cleaned_ratings,
    'Images': image
})

df.to_csv("nyka.csv")
