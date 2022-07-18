import mariadb

from credentials import *

class Card:
    def __init__(self, front, front_image_path, back, back_image_path):
        self.front = front
        self.front_image_path = front_image_path
        self.back = back
        self.back_image_path = back_image_path

def check_row_in_db(request):
    pass

def add_folder_deck(user_id, deck_name):
    pass

def set_folder_as_deck(deck_name):
    pass

def add_card(user_id, deck_name, card):
    pass

connection = mariadb.connect(
    host=DB_HOST,
    user=DB_USER_NAME,
    password=DB_USER_PWD,
    database=DB_DATABASE_NAME
)
cursor = connection.cursor()
print(DB_HOST)