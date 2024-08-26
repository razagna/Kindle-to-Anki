import genanki
import random
import codecs
import get_highlights
import create_item
import pandas as pd

front = codecs.open('template/front.html', 'r').read()
back = codecs.open('template/back.html', 'r').read()

simple_deck = genanki.Deck(
        2059400110,
        'Simple Deck'
    )

simple_model = genanki.Model(
    random.randrange(1 << 30, 1 << 31), #model id must be unique
    'simple_KtoA',
    fields=[
        {'name': 'Expression'},
        {'name': 'Reading'},
        {'name': 'Meaning'},
        {'name': 'Notes'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': front,
            'afmt': back,
        },
    ])

def create_card(word):
    info = create_item.get_info(word)

    simple_note = genanki.Note(
        model=simple_model,
        fields=[info.get('japanese'),
                info.get('reading'),
                info.get('english'),
                info.get('translation')]
    )

    return simple_note

def create_sheet(words, location, filename):
    data_frame = 0
    data_frame = pd.DataFrame(columns=['word', 'translations', 'japanese', 'readings','english'])

    for word in words:
        new_row = create_item.get_info(word)
        data_frame = data_frame.append(new_row, ignore_index=True)

    data_frame.to_excel(location + '/' + filename + '.xlsx', index=False)

def create_package(words, location, filename):
    # for i in range(len(words)):
    #     word = words[i]
    #     card = create_card(word)
    #     simple_deck.add_note(card)

    for word in words:
        card = create_card(word)
        simple_deck.add_note(card)

    genanki.Package(simple_deck).write_to_file(location + '/' + filename + '.apkg')