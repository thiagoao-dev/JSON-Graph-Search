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
    # Verifica se o nó está no grafo
    if str(no) in g.keys():
        # Verifica se o nó ainda não foi verificado
        if no not in path:
            print("Expandido nó : ", no)
            path.append(int(no))
            acoes = expandir(g, no)
            for acao in acoes:
                if acao not in path:
                    dfs(g,acao,path)
                    break
            return False
            print(path)
    return False

# Função que retorna as possíveis ações
def expandir(g, no):
    # Cria uma lista de ações
    nodes = []
    # Cria uma cópia do grafo para manipulação
    g2 = copy.deepcopy(g)
    # Varre todos os nós do grafo
    for n,v in g2.items():
        # Verifica se em cada tupla há uma ligação com o nó
        for i in v:
            # Caso o nó exista na tupla
            if int(no) == i:
                # Remove o nó atual
                v.remove(int(no))
                # Adciona o nó que faz link na lista
                nodes.append(v[0])
    # Organiza os nós por ordem númerica
    nodes.sort()
    return nodes

# Recupera os vértices do json
arquivo  = readJson()
vertices = arquivo['vertices']
dfs(vertices,input("Qual vértice iniciará a busca: "))
