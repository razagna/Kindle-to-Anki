import get_highlights
#import sys  
#sys.path.insert(0, get_highlights.location)
import scraper
import pandas as pd

if __name__ == "__main__":

    df = 0
    df = pd.DataFrame(columns=['word', 'translations', 'japanese', 'readings','english'])

    for word in get_highlights.new_words[0:5]:
        soup, sentences_soup = scraper.soupify(word)
        translations = scraper.english_translation(soup)
        random_number = scraper.generate_random_number(sentences_soup)

        if random_number >= 0:
            if random_number > 20:
                random_number = 19
            examples, indeces_furigana = scraper.furigana_indeces(sentences_soup, random_number)
            words = scraper.words_list(examples, random_number)
            furigana = scraper.furigana_list(examples, random_number)
            example = scraper.example_list(words, furigana, indeces_furigana)

            japanese = scraper.japanese_sentence(words)
            readings = scraper.japanese_readings(example)
            english = scraper.english_sentence(sentences_soup, random_number)
        else:
            japanese = ''
            readings = ''
            english = ''

        new_row = {'word': word, 'translations': translations, 'japanese': japanese, 'readings': readings, 'english': english}
        df = df.append(new_row, ignore_index=True)

    df.to_excel('vocab_list.xlsx', index=False)