import json
import random
import requests

from coursework_2.basic_word import BasicWord

def load_random_word():
    response = requests.get("https://www.jsonkeeper.com/b/WI39")
    data = json.loads(response.text)
    word = random.choice(data)
    return BasicWord(word["word"], word["subwords"])


