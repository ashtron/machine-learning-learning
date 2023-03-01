# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, "html.parser")

titles = soup.find_all(class_="indicate-hover")
clean_titles = list(map(lambda title: title.string, titles))

for title in clean_titles:
  print(title)
