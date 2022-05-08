import scraper

def get_info(word):
    soup, sentences_soup = scraper.soupify(word)
    translation = scraper.english_translation(soup)
    random_number = scraper.generate_random_number(sentences_soup)

    if random_number >= 0:
        if random_number > 20:
            random_number = 19
        examples, indeces_furigana = scraper.furigana_indeces(sentences_soup, random_number)
        words = scraper.words_list(examples, random_number)
        furigana = scraper.furigana_list(examples, random_number)
        example = scraper.example_list(words, furigana, indeces_furigana)

        japanese = scraper.japanese_sentence(words)
        reading = scraper.japanese_readings(example)
        english = scraper.english_sentence(sentences_soup, random_number)
    else:
        japanese = ''
        reading = ''
        english = ''

    word_info = {'word': word, 'translation': translation, 'japanese': japanese, 'reading': reading, 'english': english}

    return word_info