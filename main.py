__author__ = 'ThiagoAugustus'

import json

def readJson():

    with open(input("Informe o nome do arquivo.json: ")) as json_file:
        json_file = json.load(json_file)
        assert isinstance(json_file, object)
        return json_file

print(readJson())