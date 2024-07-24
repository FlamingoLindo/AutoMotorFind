import json
import random

def random_country_func():
    # Load the JSON data from the file
    with open('Files\countries.json', 'r', encoding='utf-8') as file:
        countries = json.load(file)

    random_country_index = random.randint(0, len(countries) - 1)
    
    # Random country 
    random_country = countries[random_country_index]['name']
    
    return random_country