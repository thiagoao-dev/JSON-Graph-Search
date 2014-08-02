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

# Busca em Largura (Breadth-First Search
def fbs(g, no):
    pass

# Busca em Profundidade (Depth-First Search)
def dfs(g, no, path = []):
    if no in g.keys():
        if no not in path:
            print("Expandido nó : ", no)
            path.append(no)
            '''
            if str(g[no][0]) not in path:
                print("Expadir nó : " + str(g[no][0]))
                dfs(g,str(g[no][0]),path)
            elif str(g[no][1]) not in path:
                print("Expadir nó : " + str(g[no][1]))
                dfs(g,str(g[no][1]),path)
            '''
    else:
        return False

def findNextNode(g, no):
    pass

# Recupera os vértices do json
arquivo  = readJson()
vertices = arquivo['vertices']
dfs(vertices,input("Qual vértice iniciará a busca: "))
