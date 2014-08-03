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
def bfs(g, no):
    fila = []
    path = []
    # Enquanto o path for menor que o tamanho do grafo
    while len(path) < (len(g) - 1):
        # Caso o nó não esteja no visitados
        if no not in path:
            print("Expandido o nó: ", no)
            path = path+[int(no)]
        # Expandi as ações possíveis
        acoes = expandir(g,no)
        for acao in acoes:
            if acao not in path:
                print("Do nó: ", no, " expandido o nó: ", acao)
                path = path+[acao]
                fila = fila+[acao]
        fila.sort()
        no = fila.pop()
    return path

# Busca em Profundidade (Depth-First Search)
def dfs(g, no, path = []):
    # Verifica se o valor do nó é válido
    if len(path) < (len(g)-1) and int(no) > 0:
        # Add o nó no path
        if no not in path: path.append(int(no))
        print("Expandido nó : ", no)
        acoes = expandir(g, no)
        print("Possíveis ações", acoes)
        for acao in acoes:
            if acao not in path:
                dfs(g,acao,path)
                break
        dfs(g, int(no)-1, path)
    return path

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

# Recupera os vértices do json e inicia o código
arquivo  = readJson()

print("Saída: ", bfs(arquivo['vertices'],input("Qual vértice iniciará a busca: ")))
#print("Saída: ", dfs(arquivo['vertices'],input("Qual vértice iniciará a busca: ")))
