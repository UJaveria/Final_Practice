# Convert a dictionary describing a movie (title, year, rating) to a JSON string with json.dumps() and print it.
import json

movie = {
    "title" : "3 Idiots",
    "year"  : 2009,
    "rating": 8.4
}
# Converting to a json string
json_string = json.dumps(movie)
print(json_string)
print(type(json_string))