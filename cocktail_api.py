import string
import requests

COCKTAIL_DB_ENDPOINT = "https://www.thecocktaildb.com/api/json/v1/1/"


def get_all_cocktails():
    cocktails = {letter: None for letter in list(string.ascii_lowercase)}
    for letter in cocktails:
        response = requests.get(url=f"{COCKTAIL_DB_ENDPOINT}search.php?f={letter}")
        json = response.json()
        cocktails[letter] = json['drinks']

    return cocktails


def look_up_cocktail(cocktail_id):
    response = requests.get(url=f"{COCKTAIL_DB_ENDPOINT}lookup.php?i={cocktail_id}")
    cocktail_json = response.json()
    return cocktail_json['drinks'][0]


def get_random_cocktail():
    response = requests.get(url=f"{COCKTAIL_DB_ENDPOINT}random.php")
    random_json = response.json()
    return random_json['drinks'][0]
