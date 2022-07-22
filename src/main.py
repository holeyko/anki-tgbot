import telegram

from credentials import *
import anki

def main():
    anki.add_folder(1234213, "English.Main folder.Pack 2")
    anki.make_folder_as_deck(1234213, "English.Main folder.Pack 2")
    anki.make_deck_as_folder(1234213, "English.Main folder.Pack 2")
    anki.connection.close()

if __name__ == "__main__":
    main()