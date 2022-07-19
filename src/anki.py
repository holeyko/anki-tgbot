import os
from shutil import rmtree

import mariadb

import config as cfg
import credentials as creds


class Card:
    def __init__(self, front="", back="", front_image_name="", back_image_name=""):
        self.front = front
        self.back = back
        self.front_image_name = front_image_name
        self.back_image_name = back_image_name


def add_folder(user_id, deck_path):
    os.makedirs(os.path.join(cfg.PATH_TO_DATA, str(user_id), *deck_path.split(".")), exist_ok=True)

def get_deck_id(user_id, deck_path):
    cursor.execute("SELECT deck_id FROM decks WHERE user_id=? AND name=?", (user_id, deck_path))
    return next(cursor)[0]

def make_folder_as_deck(user_id, deck_path):
    cursor.execute("INSERT INTO decks (user_id, name) VALUES (?, ?)", (user_id, deck_path))
    deck_id = get_deck_id(user_id, deck_path)

    path = os.path.join(cfg.PATH_TO_DATA, str(user_id), *deck_path.split("."))
    os.makedirs(os.path.join(path, cfg.NAME_FOLDER_WITH_IMAGES), exist_ok=True)

    with open(os.path.join(path, cfg.NAME_XML_DATA_FILE), "w") as xml_file:
        xml_file.write(f"<?xml version=\"{cfg.XML_VERSION}\" encoding=\"{cfg.XML_ENCODING}\"?>\n")
        xml_file.write(f"<deck {cfg.XML_DECK_ID}=\"{deck_id}\" {cfg.XML_DECK_NAME}=\"{deck_path}\" {cfg.XML_DECK_COUNT_REPEATS}=\"0\"></deck>\n")

def make_deck_as_folder(user_id, deck_path):
    deck_id = get_deck_id(user_id, deck_path)
    cursor.execute("DELETE FROM decks WHERE user_id=? AND name=?", (user_id, deck_path))
    cursor.execute("DELETE FROM cards WHERE deck_id=?", (deck_id, ))

    path = os.path.join(cfg.PATH_TO_DATA, str(user_id), *deck_path.split("."))
    for name in os.listdir(path):
        inner = os.path.join(path, name)
        if os.path.isfile(inner):
            os.remove(inner)
        else:
            rmtree(inner)

def remove_folder(user_id, folder_name):
    pass

def add_card_to_deck(user_id, deck_name, card):
    pass

def remove_card_from_deck(user_id, deck_name, card):
    pass


def start_learn(user_id, deck_name):
    pass


def show_res(user_id, deck_name):
    pass


connection = mariadb.connect(
    host=creds.DB_HOST,
    user=creds.DB_USER_NAME,
    password=creds.DB_USER_PWD,
    database=creds.DB_DATABASE_NAME,
    autocommit=True
)
cursor = connection.cursor()
