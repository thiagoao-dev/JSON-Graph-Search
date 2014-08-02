__author__ = 'ThiagoAugustus'

import json
import copy

# Lê o arquivo json
def readJson():
    # Abre o arquivo conforme o caminho informado
    with open(input("Informe o nome do arquivo.json: ")) as json_file:
        json_file = json.load(json_file)
        # Testa o objeto
        assert isinstance(json_file, object)
        return json_file

# Busca em Largura (Breadth-First Search
def fbs(g, no):
    pass

# Busca em Profundidade (Depth-First Search)
def dfs(g, no = '0', path = []):
    if str(no) in g.keys():
        print("Expandido nó : ", no)
        path.append(int(no))
        acoes = expandir(g, no)
        for acao in acoes:
            if acao not in path:
                dfs(g,acao,path)
                break
        print(path)
        return False

def expandir(g, no):
    nodes = []
    g2 = copy.deepcopy(g)
    for n,v in g2.items():
        for i in v:
            if int(no) == i:
                v.remove(int(no))
                nodes.append(v[0])
    nodes.sort()
    return nodes

# Recupera os vértices do json
arquivo  = readJson()
vertices = arquivo['vertices']
dfs(vertices,input("Qual vértice iniciará a busca: "))
