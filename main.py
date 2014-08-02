__author__ = 'ThiagoAugustus'

import json

# Lê o arquivo json
def readJson():
    # Abre o arquivo conforme o caminho informado
    with open(input("Informe o nome do arquivo.json: ")) as json_file:
        json_file = json.load(json_file)
        # Testa o objeto
        assert isinstance(json_file, object)
        return json_file

# Recupera os vértices do json
vertices = readJson()['vertices']

def buscaEmLargura(g, no):
    pass