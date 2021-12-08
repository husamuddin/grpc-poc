import re
import json
from os import path

def get_all_countries():
    filename = path.join(
        path.dirname(__file__),
        './mocked_data/countries.json'
    )

    with open(filename, 'r') as file:
        dataString = file.read()

    return json.loads(dataString)


def list_countries(name=None):
    data = get_all_countries()

    return [
        country for country in data['features']
        if re.compile("^{}$".format(name.lower())).match(country['properties']['name'].lower())
    ]
