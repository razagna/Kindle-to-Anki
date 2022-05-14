from bs4 import BeautifulSoup
import os

def extract_words(location):
    f = open(location, encoding="utf8")
    page = f.read()
    soup = BeautifulSoup(page,"html.parser")

    body_container = soup.find_all("div", class_ = "noteText")
    idx = len(body_container)

    new_words = []
    for id in range(idx):
        word = body_container[id].text.strip("\n")
        new_words.append(word)
    
    return new_words