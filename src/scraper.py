from bs4 import BeautifulSoup
import requests
import random

def soupify(query):
    url = 'https://jisho.org/search/' + query
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')

    sentences_url = 'https://jisho.org/search/' + query + '%20%23sentences'
    sentences_response = requests.get(sentences_url)
    sentences_soup = BeautifulSoup(sentences_response.text,'html.parser')

    return soup, sentences_soup

def english_translation(soup):
    translations = soup.findAll('span', class_ = "meaning-meaning")
    if not translations:
        translations =''
    else:
        translations = translations[0].text
    return translations

def generate_random_number(sentences_soup):
    sentences_num = sentences_soup.findAll('span', class_ = "result_count")
    if not sentences_num:
        random_number = -1
    else:
        sentences_num = int(sentences_num[0].text[3:5])
        random_number = random.randint(0,sentences_num-1)
    
    return random_number

def furigana_indeces(sentences_soup, random_number):
    examples = sentences_soup.find_all("ul", class_ = "japanese_sentence japanese japanese_gothic clearfix")
    example = examples[random_number].find_all("li", class_ = "clearfix")
    exsl = list(example)

    stringfied_example = []
    indeces_furigana = []

    for itm in exsl:
        stringfied_example.append(str(itm))

    for item in stringfied_example:
        if 'furigana' in item:
            indeces_furigana.append(stringfied_example.index(item))

    return examples, indeces_furigana

def words_list(examples, random_number):
    example_soup = examples[random_number].find_all('span', class_ = "unlinked")
    words = []
    for word in example_soup:
        if word.find_all(class_ = 'furigana') is not None:
            words.append(word.text)

    return words

def furigana_list(examples, random_number):
    examples_soup = examples[random_number].find_all("li", class_ = "clearfix")
    furigana =[]
    for item in range(len(examples_soup)):
        classs = examples_soup[item].find('span', class_ = "furigana")
        if classs is not None:
            furigana.append(classs.text)

    return furigana

def example_list(words, furigana, furigana_indeces):
    flag = False
    example = []
    for word_idx in range(len(words)):
        for furigana_idx in furigana_indeces:
            if furigana_idx == word_idx:
                if furigana_idx != 0:
                    example.extend((" ",words[furigana_idx],"[",furigana[furigana_indeces.index(word_idx)],"]"))
                else:
                    example.extend((words[furigana_idx],"[",furigana[furigana_indeces.index(word_idx)],"]"))
                flag = True
        if flag == False:
            example.append(words[word_idx])
        flag = False

    return example

def japanese_sentence(words):
    japanese = ""
    for word in words:
        japanese += str(word)

    japanese = japanese + "。"

    return japanese

def japanese_readings(example):
    readings = ""
    for element in example:
        readings += str(element)

    readings = readings + "。"

    return readings

def english_sentence(sentences_soup, random_number):
    english = sentences_soup.find_all("div", class_ = "sentence_content")
    english = english[random_number].div.span.text

    return english