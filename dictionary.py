# A simple dictionary app that imports a basic datafile (data.json) and based on user input provides the definition
# Allows for typos, upper and lowercase letters and uses the get_close_matches function from difflib

import json
from difflib import get_close_matches 

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data, 1, 0.8)) > 0:
        keep_going = input("Did you mean %s instead? Type Y for yes and N for no: " % get_close_matches(word, data.keys())[0])
        if keep_going is 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif keep_going == "N":
            return "The word doesn't appear to exist in this database."
        else:
            return "We didn't understand your query"
    else:
        return "The word doesn't exist in this database. Please double check it"

word = input("Enter input: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
