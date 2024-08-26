import PySimpleGUI as sg
import get_highlights
import generate_cards
import sys

if __name__ == "__main__":
    layout1 = [  [sg.Text("Select a file to load Kindle highlights from:")],
                [sg.Input(size=60), sg.FileBrowse(key="highlights")],
                [sg.Text("Select a location to save your cards in:")],
                [sg.Input(size=60), sg.FolderBrowse(key="destination")],
                [sg.Text("Pick the format of the cards:"), sg.Radio('Anki Deck', "RADIO1", key="anki", default=True), sg.Radio('Excel Sheet', "RADIO1")],
                [sg.Text("File Name:"), sg.Input(key="filename", size=39), sg.Button("Generate"), sg.Button("Cancel")]  
            ]

    if getattr(sys, 'frozen', False):
        load_icon = os.path.join(sys._MEIPASS, "assets/loading_icon.gif")
    else:
        load_icon = "assets/loading_icon.gif"

    layout2 = [  [sg.Text('Loading....', font='ANY 15')],
                [sg.Image(load_icon, key='loading')],
                [sg.Button('Cancel')]   ]

    # ----------- Create actual layout using Columns and a row of Buttons
    layout = [[sg.Column(layout1, key='COL1', visible=True), sg.Column(layout2, key='COL2', visible=False)],]

    window = sg.Window('Kindle to Anki', layout, size=(530, 200))

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break

        if event == "Generate":
            words = get_highlights.extract_words(values["highlights"])

            if values["anki"] == True:
                generate_cards.create_package(words[0], values["destination"], values["filename"])
            else:
                generate_cards.create_sheet(words[0], values["destination"], values["filename"])

    window.close()