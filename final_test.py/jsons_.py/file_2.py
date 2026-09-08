# Load a JSON string into a Python dictionary with json.loads() and print one specific field.

import json

movies = {
    "title" : "3 Idiots",
    "year"  : 2009,
    "rating": 8.4
}

# Converting to a json string
json_string = json.dumps(movies)

print()
# loading back to dictionary
movie_dic = json.loads(json_string)
print(movie_dic["year"])