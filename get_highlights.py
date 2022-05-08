from bs4 import BeautifulSoup
import os

location = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(location, 'kindle_highlights.html'), encoding="utf8")
page = f.read()
soup = BeautifulSoup(page,"html.parser")

body_container = soup.find_all("div", class_ = "noteText")
idx = len(body_container)

new_words = []
for id in range(idx):
    word = body_container[id].text.strip("\n")
    new_words.append(word)